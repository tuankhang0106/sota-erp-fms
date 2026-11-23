const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const TARGET_URL = "https://portalink.erp.sota-solutions.com/";
const USERNAME = process.env.ODOO_USER || "";
const PASSWORD = process.env.ODOO_PASS || "";

const OUTPUT_DIR = path.join(__dirname, "survey_output");
const SCREENSHOTS_DIR = path.join(OUTPUT_DIR, "screenshots");
if (!fs.existsSync(SCREENSHOTS_DIR)) {
  fs.mkdirSync(SCREENSHOTS_DIR, { recursive: true });
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

  let loadMenusData = null;
  page.on('response', async (response) => {
    try {
      const url = response.url();
      if (url.includes('/web/webclient/load_menus/')) {
        const text = await response.text();
        loadMenusData = JSON.parse(text);
        console.log("Captured load_menus data successfully!");
      }
    } catch (e) {}
  });

  console.log("Navigating to login...");
  await page.goto(TARGET_URL + "web/login", { waitUntil: 'networkidle2', timeout: 30000 });

  const userField = await page.$('input[name="login"]');
  const passField = await page.$('input[name="password"]');
  const submitBtn = await page.$('button[type="submit"]');

  await userField.type(USERNAME, { delay: 20 });
  await passField.type(PASSWORD, { delay: 20 });
  await Promise.all([
    page.waitForNavigation({ waitUntil: 'networkidle2', timeout: 30000 }),
    submitBtn.click()
  ]);

  console.log("Logged in. Waiting 3 seconds for menus to settle...");
  await new Promise(r => setTimeout(r, 3000));

  if (loadMenusData) {
    fs.writeFileSync(path.join(OUTPUT_DIR, "menus_full.json"), JSON.stringify(loadMenusData, null, 2));
    console.log("Saved menus_full.json");
  }

  // Extract root apps from page
  const apps = await page.evaluate(() => {
    // In Odoo 16/17, root apps can be found in dropdown or DOM
    const appElements = Array.from(document.querySelectorAll('.o_app, .dropdown-item.o_app, a.o_nav_entry'));
    return appElements.map(el => ({
      name: el.innerText.trim(),
      href: el.getAttribute('href') || '',
      menuId: el.getAttribute('data-menu-id') || '',
      actionId: el.getAttribute('data-action-id') || ''
    })).filter(a => a.name.length > 0);
  });

  console.log(`Found ${apps.length} apps from DOM:`, apps.map(a => a.name));

  // Let's also extract root apps from loadMenusData if available
  let rootApps = [];
  if (loadMenusData) {
    const root = loadMenusData.root || loadMenusData[loadMenusData.root] || {};
    const childrenIds = loadMenusData.children || (loadMenusData.root ? loadMenusData.root.children : []) || [];
    console.log("loadMenusData keys:", Object.keys(loadMenusData).slice(0, 10));
    
    // In Odoo, load_menus returns an object where keys are menu IDs or { "children": [...] }
    fs.writeFileSync(path.join(OUTPUT_DIR, "load_menus_sample.json"), JSON.stringify(Object.keys(loadMenusData), null, 2));
  }

  // Take screenshot of home
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "00_home.png") });

  // Navigate to key modules in read-only mode to capture UI
  // 1. Vận chuyển (Freight)
  console.log("Navigating to Vận chuyển (Freight)...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=309&action=638", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "01_freight.png") });

  // Extract freight submenus
  const freightSubmenus = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('.o_menu_sections .dropdown-toggle, .o_menu_sections .dropdown-item, .o_menu_brand, nav.o_main_navbar button, nav.o_main_navbar a')).map(e => e.innerText.trim()).filter(Boolean);
  });
  console.log("Freight submenus:", freightSubmenus);

  // 2. Kế toán (Accounting)
  console.log("Navigating to Kế toán (Accounting)...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=178&action=333", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "02_accounting.png") });

  // 3. CRM
  console.log("Navigating to CRM...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=231&action=450", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "03_crm.png") });

  // 4. Liên hệ (Contacts)
  console.log("Navigating to Liên hệ (Contacts)...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=123&action=436", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "04_contacts.png") });

  // 5. Nhân viên (Employees)
  console.log("Navigating to Nhân viên (Employees)...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=136&action=193", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "05_employees.png") });

  // 6. Chi phí (Expenses)
  console.log("Navigating to Chi phí (Expenses)...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=297&action=421", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "06_expenses.png") });

  // 7. Activity Dashboard
  console.log("Navigating to Activity Dashboard...");
  await page.goto("https://portalink.erp.sota-solutions.com/web#menu_id=164&action=257", { waitUntil: 'networkidle2', timeout: 30000 });
  await new Promise(r => setTimeout(r, 4000));
  await page.screenshot({ path: path.join(SCREENSHOTS_DIR, "07_activity_dashboard.png") });

  await browser.close();
  console.log("Done fetching module screenshots and metadata.");
})().catch(e => {
  console.error("Error:", e);
  process.exit(1);
});
