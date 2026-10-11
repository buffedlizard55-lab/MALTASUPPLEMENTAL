// The npm-distributed headless browser avoids a separate browser CDN download.
const {default: chromium, inflate} = require('@sparticuz/chromium');
const path = require('path');
module.exports = async function () {
  await chromium.executablePath();
  await inflate(path.resolve('node_modules/@sparticuz/chromium/bin/al2023.tar.br'));
};
