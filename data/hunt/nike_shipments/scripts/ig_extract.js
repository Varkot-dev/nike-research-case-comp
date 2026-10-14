// Extract window.__NUXT__ state from saved ImportGenius HTML pages (data-only IIFE) in a sandboxed vm with timeout.
// Usage: node ig_extract.js out.json file1.html file2.html ...
const fs = require('fs'), vm = require('vm'), path = require('path');
const out = {};
for (const f of process.argv.slice(3)) {
  const t = fs.readFileSync(f, 'utf8');
  const m = t.match(/<script>(window\.__NUXT__=[\s\S]*?)<\/script>/);
  if (!m) { out[path.basename(f)] = null; continue; }
  const ctx = { window: {} };
  try { vm.runInNewContext(m[1], ctx, { timeout: 2000 }); } catch (e) { out[path.basename(f)] = { error: String(e) }; continue; }
  const p = ctx.window.__NUXT__.state.profile;
  out[path.basename(f)] = {
    company: p.company, traderType: p.traderType, totalShipments: p.totalShipments, country: p.country,
    datapoints: p.datapoints, ports: p.ports, consignees: p.consignees, shippers: p.shippers,
    shipments: (p.shipments && p.shipments[0]) ? p.shipments[0].shipments : [],
    detailNotify: p.shipmentDetails ? p.shipmentDetails.NotifyParty : null,
    detailNotifyAddr: p.shipmentDetails ? p.shipmentDetails.NotifyPartyAddress : null,
  };
}
fs.writeFileSync(process.argv[2], JSON.stringify(out, null, 1));
