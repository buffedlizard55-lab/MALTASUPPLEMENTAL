const {test, expect} = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;
const fs = require('fs');
const pages = ['index.html','getting-around.html','restaurants.html','activities.html','everyday.html','radio.html','costs.html','sources.html'];
const topics = {'getting-around.html':'transport','restaurants.html':'food','activities.html':'activities','everyday.html':'everyday','radio.html':'radio'};
const data = topic => JSON.parse(fs.readFileSync(`data/${topic}.json`));

for (const width of [360, 768, 1440]) {
  test(`all pages render, fit and pass axe at ${width}px`, async ({page}) => {
    await page.setViewportSize({width, height:900});
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    for (const url of pages) {
      await page.goto(url);
      await expect(page.locator('.brand')).toBeVisible();
      await expect(page.locator('h1')).toHaveCount(1);
      if (topics[url]) await expect(page.locator('.record-card')).toHaveCount(data(topics[url]).records.length);
      if (url === 'costs.html') await expect(page.locator('[data-expense-row]')).toHaveCount(25);
      if (url === 'index.html') await expect(page.locator('[data-overview] .card')).toHaveCount(4);
      if (url === 'sources.html') await expect(page.locator('[data-document] .document-text')).toHaveCount(2);
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1), url).toBeTruthy();
      const audit = await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
      expect(audit.violations, `${url}: ${audit.violations.map(v=>v.id).join(',')}`).toEqual([]);
    }
    expect(errors).toEqual([]);
  });
}

test('topic cards match every canonical field and filters combine/reset', async ({page}) => {
  for (const [url,topic] of Object.entries(topics)) {
    const records = data(topic).records;
    await page.goto(url);
    await expect(page.locator('.record-card')).toHaveCount(records.length);
    for (const r of records) {
      const card = page.locator(`[id="${r.id}"]`);
      await expect(card.locator('h3')).toHaveText(r.name);
      await expect(card.locator('p').first()).toHaveText(r.description);
      await expect(card.locator('dd').nth(1)).toHaveText(r.hours);
      await expect(card.locator('dd').nth(2)).toHaveText(r['price range']);
      await expect(card.locator('a.record-source').first()).toHaveAttribute('href',r.source_url);
      await expect(card.locator('.record-source-meta')).toContainText(r.date_checked);
    }
    const first = records[0];
    await page.locator('[data-confidence-filter]').selectOption(first.confidence);
    await page.locator('[data-area-filter]').selectOption(first.area);
    await page.locator('[data-topic-tools] select').first().selectOption(first.category);
    await expect(page.locator('.record-card')).toHaveCount(records.filter(r => r.area === first.area && r.confidence===first.confidence && r.category===first.category).length);
    await page.locator('input[type=search]').fill('NO_SUCH_ITEM_987');
    await expect(page.locator('.empty-state')).toBeVisible();
    await page.getByRole('button',{name:'Reset filters'}).click();
    await expect(page.locator('.record-card')).toHaveCount(records.length);
    await page.locator(`#${first.id} summary`).click();
    await expect(page.locator(`#${first.id} .record-notes p`)).toHaveText(first.notes);
  }
});

test('mobile navigation, skip link and canonical deep link', async ({page}) => {
  await page.setViewportSize({width:360,height:800});
  await page.goto('index.html');
  const toggle = page.locator('.nav-toggle');
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-expanded','true');
  await expect(page.getByRole('navigation').getByRole('link')).toHaveCount(8);
  await page.getByRole('navigation').getByRole('link',{name:'Sports radio',exact:true}).click();
  await expect(page).toHaveURL(/radio.html$/);
  await expect(page.locator('#main-navigation [aria-current=page]')).toHaveText('Sports radio');
  await page.goto('activities.html#in-guardia-2026-10-18');
  await expect(page.locator('#in-guardia-2026-10-18')).toBeInViewport();
  await page.goto('index.html');
  await page.keyboard.press('Tab');
  await expect(page.getByRole('link',{name:'Skip to main content'})).toBeFocused();
});

