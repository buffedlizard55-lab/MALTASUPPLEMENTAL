const {defineConfig} = require('@playwright/test');
const {tmpdir} = require('os');
const {join} = require('path');
module.exports = defineConfig({
  testDir: './tests',
  globalSetup: './tests/browser-setup.js',
  fullyParallel: false,
  workers: 1,
  timeout: 60000,
  use: { baseURL: process.env.SITE_URL || 'http://127.0.0.1:8080', headless: true,
    launchOptions: {executablePath: process.env.CHROMIUM_PATH || join(tmpdir(), 'chromium'), args: ['--no-sandbox', '--disable-dev-shm-usage'], env: {...process.env, LD_LIBRARY_PATH: [join(tmpdir(),'al2023','lib'), process.env.LD_LIBRARY_PATH].filter(Boolean).join(':')}} },
  webServer: process.env.SITE_URL ? undefined : {command: 'python3 -m http.server 8080 --bind 0.0.0.0', url: 'http://127.0.0.1:8080', reuseExistingServer: true}
});
