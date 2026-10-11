const {test, expect} = require('@playwright/test');
const fs = require('fs');
const data = topic => JSON.parse(fs.readFileSync(`data/${topic}.json`, 'utf8'));
const budget = id => `#expense-${id}-budget`;
const storageKey = 'malta-trip-2026-10-13-19-expenses-v1';

test('overview and event desk are exact canonical projections, including unknown weekend times', async ({page}) => {
  await page.goto('index.html');
  await expect(page.locator('[data-record-ref]')).toHaveCount(6);
  const records = ['activities','transport','food','everyday','radio'].flatMap(t=>data(t).records);
  for (const card of await page.locator('[data-record-ref]').all()) {
    const id = await card.getAttribute('data-record-ref');
    const record = records.find(r=>r.id === id);
    expect(record).toBeTruthy();
    await expect(card.locator('h3')).toHaveText(record.name);
    await expect(card.locator('p').first()).toHaveText(record.description);
    const href = await card.locator('a').getAttribute('href');
    expect(href.endsWith('#' + id)).toBeTruthy();
  }
  await page.goto('event.html#twc-teams-format');
  await expect(page.locator('#event-evidence')).toHaveAttribute('open','');
  await expect(page.locator('#twc-teams-format')).toBeInViewport();
  await page.goto('event.html#twc-day-2026-10-18');
  await expect(page.locator('[data-record-list] .record-card')).toHaveCount(6);
  await expect(page.locator('[data-topic-data] .record-card')).toHaveCount(data('event').records.length);
  await expect(page.locator('#twc-day-2026-10-18')).toBeInViewport();
  for (const record of data('activities').records.filter(r=>r.id === 'twc-finals-2026' || r.id.startsWith('twc-day-'))) {
    const card = page.locator('#' + record.id);
    await expect(card.locator('h3')).toHaveText(record.name);
    await expect(card.locator('p').first()).toHaveText(record.description);
    await expect(card.locator('dd').nth(1)).toHaveText(record.hours);
    await expect(card.locator('dd').nth(2)).toHaveText(record['price range']);
    await expect(card.locator('.record-notes p')).toHaveText(record.notes);
    await expect(card.locator('a.record-source').first()).toHaveAttribute('href', record.source_url);
  }
});

test('expense JSON backup round-trips only after consent; invalid imports leave data alone', async ({page}) => {
  await page.goto('costs.html');
  await page.locator(budget('flights')).fill('480.25');
  await page.locator('#expense-flights-actual').fill('481');
  await page.locator('#expense-flights-note').fill('<b>Receipt "A"</b>');
  const downloading = page.waitForEvent('download');
  await page.getByRole('button', {name:'Download JSON backup'}).click();
  const download = await downloading;
  const contents = fs.readFileSync(await download.path());
  const backup = JSON.parse(contents);
  expect(backup.currency).toBe('EUR');
  expect(Object.keys(backup.entries)).toHaveLength(25);
  await page.locator(budget('flights')).fill('9');
  const upload = {name:'backup.json', mimeType:'application/json', buffer:contents};
  await page.locator('#restore-json').setInputFiles(upload); // default dismiss
  await expect(page.locator('#save-status')).toContainText('cancelled');
  await expect(page.locator(budget('flights'))).toHaveValue('9');
  page.once('dialog', d=>d.accept());
  await page.locator('#restore-json').setInputFiles(upload);
  await expect(page.locator(budget('flights'))).toHaveValue('480.25');
  await expect(page.locator('#actual-total')).toHaveText('€481.00');
  await expect(page.locator('#expense-flights-note')).toHaveValue('<b>Receipt "A"</b>');
  await page.reload();
  await expect(page.locator(budget('flights'))).toHaveValue('480.25');
  for (const mutation of [b=>{b.currency='USD'}, b=>{b.entries.flights.budget='-1'}, b=>{b.entries.flights.budget='1.234'}, b=>{b.entries.flights.note='x'.repeat(241)}, b=>{b.entries.unknown={}}, b=>{b.entries.flights=null}]) {
    const invalid = structuredClone(backup); mutation(invalid);
    await page.locator('#restore-json').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(invalid))});
    await expect(page.locator('#save-status')).toContainText('not restored');
    await expect(page.locator(budget('flights'))).toHaveValue('480.25');
  }
});

