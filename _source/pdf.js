const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const [,, htmlPath, pdfPath, label] = process.argv;
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.setContent(fs.readFileSync(htmlPath, 'utf8'), { waitUntil: 'load' });
  await pg.evaluate(() => document.fonts.ready);
  await pg.pdf({ path: pdfPath, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: `<div style="width:100%;font-family:'Be Vietnam Pro';font-size:7px;color:#9a8f82;padding:0 14mm;display:flex;justify-content:space-between"><span>${label}</span><span class="pageNumber"></span></div>` });
  await b.close();
})();
