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

test('date-by-date transport plan and opening matchups render from canonical records', async ({page}) => {
  await page.goto('getting-around.html#event-day-by-date');
  await expect(page.locator('#event-day-by-date .day-plan > li')).toHaveCount(7);
  expect(await page.locator('#event-day-by-date time').evaluateAll(n => n.map(x => x.dateTime))).toEqual([
    '2026-10-13','2026-10-14','2026-10-15','2026-10-16','2026-10-17','2026-10-18','2026-10-19'
  ]);
  const plan = data('transport').records.find(r => r.id === 'event-day-transport-by-date');
  await expect(page.locator('#event-day-transport-by-date h3')).toHaveText(plan.name);
  await expect(page.locator('#event-day-transport-by-date .record-notes p')).toHaveText(plan.notes);
  // Every evidence link inside the derived plan must resolve to a rendered record card.
  const hrefs = await page.locator('#event-day-by-date a[href^="#"]').evaluateAll(a => a.map(x => x.getAttribute('href')));
  expect(hrefs.length).toBeGreaterThanOrEqual(7);
  for (const href of hrefs) await expect(page.locator(href), href).toBeVisible();
  await page.goto('event.html#opening-matchups');
  await expect(page.locator('#opening-matchups .card')).toHaveCount(3);
  await page.goto('event.html#twc-opening-matchups-14-oct');
  await expect(page.locator('#event-evidence')).toHaveAttribute('open', '');
  const matchup = data('event').records.find(r => r.id === 'twc-opening-matchups-14-oct');
  await expect(page.locator('#twc-opening-matchups-14-oct')).toBeInViewport();
  await expect(page.locator('#twc-opening-matchups-14-oct h3')).toHaveText(matchup.name);
  await expect(page.locator('#twc-opening-matchups-14-oct dd').nth(1)).toHaveText(matchup.hours);
  await expect(page.locator('#twc-opening-matchups-14-oct .record-notes p')).toHaveText(matchup.notes);
});

test('radio trip-week listening plan is labelled on mobile and a semantic table on desktop', async ({page}) => {
  await page.setViewportSize({width:360,height:850});
  await page.goto('radio.html#listening-plan');
  await expect(page.locator('#listening-plan h2')).toContainText('13–19 October 2026');
  await expect(page.locator('#listening-plan tbody tr')).toHaveCount(12);
  const radioRecords=data('radio').records;
  const sportiva=radioRecords.find(r=>r.id==='radio-sportiva-dab-plus');
  const bbc=radioRecords.find(r=>r.id==='bbc-world-service-dab-sportsworld');
  expect(sportiva.hours).toContain('15:05–17:00');
  expect(bbc.hours).toContain('15:06 and 16:06 Malta time');
  await expect(page.locator('#listening-plan')).toContainText('15:05–17:00 as published');
  await expect(page.locator('#listening-plan')).toContainText('15:06 start');
  await expect(page.locator('#listening-plan')).toContainText('Diretta Sp.+Calciom.');
  await expect(page.locator('#listening-plan')).toContainText('Diretta Sportiva');
  await expect(page.locator('#listening-plan')).toContainText('5–11 October only');
  await expect(page.locator('#scan-checklist')).toBeVisible();
  await expect(page.locator('#listening-plan')).toContainText('15:06 start');
  await expect(page.locator('#listening-plan')).toContainText('16:06 start');
  await expect(page.locator('#listening-plan')).toContainText('starts after the published Saturday 13:30 Malta EPL kick-off');
  await expect(page.locator('#listening-plan')).toContainText('starts after the published Sunday 15:00 Malta EPL kick-offs');
  await expect(page.locator('#listening-plan')).toContainText('No named match');
  for (const width of [320,360,720]) {
    await page.setViewportSize({width,height:850});
    const mobile = await page.locator('#listening-plan tbody tr').first().locator('td').evaluateAll(cells => ({
      display: getComputedStyle(cells[0]).display,
      labels: cells.map(cell=>cell.getAttribute('data-label')),
      pageWidth: document.documentElement.scrollWidth,
      viewport: window.innerWidth
    }));
    expect(mobile.display).toBe('grid');
    expect(mobile.labels).toEqual(['When (Malta)','Service & tuning','Programme','Evidence / limitation']);
    expect(mobile.pageWidth).toBeLessThanOrEqual(mobile.viewport);
  }
  await page.setViewportSize({width:1440,height:900});
  const desktopDisplay = await page.locator('#listening-plan tbody td').first().evaluate(cell=>getComputedStyle(cell).display);
  expect(desktopDisplay).toBe('table-cell');
  const sourceLinks = await page.locator('#listening-plan > p a[href^="https://"]').count();
  expect(sourceLinks).toBeGreaterThanOrEqual(8);
});