test('planner defaults, exact price status, totals, autosave and daily rows', async ({page}) => {
  await page.goto('costs.html');
  await expect(page.locator('[data-expense-row]')).toHaveCount(25);
  for (const r of data('expenses').records) {
    await expect(page.locator(`[data-expense-row="${r.id}"] dd`)).toHaveText(r['price range']);
  }
  expect(await page.locator('[data-expense-field]').evaluateAll(inputs => inputs.every(i=>i.value===''))).toBeTruthy();
  await page.locator('#expense-flights-budget').fill('100.25');
  await page.locator('#expense-flights-actual').fill('120.50');
  await expect(page.locator('#budget-total')).toHaveText('€100.25');
  await expect(page.locator('#difference-total')).toHaveText('+€20.25');
  await page.locator('.daily-planner summary').click();
  await page.locator('#expense-daily-2026-10-13-actual').fill('7.50');
  await expect(page.locator('#actual-total')).toHaveText('€128.00');
  await page.reload();
  await expect(page.locator('#expense-flights-budget')).toHaveValue('100.25');
  await expect(page.locator('#actual-total')).toHaveText('€128.00');
  await page.getByRole('button',{name:'Clear saved entries'}).click(); // default dismiss: must retain data
  await expect(page.locator('#expense-flights-budget')).toHaveValue('100.25');
  page.once('dialog', d=>d.accept());
  await page.getByRole('button',{name:'Clear saved entries'}).click();
  await expect(page.locator('#actual-total')).toHaveText('€0.00');
  await page.reload();
  await expect(page.locator('#expense-flights-budget')).toHaveValue('');
});

test('CSV download preserves quotes/newlines and neutralizes formula prefixes', async ({page}) => {
  await page.goto('costs.html');
  await page.locator('#expense-flights-budget').fill('5');
  await page.locator('#expense-flights-note').fill(' \t=SUM(1,2)');
  await page.locator('#expense-hotel-stay-note').fill('Receipt "A", paid');
  const dl = page.waitForEvent('download');
  await page.getByRole('button',{name:'Download CSV backup'}).click();
  const download = await dl;
  expect(download.suggestedFilename()).toBe('malta-expenses-2026-10-13-to-19.csv');
  const csv = fs.readFileSync(await download.path(),'utf8');
  expect(csv.charCodeAt(0)).toBe(0xfeff);
  expect(csv).toContain(`"' \t=SUM(1,2)"`);
  expect(csv).toContain('"Receipt ""A"", paid"');
  expect(csv).toContain('13 October · optional daily spending');
  expect(csv.split('\r\n')).toHaveLength(26);
});

test('planner handles invalid input, corrupt storage and storage denial', async ({browser}) => {
  for (const storageCase of ['corrupt','denied']) {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.addInitScript(caseName => {
      if (caseName === 'corrupt') localStorage.setItem('malta-trip-2026-10-13-19-expenses-v1','bad json');
      else Object.defineProperty(window, 'localStorage', {get(){throw new Error('denied')}});
    }, storageCase);
    await page.goto('costs.html');
    await expect(page.locator('[data-expense-row]')).toHaveCount(25);
    await page.locator('#expense-flights-budget').fill('20');
    await expect(page.locator('#budget-total')).toHaveText('€20.00');
    if (storageCase === 'denied') await expect(page.locator('#save-status')).toContainText('unavailable');
    await page.locator('#expense-flights-budget').fill('-1');
    await expect(page.locator('#budget-total')).toHaveText('€0.00');
    await expect(page.locator('#save-status')).toContainText('non-negative');
    await page.locator('#expense-flights-budget').fill('1.234');
    await expect(page.locator('#budget-total')).toHaveText('€0.00');
    await context.close();
  }
});

test('failed data fetch is visible and cannot export an empty planner', async ({page}) => {
  await page.route('**/data/*.json', route=>route.fulfill({status:503,body:'unavailable'}));
  await page.goto('costs.html');
  await expect(page.locator('#expense-list')).toContainText('could not be loaded');
  await expect(page.locator('#export-csv')).toBeDisabled();
  await page.goto('radio.html');
  await expect(page.locator('[data-topic-data]')).toContainText('could not be loaded');
});
