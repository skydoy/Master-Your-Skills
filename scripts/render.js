// Render HTML files to PNG at 2x. Usage: node scripts/render.js in.html out.png [width] [height]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [inp, out, w = '1600', h = '900'] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(inp));
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: out, omitBackground: true });
  await b.close();
})();
