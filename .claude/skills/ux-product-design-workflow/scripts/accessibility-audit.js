const { chromium } = require('playwright');
const { injectAxe, checkA11y, getViolations } = require('axe-playwright');

async function runAccessAudit(url = 'https://example.com') {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  try {
    await page.goto(url, { waitUntil: 'domcontentloaded' });

    await injectAxe(page);

    const violations = await getViolations(page, null, {
      detailedReport: true,
    });

    console.log("--- نتائج التدقيق الأخلاقي (Accessibility Audit) ---");
    console.log(`URL: ${url}`);
    console.log(`الانتهاكات: ${violations.length}`);
    console.dir(violations, { depth: null });
  } catch (error) {
    console.error("💥 خطأ:", error);
  } finally {
    await browser.close();
  }
}

const url = process.argv[2] || 'https://example.com';
runAccessAudit(url);
