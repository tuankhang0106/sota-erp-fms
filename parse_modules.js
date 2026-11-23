const fs = require('fs');
const path = require('path');

const menus = require('./survey_output/menus_full.json');

const rootIds = [74, 117, 164, 309, 582, 168, 123, 231, 158, 178, 255, 136, 495, 297, 4];

function getMenuTree(menuId, depth = 0) {
  const item = menus[menuId];
  if (!item) return null;

  const node = {
    id: item.id,
    name: item.name,
    xmlid: item.xmlid,
    actionID: item.actionID,
    actionModel: item.actionModel,
    children: []
  };

  if (item.children && Array.isArray(item.children)) {
    for (const childId of item.children) {
      const childNode = getMenuTree(childId, depth + 1);
      if (childNode) {
        node.children.push(childNode);
      }
    }
  }

  return node;
}

const tree = rootIds.map(id => getMenuTree(id)).filter(Boolean);

fs.writeFileSync(path.join(__dirname, 'survey_output', 'parsed_module_tree.json'), JSON.stringify(tree, null, 2));

// Generate a Markdown summary
let md = "# DANH SÁCH TOÀN BỘ CÁC MODULE VÀ MENU TRONG HỆ THỐNG SOTA ERP\n\n";
md += `**Thời gian khảo sát:** ${new Date().toISOString()}\n`;
md += `**URL:** https://portalink.erp.sota-solutions.com/\n`;
md += `**Tổng số Module gốc (Apps):** ${tree.length}\n\n`;

function renderMarkdown(node, indent = "") {
  let line = `${indent}- **${node.name}** (ID: ${node.id}`;
  if (node.actionID) line += `, Action: ${node.actionID}`;
  if (node.xmlid) line += `, XML: \`${node.xmlid}\``;
  line += `)\n`;

  for (const child of node.children) {
    line += renderMarkdown(child, indent + "  ");
  }
  return line;
}

for (const app of tree) {
  md += `## 📦 Module: ${app.name}\n`;
  md += `- **ID:** ${app.id} | **Action:** ${app.actionID || 'None'} | **XML ID:** \`${app.xmlid || ''}\`\n`;
  if (app.children.length > 0) {
    md += `\n### Các Menu con (Submenus / Features):\n`;
    for (const sub of app.children) {
      md += renderMarkdown(sub, "");
    }
  } else {
    md += `*(Module đơn cấp, không có sub-menu)*\n`;
  }
  md += "\n---\n\n";
}

fs.writeFileSync(path.join(__dirname, 'survey_output', 'MODULES_SUMMARY.md'), md, 'utf-8');
console.log("Exported parsed_module_tree.json and MODULES_SUMMARY.md successfully!");