test('trip-window live-sport table separates fixtures from radio carriage', async ({page}) => {
  const radioRecords = data('radio').records;
  const bfbs = radioRecords.find(r=>r.id==='bfbs-radio-2-epl-not-a-malta-service');
  const pbs = radioRecords.find(r=>r.id==='pbs-radju-malta-radio-sports-carriage-lead');
  const window = radioRecords.find(r=>r.id==='other-sports-13-19-oct-outside-window');
  expect(bfbs.confidence).toBe('partially verified');
  expect(bfbs.notes).toContain('31 March 1979');
  expect(pbs.description).toContain('93.7 MHz');
  expect(pbs.description).toContain('105.9 MHz');
  expect(window.hours).toContain('20–21 October');
  expect(window.hours).toContain('13 and Wednesday 14 October');
  expect(window.hours).toContain('23–25 October');

  await page.setViewportSize({width:360,height:850});
  await page.goto('radio.html#trip-window-live-sport');
  await expect(page.locator('#trip-window-live-sport h2')).toContainText('Trip-window live sport');
  await expect(page.locator('#trip-window-live-sport tbody tr')).toHaveCount(6);
  await expect(page.locator('#trip-window-live-sport')).toContainText('13:30');
  await expect(page.locator('#trip-window-live-sport')).toContainText('15:30');
  await expect(page.locator('#trip-window-live-sport')).toContainText('BFBS Malta closed on 31 March 1979');
  await expect(page.locator('#trip-window-live-sport')).toContainText('outside your dates');
  const labels = await page.locator('#trip-window-live-sport tbody tr').first().locator('td')
    .evaluateAll(cells => ({display: getComputedStyle(cells[0]).display, labels: cells.map(c=>c.getAttribute('data-label'))}));
  expect(labels.display).toBe('grid');
  expect(labels.labels).toEqual(['When (Malta)','Fixture / event','Terrestrial radio carriage']);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBeTruthy();

  await page.setViewportSize({width:1440,height:900});
  const desktopDisplay = await page.locator('#trip-window-live-sport tbody td').first().evaluate(cell=>getComputedStyle(cell).display);
  expect(desktopDisplay).toBe('table-cell');
  const sources = await page.locator('#trip-window-live-sport a[href^="https://"]').count();
  expect(sources).toBeGreaterThanOrEqual(5);
  await expect(page.locator('#bfbs-radio-2-epl-not-a-malta-service h3')).toHaveText(bfbs.name);
  await expect(page.locator('#bfbs-radio-2-epl-not-a-malta-service .record-notes p')).toHaveText(bfbs.notes);
  await expect(page.locator('#pbs-radju-malta-radio-sports-carriage-lead .record-notes p')).toHaveText(pbs.notes);
  await expect(page.locator('#other-sports-13-19-oct-outside-window .record-notes p')).toHaveText(window.notes);
});

