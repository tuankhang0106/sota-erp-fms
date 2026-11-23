const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const TARGET_URL = "https://portalink.erp.sota-solutions.com/";
const USERNAME = process.env.ODOO_USER || "";
const PASSWORD = process.env.ODOO_PASS || "";

const OUTPUT_DIR = path.join(__dirname, "survey_output");
if (!fs.existsSync(OUTPUT_DIR)) {
  fs.mkdirSync(OUTPUT_DIR, { recursive: true });
}

(async () => {
  console.log("Launching Chrome...");
  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: "new",
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--ignore-certificate-errors', '--window-size=1920,1080']
  });

  const page = await browser.newPage();
  await page.setViewport({ width: 1920, height: 1080 });

  const apiLogs = [];
  page.on('response', async (response) => {
    try {
      const req = response.request();
      const url = response.url();
      const status = response.status();
      const method = req.method();
      
      // Log API or interesting requests
      if (!url.match(/\.(png|jpg|jpeg|svg|css|woff2?|ico)($|\?)/i)) {
        let responseBody = null;
        try {
          const ct = response.headers()['content-type'] || '';
          if (ct.includes('application/json') || ct.includes('text/plain')) {
            responseBody = await response.text();
          }
        } catch (e) {}

        apiLogs.push({
          url,
          method,
          status,
          responseBody: responseBody ? responseBody.substring(0, 500) : null
        });
      }
    } catch (err) {}
  });

  console.log("Navigating to: " + TARGET_URL);
  await page.goto(TARGET_URL, { waitUntil: 'networkidle2', timeout: 30000 });

  await page.screenshot({ path: path.join(OUTPUT_DIR, "01_login_page.png") });
  console.log("Saved 01_login_page.png");

  // Inspect page content and form elements
  const pageTitle = await page.title();
  console.log("Page title: " + pageTitle);
  const currentUrl = page.url();
  console.log("Current URL: " + currentUrl);

  const inputs = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('input')).map(i => ({
      name: i.name,
      type: i.type,
      id: i.id,
      placeholder: i.placeholder,
      className: i.className
    }));
  });
  console.log("Found inputs:", JSON.stringify(inputs, null, 2));

  // Find email/username field and password field
  const usernameSelector = 'input[type="text"], input[type="email"], input[name*="user"], input[name*="email"], input[id*="user"], input[id*="email"]';
  const passwordSelector = 'input[type="password"]';

  const userField = await page.$(usernameSelector);
  const passField = await page.$(passwordSelector);

  if (userField && passField) {
    console.log("Filling credentials...");
    await userField.click();
    await userField.type(USERNAME, { delay: 30 });
    await passField.click();
    await passField.type(PASSWORD, { delay: 30 });

    await page.screenshot({ path: path.join(OUTPUT_DIR, "02_filled_credentials.png") });

    // Look for submit button
    const submitBtn = await page.$('button[type="submit"], input[type="submit"], button.ant-btn-primary, button');
    if (submitBtn) {
      console.log("Submitting login form...");
      await Promise.all([
        page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 30000 }).catch(e => console.log("Navigation timeout or SPA: " + e.message)),
        submitBtn.click()
      ]);
    } else {
      console.log("Pressing Enter to login...");
      await Promise.all([
        page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 30000 }).catch(e => console.log("Navigation timeout or SPA: " + e.message)),
        page.keyboard.press('Enter')
      ]);
    }

    // Wait a few seconds for SPA render
    await new Promise(r => setTimeout(r, 5000));

    const postLoginUrl = page.url();
    console.log("Post-login URL: " + postLoginUrl);
    await page.screenshot({ path: path.join(OUTPUT_DIR, "03_post_login.png") });
    console.log("Saved 03_post_login.png");

    // Extract HTML & navigation menus
    const navStructure = await page.evaluate(() => {
      // Look for menu items, links, sidebars
      const links = Array.from(document.querySelectorAll('a')).map(a => ({
        text: a.innerText.trim(),
        href: a.href,
        className: a.className
      })).filter(l => l.text.length > 0 && !l.href.startsWith('javascript'));

      const menuItems = Array.from(document.querySelectorAll('[role="menuitem"], .ant-menu-item, .menu-item, nav a, .sidebar a, ul.ant-menu li')).map(el => ({
        text: el.innerText.trim(),
        className: el.className
      }));

      return {
        title: document.title,
        bodyTextSnippet: document.body.innerText.substring(0, 1000),
        links,
        menuItems
      };
    });

    fs.writeFileSync(path.join(OUTPUT_DIR, "nav_structure.json"), JSON.stringify(navStructure, null, 2));
    fs.writeFileSync(path.join(OUTPUT_DIR, "api_logs.json"), JSON.stringify(apiLogs, null, 2));
    console.log("Extracted navigation and APIs successfully.");
  } else {
    console.log("Could not find input fields!");
  }

  await browser.close();
  console.log("Survey script completed.");
})().catch(err => {
  console.error("Error occurred:", err);
  process.exit(1);
});