test('quick-fill rejects unsafe currency/amounts, sums categories and invalidates stale previews', async ({page}) => {
  await page.goto('costs.html');
  await page.locator('#itinerary-input').fill([
    '2026-10-13 | Flight | USD 480',
    '2026-10-14 | Dinner | 12.50',
    '2026-10-15 | Lunch | €20,25',
    '2026-10-15 | Lunch | €20,25',
    '2026-10-14 | Hotel tax | 9',
    "2026-10-14 | Museum in Ta' Qali | 10",
    '2026-10-14 | Rental car insurance | 25',
    '2026-10-14 | Esports event ticket | 0',
    '2026-10-14 | Taxi | -8',
    '2026-10-14 | Bus pass | 1,234',
    '2026-10-14 | eSIM | 1.234,56',
    '2026-10-14 | Laundry | 1,234.56',
    '2026-10-14',
    '2026-10-14 | Flight 1234'
  ].join('\n'));
  await page.getByRole('button',{name:'Preview matches'}).click();
  await expect(page.locator('#itinerary-preview')).toContainText('combined 2 distinct lines = €32.75');
  await page.getByRole('button',{name:'Apply preview to blank budget fields'}).click();
  await expect(page.locator(budget('flights'))).toHaveValue('');
  await expect(page.locator(budget('food-and-drink'))).toHaveValue('32.75');
  await expect(page.locator(budget('hotel-separate-charges'))).toHaveValue('9.00');
  await expect(page.locator(budget('hotel-stay'))).toHaveValue('');
  await expect(page.locator(budget('activities-and-sightseeing'))).toHaveValue('10.00');
  await expect(page.locator(budget('event-commute'))).toHaveValue('');
  await expect(page.locator(budget('car-rental'))).toHaveValue('25.00');
  await expect(page.locator(budget('event-access'))).toHaveValue('0.00');
  await expect(page.locator(budget('taxi-rideshare'))).toHaveValue('');
  await expect(page.locator(budget('local-bus-and-cards'))).toHaveValue('');
  await expect(page.locator(budget('mobile-connectivity'))).toHaveValue('1234.56');
  await expect(page.locator(budget('other-incidentals'))).toHaveValue('1234.56');
  await page.locator('#itinerary-input').fill('2026-10-13 | Flight | 10');
  await page.getByRole('button',{name:'Preview matches'}).click();
  await expect(page.locator('#apply-itinerary')).toBeEnabled();
  await page.locator('#itinerary-input').fill('2026-10-13 | Flight | 20');
  await expect(page.locator('#apply-itinerary')).toBeDisabled();
  await expect(page.locator(budget('flights'))).toHaveValue('');
});

test('filtered deep links, malformed hashes and Escape navigation remain usable', async ({page}) => {
  const errors=[]; page.on('pageerror',e=>errors.push(e.message));
  await page.setViewportSize({width:360,height:800});
  await page.goto('radio.html#%');
  await expect(page.locator('.record-card')).toHaveCount(data('radio').records.length);
  await page.locator('input[type=search]').fill('NO_MATCH_987');
  await page.locator('a[href="#bbc-world-service-dab-sportsworld"]').first().click();
  await expect(page.locator('#bbc-world-service-dab-sportsworld')).toBeVisible();
  await expect(page.locator('input[type=search]')).toHaveValue('');
  await page.locator('.nav-toggle').click();
  await page.keyboard.press('Escape');
  await expect(page.locator('.nav-toggle')).toHaveAttribute('aria-expanded','false');
  await expect(page.locator('.nav-toggle')).toBeFocused();
  expect(errors).toEqual([]);
});

test('partial summary failure does not hide successful topics; all load actions fail safely', async ({page}) => {
  await page.route('**/data/radio.json',route=>route.fulfill({status:503,body:'unavailable'}));
  await page.goto('index.html');
  await expect(page.locator('[data-overview] [data-record-ref]')).toHaveCount(5);
  await expect(page.locator('[data-overview] .callout-danger')).toContainText('Summary unavailable');
  await page.route('**/data/activities.json',route=>route.fulfill({status:503,body:'unavailable'}));
  await page.goto('event.html');
  await expect(page.locator('[data-record-list] .callout-danger')).toHaveCount(2);
  await page.route('**/data/expenses.json',route=>route.fulfill({status:503,body:'unavailable'}));
  await page.goto('costs.html');
  await expect(page.locator('#export-json')).toBeDisabled();
  await expect(page.locator('#restore-json')).toBeDisabled();
  await expect(page.locator('#download-template')).toBeDisabled();
  await expect(page.locator('#preview-itinerary')).toBeDisabled();
});