test('hotel outlet records keep their own facts (no cross-record contamination)', async ({page}) => {
  const food = data('food').records;
  const espresso = food.find(r=>r.id==='espresso-odycy');
  const minoa = food.find(r=>r.id==='minoa-ax-odycy');
  // Regression: the Espresso record once carried Minoa's hours, address, source and review figures.
  expect(espresso.hours).toContain('24/7');
  expect(espresso.hours).not.toEqual(minoa.hours);
  expect(espresso.source_url).toBe('https://axhotelsmalta.com/odycy/qawra-restaurants/espresso-grab-and-go/');
  expect(espresso.source_url).not.toBe(minoa.source_url);
  expect(espresso.address).toContain('Level 0');
  expect(minoa.address).toContain('Level 11');
  expect(espresso.description).not.toContain('Best of the Best');
  expect(minoa.notes).toContain('Best of the Best');
  await page.goto('restaurants.html#espresso-odycy');
  await expect(page.locator('#espresso-odycy h3')).toHaveText(espresso.name);
  await expect(page.locator('#espresso-odycy .record-notes p')).toHaveText(espresso.notes);
  await expect(page.locator('#espresso-odycy')).toContainText('24/7');
  // The Espresso record must make no price claim (Minoa's tasting-menu figures stay with Minoa).
  expect(espresso['price range']).not.toContain('€');
  expect(espresso.description).not.toContain('€');
  await expect(page.locator('#espresso-odycy dd').nth(2)).not.toContainText('€');
  await expect(page.locator('#minoa-ax-odycy dd').nth(2)).toContainText('€70');
});

test('Kalshi market listing is presented as a listing, never as radio carriage', async ({page}) => {
  const radio = data('radio').records;
  const markets = radio.find(r=>r.id==='kalshi-trip-window-markets-api-2026-10-11');
  expect(markets).toBeTruthy();
  expect(markets.confidence).toBe('verified');
  expect(markets.source_type).toBe('official');
  expect(markets.source_url).toContain('api.elections.kalshi.com');
  // Trip-window fixtures named in the API record, and the negatives it must keep saying.
  for (const fixture of ['Everton v Chelsea','Brentford v Liverpool','Fulham v Hull City','Manchester City v Ipswich','Newcastle v Aston Villa',
    'Bournemouth v Sunderland','Brighton v Crystal Palace','Leeds v Manchester United','Nottingham Forest v Arsenal','Tottenham v Coventry']) {
    expect(markets.hours).toContain(fixture);
  }
  expect(markets.hours).toContain('LASK v Liverpool');
  expect(markets.hours).toContain('Houston v Jacksonville');
  expect(markets.hours).toContain('no Thunderpick World Championship fixture appeared');
  expect(markets.hours).toContain('no per-match Serie A market was listed');
  // No price, odds or recommendation claim is allowed in the record.
  expect(markets['price range']).toContain('Not applicable');
  for (const field of ['hours','description','notes']) {
    expect(markets[field]).not.toMatch(/\bodds\b|\d+\s?¢|cents per contract/i);
  }

  await page.setViewportSize({width:360,height:850});
  await page.goto('radio.html#kalshi-trip-window-markets');
  await expect(page.locator('#kalshi-trip-window-markets')).toContainText('What the exchange actually lists');
  await expect(page.locator('#kalshi-trip-window-markets + p')).toContainText('public API');
  const table = page.locator('#kalshi-trip-window-markets').locator('xpath=following-sibling::div[1]//tbody/tr');
  await expect(table).toHaveCount(5);
  const section = page.locator('section[aria-labelledby="kalshi-epl-title"]');
  const sectionText = await section.innerText();
  expect(sectionText).toContain('KXEPLGAME');
  expect(sectionText).toContain('KXCS2GAME');
  expect(sectionText).toContain('No Thunderpick World Championship fixture was listed');
  expect(sectionText).toContain('Nothing on this page is a price');
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBeTruthy();

  // The canonical projection of the API record renders with its own notes, and the anchor is reachable.
  await page.setViewportSize({width:1440,height:900});
  await page.goto('radio.html#kalshi-trip-window-markets-api-2026-10-11');
  await expect(page.locator('#kalshi-trip-window-markets-api-2026-10-11 h3')).toHaveText(markets.name);
  await expect(page.locator('#kalshi-trip-window-markets-api-2026-10-11 .record-notes p')).toHaveText(markets.notes);
});