test('site works mounted below a GitHub-Pages-style project prefix', async ({page}) => {
  await page.route('**/project-prefix/**', async route=> {
    const url = new URL(route.request().url());
    url.pathname = url.pathname.replace('/project-prefix/','/');
    await route.fulfill({response:await route.fetch({url:url.href})});
  });
  await page.goto('project-prefix/index.html');
  await expect(page.locator('[data-record-ref]')).toHaveCount(6);
  await page.locator('.hero-actions a').first().click();
  await expect(page).toHaveURL(/project-prefix\/event.html$/);
  await expect(page.locator('[data-record-list] .record-card')).toHaveCount(6);
  await expect(page.locator('[data-topic-data] .record-card')).toHaveCount(data('event').records.length);
  await page.locator('a[href="costs.html#event-access"]').click();
  await expect(page).toHaveURL(/project-prefix\/costs.html#event-access$/);
  await expect(page.locator('[data-expense-row]')).toHaveCount(25);
});

test('legacy routes and no-JavaScript fallback still provide onward links', async ({browser,page}) => {
  for (const path of ['hotel.html','hotspawn.html','itinerary.html','landmarks.html','logistics.html','qawra.html']) {
    await page.goto(path);
    await expect(page.locator('main h1')).toHaveCount(1);
    for (const link of await page.locator('main a').all()) {
      const href = await link.getAttribute('href');
      expect(fs.existsSync(href.split('#')[0])).toBeTruthy();
    }
  }
  const context=await browser.newContext({javaScriptEnabled:false});
  const noJS=await context.newPage();
  await noJS.goto(new URL('sources.html',page.url()).href);
  await expect(noJS.locator('noscript strong')).toHaveText('JavaScript is off.');
  await expect(noJS.getByRole('link',{name:'Transport',exact:true})).toHaveAttribute('href','data/transport.json');
  await context.close();
});


test('backup normalizes valid numeric input and rejects malformed, oversized or wrong-trip files', async ({page}) => {
  await page.goto('costs.html');
  await page.locator(budget('flights')).fill('.5');
  await page.locator('#expense-flights-actual').fill('1e2');
  await expect(page.locator('#budget-total')).toHaveText('€0.50');
  const downloading=page.waitForEvent('download');
  await page.getByRole('button',{name:'Download JSON backup'}).click();
  const backup=JSON.parse(fs.readFileSync(await (await downloading).path(),'utf8'));
  expect(backup.entries.flights).toEqual({budget:'0.50',actual:'100.00',note:''});
  page.once('dialog',d=>d.accept());
  await page.locator('#restore-json').setInputFiles({name:'valid.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(backup))});
  await expect(page.locator(budget('flights'))).toHaveValue('0.50');
  await expect(page.locator('#expense-flights-actual')).toHaveValue('100.00');
  // Long leading-zero representations must not silently lose the significant digit.
  const padded=structuredClone(backup);padded.entries.flights.budget='0000000000000000000000000000001.25';
  page.once('dialog',d=>d.accept());
  await page.locator('#restore-json').setInputFiles({name:'padded.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(padded))});
  await expect(page.locator(budget('flights'))).toHaveValue('1.25');
  const invalidContents=[Buffer.from('{bad json'),Buffer.alloc(1048577,32),Buffer.from('null')];
  for (const mutate of [b=>{b.format='other'},b=>{b.version=2},b=>{b.trip='2025-10-13/2025-10-19'},b=>{b.entries=[]},b=>{b.entries.flights.budget=2},b=>{b.entries.flights.extra='x'},b=>{b.entries.flights.budget='1000000001'},b=>{delete b.entries.flights.note},b=>{b.entries=JSON.parse('{"__proto__":{"polluted":true}}')}]) {
    const invalid=structuredClone(backup);mutate(invalid);invalidContents.push(Buffer.from(JSON.stringify(invalid)));
  }
  for (const buffer of invalidContents) {
    await page.locator('#restore-json').setInputFiles({name:'invalid.json',mimeType:'application/json',buffer});
    await expect(page.locator('#save-status')).toContainText('not restored');
    await expect(page.locator(budget('flights'))).toHaveValue('1.25');
    await expect(page.locator('#actual-total')).toHaveText('€100.00');
  }
  expect(await page.evaluate(()=>({}).polluted)).toBeUndefined();
});

test('quick-fill keeps refundable holds out of totals and flags explicit wrong years', async ({page}) => {
  await page.goto('costs.html');
  await page.locator('#itinerary-input').fill([
    '2026-10-13 | Hotel refundable deposit | 100',
    '2026-10-13 | Car hire security deposit | 500',
    '2026-10-13 | Hotel pre-authorisation | 200',
    '2026-10-13 | Card hold | 30',
    '14 Oct 2025 | Unclassified purchase | 8',
    'Oct 14, 2025 | Unclassified purchase | 9',
    '2026-10-14 | Dinner | 12.50'
  ].join('\n'));
  await page.getByRole('button',{name:'Preview matches'}).click();
  await expect(page.locator('#itinerary-preview')).toContainText('keep refundable holds in notes');
  await expect(page.locator('#itinerary-preview')).toContainText('date is outside');
  await page.getByRole('button',{name:'Apply preview to blank budget fields'}).click();
  await expect(page.locator('#budget-total')).toHaveText('€12.50');
  for (const id of ['hotel-stay','hotel-separate-charges','car-rental','daily-2026-10-14']) await expect(page.locator(budget(id))).toHaveValue('');
});
