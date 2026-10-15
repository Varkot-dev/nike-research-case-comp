// Builds "Nike Short Thesis.pptx": an editable investment-banking style deck.
// Run: node build_deck.js   (then it applies the theme and writes the file)
const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/d0bcab90-6d1a-4318-8329-9d3986c95703_f8e9643a-c32e-4a7c-bbb1-d14f914bb75a/pptx/scripts/apply_theme.js");

const OUT = "Nike Short Thesis.pptx";

// ---- palette (hex, no #) ----
const NAVY = "0B2A4A";
const INK = "1F2933";
const SLATE = "5B7083";
const LSLATE = "9FB0C0";
const RULE = "C9CED6";
const PANEL = "EEF1F5";
const RED = "A4262C";
const GREEN = "2F6B4F";
const GREY = "6B7280";
const WHITE = "FFFFFF";
const FONT = "Arial";

const THEME = {
  name: "Nike Short Thesis",
  headFontFace: FONT,
  bodyFontFace: FONT,
  colors: {
    dk1: INK, lt1: WHITE, dk2: NAVY, lt2: PANEL,
    accent1: NAVY, accent2: RED, accent3: SLATE, accent4: LSLATE, accent5: GREEN, accent6: RULE,
    hlink: "1F4E79", folHlink: SLATE,
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
pres.title = "Nike, Inc. (NKE): Short thesis";
pres.author = "Team draft";

const FOOT = "Nike, Inc. (NYSE: NKE)  |  Short thesis  |  Team draft, October 14, 2026";

pres.defineSlideMaster({
  title: "COVER",
  background: { color: NAVY },
  objects: [],
});
pres.defineSlideMaster({
  title: "CONTENT",
  background: { color: WHITE },
  objects: [
    { text: { text: FOOT, options: { x: 0.6, y: 7.02, w: 9.5, h: 0.3, fontFace: FONT, fontSize: 10, color: GREY, margin: 0 } } },
    {
      placeholder: {
        options: { name: "title", type: "title", x: 0.6, y: 0.38, w: 12.13, h: 1.0, fontFace: FONT, fontSize: 24, bold: true, color: NAVY, valign: "top", align: "left", margin: 0 },
        text: "",
      },
    },
  ],
  slideNumber: { x: 12.0, y: 7.02, w: 0.73, h: 0.3, fontFace: FONT, fontSize: 10, color: GREY, align: "right" },
});

// ---- helpers ----
const hdr = (t, align) => ({ text: t, options: { bold: true, color: WHITE, fill: { color: NAVY }, fontFace: FONT, fontSize: 12, align: align || "left", valign: "middle" } });
const BORDER = [{ type: "none" }, { type: "none" }, { type: "solid", pt: 0.5, color: RULE }, { type: "none" }];
const cell = (t, o) => ({ text: t, options: Object.assign({ fontFace: FONT, fontSize: 12, color: INK, valign: "middle", border: BORDER }, o || {}) });
const source = (slide, txt) => slide.addText(txt, { x: 0.6, y: 6.42, w: 12.13, h: 0.55, fontFace: FONT, fontSize: 10, color: GREY, valign: "bottom", margin: 0, isTextBox: true, objectName: "Source" });
const label = (slide, txt, x, y, w) => slide.addText(txt, { x, y, w, h: 0.32, fontFace: FONT, fontSize: 12, bold: true, color: NAVY, margin: 0, isTextBox: true });
const content = (section, title, notes) => {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  return s;
};
const chartBase = {
  catAxisLabelFontFace: "+mn-lt", valAxisLabelFontFace: "+mn-lt", dataLabelFontFace: "+mn-lt", titleFontFace: "+mn-lt", legendFontFace: "+mn-lt",
  catAxisLabelFontSize: 12, catAxisLabelColor: INK, valAxisLabelFontSize: 11, valAxisLabelColor: GREY,
  dataLabelFontSize: 12, dataLabelColor: INK, dataLabelFontBold: true, showValue: true, showLegend: false,
  valGridLine: { style: "none" }, catGridLine: { style: "none" }, valAxisHidden: true,
  showTitle: true, titleFontSize: 13, titleColor: NAVY,
};

// =============== 1. COVER ===============
pres.addSection({ title: "Recommendation" });
{
  const s = pres.addSlide({ masterName: "COVER", sectionTitle: "Recommendation" });
  s.addText("Nike, Inc. (NYSE: NKE)", { x: 0.9, y: 0.9, w: 8, h: 0.4, fontFace: FONT, fontSize: 16, color: LSLATE, margin: 0, isTextBox: true });
  s.addText("Equity research case competition  |  Team draft", { x: 0.9, y: 1.3, w: 9, h: 0.4, fontFace: FONT, fontSize: 14, color: LSLATE, margin: 0, isTextBox: true });
  s.addText("Recommendation: SHORT", { x: 0.9, y: 2.6, w: 9, h: 0.5, fontFace: FONT, fontSize: 20, bold: true, color: "E8735F", margin: 0, isTextBox: true });
  s.addText("Today's price needs an operating margin Nike has not earned since FY24. Volume has not grown in seven years, and price is now falling.", { x: 0.9, y: 3.2, w: 10.6, h: 1.6, fontFace: FONT, fontSize: 36, bold: true, color: WHITE, margin: 0, valign: "top", isTextBox: true });
  const stats = [["$35.35", "Share price, Oct 12, 2026"], ["21.5x", "P/E on FY28E (peer median 13.2x)"], ["$1.65", "FY28E consensus EPS"], ["Nov 16 to 17", "Investor Day"]];
  stats.forEach((st, i) => {
    const x = 0.9 + i * 3.05;
    s.addText(st[0], { x, y: 5.55, w: 2.9, h: 0.55, fontFace: FONT, fontSize: 26, bold: true, color: WHITE, margin: 0, isTextBox: true });
    s.addText(st[1], { x, y: 6.1, w: 2.8, h: 0.5, fontFace: FONT, fontSize: 12, color: LSLATE, margin: 0, valign: "top", isTextBox: true });
  });
  s.addNotes("Short means we expect the share price to fall, or to do worse than peers. The pitch is deliberately narrow: FY28 expectations are too high. We do not rely on a near-term earnings miss, because Nike landed inside or above its guided range on revenue and gross margin 16 of 16 times in the last eight quarters, but Q1 FY27 revenue (-4.3% against a midpoint of about -3.5%) was the first to fall below the midpoint. Peer multiples are one pull from Yahoo Finance at the Oct 13 close and should be refreshed around Oct 30.");
}

// =============== 2. EXECUTIVE SUMMARY ===============
{
  const s = content("Recommendation", "We recommend a short: the price needs a margin recovery that volume, price and share data do not support",
    "Four points. 1) FY28 consensus needs a margin gain Nike has not delivered in any recent year. 2) The decline is not only Nike-specific, but Nike is losing share in markets that are still growing, with China the clearest case. 3) The repair timetable keeps slipping. 4) We state the risks openly: running is real, tariffs are lower than Nike planned, and the short is crowded but not a squeeze setup.");
  const pts = [
    ["The price needs a margin Nike has not earned since FY24. ", "A reverse DCF at a 9% to 10% required return needs a long-run operating margin of 11% to 14%; peer parity on P/E needs about 11.6%. Consensus has 7.2% in FY28; FY26 was 8.3% (6.2% without the tariff refund). On sales and EBITDA Nike already trades at the peer median, so the premium is only a margin bet."],
    ["Volume has not grown in seven years; price did the work and is now falling. ", "Nike footwear units are flat versus FY19 while revenue per pair is up 22%. Since FY23 units are down 10.7%, and price turned negative in FY25 (-3 points), FY26 (-1) and Q1 FY27 (-1, with units -5%). All figures from Nike's own 10-K unit and ASP disclosures."],
    ["Share loss where markets still grow. ", "Nike's two largest China partners closed 26% of doors in three years; Nike trails the European peer median by 14 to 18 points for eight quarters; nike.com visits fell 11% in August while adidas.com rose 12.5% and DICK'S rose 15%, so the digital decline is lost demand, not only a deliberate cut."],
    ["What we do not claim, and the risks. ", "No single smoking gun: 12 forensic hunts found none. The FY28 EPS gap on filing facts alone is $0.09 to $0.19; the larger gap depends on the margin step not happening. Running volume is real, 2026 trademark filings are at a 15-year high, and Nike landed inside its guided range 16 of 16 times."],
  ];
  const runs = [];
  pts.forEach((p, i) => {
    runs.push({ text: p[0], options: { bold: true, color: NAVY, fontSize: 13 } });
    runs.push({ text: p[1], options: { color: INK, fontSize: 13, breakLine: i < pts.length - 1, paraSpaceAfter: 12 } });
  });
  s.addText(runs, { x: 0.6, y: 1.65, w: 7.4, h: 4.6, fontFace: FONT, valign: "top", margin: 0, isTextBox: true, objectName: "Key points" });
  label(s, "Key data", 8.45, 1.65, 4.2);
  const rows = [
    [hdr("Metric"), hdr("Value", "right")],
    [cell("Share price (Oct 12, 2026)"), cell("$35.35", { align: "right", bold: true })],
    [cell("Market capitalization"), cell("about $52.5B", { align: "right" })],
    [cell("P/E, FY27E"), cell("27.4x", { align: "right" })],
    [cell("P/E, FY28E (peer median 13.2x)"), cell("21.5x", { align: "right", bold: true, color: RED })],
    [cell("FY27 guide, adjusted EPS"), cell("$1.15 to $1.35", { align: "right" })],
    [cell("FY28E consensus EPS"), cell("$1.65", { align: "right" })],
    [cell("Short interest, % of tradable shares"), cell("8.2%", { align: "right" })],
  ];
  s.addTable(rows, { x: 8.45, y: 2.05, w: 4.28, colW: [2.78, 1.5], rowH: 0.42, fontFace: FONT, fontSize: 12 });
  source(s, "Sources: Nike FY26 10-K, Q1 FY27 10-Q, Q1 FY27 earnings release and call (Oct 1, 2026); Yahoo Finance (Oct 13, 2026 close); FINRA (Sep 30, 2026); BEA PCE footwear; team analysis.");
}

// =============== 3. SCOREBOARD ===============
{
  const s = content("Recommendation", "Five of eight tests lean short and none leans long; China is the only strong grade",
    "This is the evidence summary after independent checkers re-pulled samples and re-ran the tests. Several early findings were downgraded (see the appendix). Strength grades are the post-checker grades. Running is graded neutral because volume is real but price health is mixed.");
  const dir = (d) => cell(d, { bold: true, align: "center", color: d.startsWith("Short") ? RED : SLATE });
  const rows = [
    [hdr("Question"), hdr("What the data shows"), hdr("Direction", "center"), hdr("Strength", "center")],
    [cell("Has China found a floor?", { bold: true }), cell("Nike guides worse than -26%; partners closing doors faster than ANTA, Li-Ning, Xtep adult; peer-set share 65% (2022) to 50% (H1 2026)"), dir("Short"), cell("Strong", { align: "center", bold: true })],
    [cell("Is North America demand growing?", { bold: true }), cell("Consumer demand not growing; channel fill cannot be proven (units at or above real spending)"), dir("Short"), cell("Moderate", { align: "center" })],
    [cell("Are factory orders turning?", { bold: true }), cell("Feng Tay about -6% a month on a two-year basis, no turn"), dir("Short"), cell("Moderate", { align: "center" })],
    [cell("Is discounting improving?", { bold: true }), cell("nike.com 30.5% to 31.0% of pages discounted; not clearly worse than rivals"), dir("Short"), cell("Moderate", { align: "center" })],
    [cell("Are lifestyle classics near a bottom?", { bold: true }), cell("Dunk and Air Force 1 at a price floor; Jordan retro is not (AJ1 High resale -22% in USD)"), dir("Short"), cell("Moderate", { align: "center" })],
    [cell("Is running real or discount-driven?", { bold: true }), cell("Volume real (Dick's reviews +49% vs Hoka +22%); Pegasus 42 marked down"), dir("Neutral"), cell("Moderate", { align: "center" })],
    [cell("Are expectations too high?", { bold: true }), cell("Q2 and FY27 match evidence; FY28 EPS looks high; tariff relief offsets part"), dir("Neutral (decider)"), cell("Moderate", { align: "center" })],
    [cell("Do similar setups bottom?", { bold: true }), cell("Coin flip; short interest, fund exits and insider buying did not predict returns"), dir("Neutral"), cell("Moderate", { align: "center" })],
  ];
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.13, colW: [3.1, 6.33, 1.6, 1.1], rowH: [0.38, 0.56, 0.56, 0.5, 0.5, 0.56, 0.56, 0.56, 0.56], fontFace: FONT, fontSize: 12 });
  source(s, "Sources: team scoreboard after checker review (research_notes/Long or short cruxes/00_SCOREBOARD.md): Nike filings and calls; HKEX filings (Topsports, Pou Sheng, ANTA, Li-Ning, Xtep); Taiwan MOPS; Common Crawl nike.com panel; SNKRDUNK; BEA.");
}

// =============== 4. SITUATION ===============
pres.addSection({ title: "Fundamentals and valuation" });
{
  const s = content("Fundamentals and valuation", "Sales are down 10% from FY24 and operating margin has fallen about four points; FY27 is guided lower again",
    "Revenue: FY24 $51,362M, FY25 $46,309M (sum of quarters), FY26 $46,398M. FY27E is the midpoint of a high-single-digit decline read as -7% to -9% (about $42.2B to $43.2B); Nike did not say whether the guide is reported or currency-neutral. Operating (EBIT) margin: FY24 12.7%, FY25 8.2%, FY26 8.3%. FY27E and FY28E margins are consensus (5.7% and 7.2%). FY26 EPS of $2.10 includes a one-time $0.52 tariff refund; adjusted $1.58.");
  s.addChart(pres.charts.BAR, [{ name: "Revenue ($B)", labels: ["FY24", "FY25", "FY26", "FY27E (guide mid)"], values: [51.4, 46.3, 46.4, 42.7] }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 5.95, h: 3.9, barDir: "col", barGapWidthPct: 60, chartColors: [NAVY, NAVY, NAVY, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '"$"0.0"B"', title: "Revenue ($B)", valAxisMinVal: 0, valAxisMaxVal: 60,
  }));
  s.addChart(pres.charts.BAR, [{ name: "Operating margin (%)", labels: ["FY24", "FY25", "FY26", "FY27E", "FY28E"], values: [12.7, 8.2, 8.3, 5.7, 7.2] }], Object.assign({}, chartBase, {
    x: 6.8, y: 1.65, w: 5.93, h: 3.9, barDir: "col", barGapWidthPct: 60, chartColors: [NAVY, NAVY, NAVY, LSLATE, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '0.0"%"', title: "Operating (EBIT) margin (%), consensus for FY27E and FY28E", valAxisMinVal: 0, valAxisMaxVal: 16,
  }));
  s.addText("FY26 reported EPS of $2.10 includes a one-time $0.52 tariff refund (adjusted $1.58). FY27 guide: adjusted EPS $1.15 to $1.35.", { x: 0.6, y: 5.65, w: 12.13, h: 0.5, fontFace: FONT, fontSize: 13, color: INK, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: Nike FY24 10-K p.57, FY26 10-K p.55, Q1 FY27 release. FY25 revenue is the sum of reported quarters. FY27E revenue is the midpoint of a guide read as -7% to -9%. FY27E and FY28E margins are consensus (repo notes, Oct 13, 2026).");
}

// =============== 5. VALUATION ===============
{
  const s = content("Fundamentals and valuation", "Nike trades at a 63% premium to peers on FY28 earnings, but at the peer median on sales and cash profit",
    "27.4x means investors pay $27.40 for $1 of expected FY27 earnings. Nine peers: adidas, Puma, Deckers, On, Lululemon, Under Armour, ASICS, Anta, VF. Puma at 88x on FY28 is not meaningful and is excluded from the chart (it is included in the median calculation as reported). The premium is +41% against six footwear-led peers, +81% without Puma and Under Armour, and +10% against the fast growers On and ASICS. EV multiples are from the Oct 12 table and were not refreshed. Refresh from one source near Oct 30.");
  const labels = ["Under Armour", "ASICS", "Nike", "On", "adidas", "VF Corp", "Lululemon", "Anta", "Deckers"];
  const vals = [25.3, 21.8, 21.5, 17.3, 13.2, 11.9, 10.9, 10.9, 10.0];
  s.addChart(pres.charts.BAR, [{ name: "P/E FY28E", labels, values: vals }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 7.0, h: 4.6, barDir: "col", barGapWidthPct: 40, chartColors: [LSLATE, LSLATE, RED, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '0.0"x"', title: "Price to FY28E earnings (x); Puma (88x) not meaningful and not shown", valAxisMinVal: 0, valAxisMaxVal: 30, catAxisLabelFontSize: 11,
  }));
  label(s, "Nike vs peer median (nine peers)", 8.0, 1.75, 4.7);
  const rows = [
    [hdr("Multiple"), hdr("Nike", "right"), hdr("Peer median", "right")],
    [cell("P/E, FY27E"), cell("27.4x", { align: "right", bold: true }), cell("15.8x", { align: "right" })],
    [cell("P/E, FY28E"), cell("21.5x", { align: "right", bold: true, color: RED }), cell("13.2x", { align: "right" })],
    [cell("EV / Sales"), cell("1.20x", { align: "right" }), cell("1.18x", { align: "right" })],
    [cell("EV / EBITDA"), cell("11.3x", { align: "right" }), cell("11.6x", { align: "right" })],
  ];
  s.addTable(rows, { x: 8.0, y: 2.15, w: 4.73, colW: [2.0, 1.2, 1.53], rowH: 0.42, fontFace: FONT, fontSize: 12 });
  s.addText("On sales and cash profit Nike already trades like an average peer. The whole premium is a bet that its profit margin comes back.", { x: 8.0, y: 4.5, w: 4.73, h: 1.4, fontFace: FONT, fontSize: 14, color: INK, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: Yahoo Finance forward P/E, one pull at the Oct 13, 2026 close; EV/Sales and EV/EBITDA from the Oct 12, 2026 peer table (not refreshed). Peers: adidas, Puma, Deckers, On, Lululemon, Under Armour, ASICS, Anta, VF.");
}

// =============== 6. WHAT THE PRICE NEEDS ===============
{
  const s = content("Fundamentals and valuation", "To justify today's price, long-run margin must return to roughly 11% to 14%; consensus has 7.2% in FY28",
    "A reverse DCF starts from today's price and asks what long-run margin the market must assume. WACC is the yearly return investors demand; a higher WACC needs a higher margin. We show 8%, 9% and 10% because 9% and 10% both come from standard equity risk premium choices (Damodaran and Kroll). This is not a price target and no model is built yet. The 10-year average of 11.8% is our arithmetic on reported margins. Scoreboard caution: this supports 'FY28 and beyond is priced for a rebound', not 'the price assumes FY24 margins outright'.");
  s.addChart(pres.charts.BAR, [{ name: "Operating margin", labels: ["FY28E consensus", "FY26 actual", "10-year average", "FY24 actual"], values: [7.2, 8.3, 11.8, 12.7] }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 6.2, h: 4.5, barDir: "col", barGapWidthPct: 60, chartColors: [LSLATE, LSLATE, NAVY, NAVY],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '0.0"%"', title: "Operating (EBIT) margin (%)", valAxisMinVal: 0, valAxisMaxVal: 16,
  }));
  label(s, "Margin the price requires (long-run operating margin)", 7.2, 1.75, 5.5);
  const rows = [
    [hdr("Required return (WACC)"), hdr("Required margin", "right")],
    [cell("8%"), cell("9.4% to 10.3%", { align: "right" })],
    [cell("9%"), cell("11.4% to 12.2%", { align: "right", bold: true })],
    [cell("10%"), cell("13.4% to 14.1%", { align: "right", bold: true })],
  ];
  s.addTable(rows, { x: 7.2, y: 2.15, w: 5.53, colW: [2.9, 2.63], rowH: 0.42, fontFace: FONT, fontSize: 12 });
  s.addText([
    { text: "Even at 9%, the price needs about the 10-year average margin, 3.5 points above today, on FY28E revenue of about $43.6B versus $51.4B in FY24.", options: { breakLine: true, paraSpaceAfter: 10 } },
    { text: "At $35.35 and 3% sales growth, a buyer earns about 9.0% a year only if margins settle at the 10-year average; at today's 8.3% it is about 7.2%.", options: {} },
  ], { x: 7.2, y: 4.1, w: 5.53, h: 2.1, fontFace: FONT, fontSize: 13, color: INK, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: reverse DCF grid (22.5% tax, 3% revenue CAGR FY28 to FY36; range across growth assumptions), replicated cell by cell in repo; Nike FY24 and FY26 10-Ks; consensus (Oct 13, 2026). 10-year average is team arithmetic. Not a price target.");
}

// =============== 7. FY28 EPS ===============
{
  const s = content("Fundamentals and valuation", "Consensus FY28 EPS of $1.65 needs margin gains Nike has not delivered, and management will not discuss FY28",
    "FY28 bridge (D1, labelled arithmetic from the FY27 guide midpoint): consensus EBIT rises about $700M, of which volume on consensus revenue explains about $200M; the other roughly $500M (114 bp) must come from gross margin and cost, which needs Pace savings to drop through in full plus about 30 bp of gross margin. The gap to consensus that rests on filing facts alone is $0.09 to $0.19 before the tariff offset; the base case of $1.17 (-$0.48) depends on the judgment that the margin step does not happen, so we do not present it as fact. Nike's best one-year margin gain between FY22 and FY26 was 60 bp. FY28 consensus was $2.22 thirty days earlier (Yahoo earningsTrend), so it has already been cut by 26%; with 24 cuts in 7 days, more cuts look likely, but that is our view. Quotes are from the Q1 FY27 call on Oct 1, 2026.");
  s.addChart(pres.charts.BAR, [{ name: "EPS ($)", labels: ["FY26 adjusted (ex tariff refund)", "FY27E guide midpoint", "FY28E consensus, today", "FY28E consensus, 30 days ago"], values: [1.58, 1.25, 1.65, 2.22] }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 6.6, h: 4.5, barDir: "col", barGapWidthPct: 50, chartColors: [NAVY, NAVY, RED, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '"$"0.00', title: "Diluted EPS ($)", valAxisMinVal: 0, valAxisMaxVal: 2.6, catAxisLabelFontSize: 11,
  }));
  label(s, "What management said (Q1 FY27 call, Oct 1, 2026)", 7.6, 1.75, 5.1);
  const q = [
    ["\"...probably bleed in a little bit into fiscal '28 as well.\"", "CFO Dave Denton, p.24"],
    ["Pace savings mostly \"realized in fiscal years '29 and '30\".", "CFO Dave Denton, p.10"],
    ["On FY28 revenue: \"why don't we hold that question, we'll come back to it at Investor Day.\"", "CFO Dave Denton, p.25"],
  ];
  const runs = [];
  q.forEach((x, i) => {
    runs.push({ text: x[0], options: { italic: true, color: INK, fontSize: 13, breakLine: true } });
    runs.push({ text: x[1], options: { color: GREY, fontSize: 11, breakLine: i < q.length - 1, paraSpaceAfter: 12 } });
  });
  s.addText(runs, { x: 7.6, y: 2.15, w: 5.13, h: 3.0, fontFace: FONT, margin: 0, valign: "top", isTextBox: true });
  s.addText("Consensus needs about $700M more EBIT in FY28. Volume explains about $200M. The other $500M (114 bp) must come from margin and cost, and Nike's best one-year gain since FY22 was 60 bp.", { x: 7.6, y: 4.55, w: 5.13, h: 0.9, fontFace: FONT, fontSize: 15, bold: true, color: NAVY, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: Nike Q1 FY27 call transcript (Oct 1, 2026); Q1 FY27 release; Yahoo Finance earningsTrend (Oct 14, 2026). Margin arithmetic is team analysis on reported and consensus figures; FY28 revenue assumed about flat.");
}

// =============== 8. GUIDE IMPLIED ===============
pres.addSection({ title: "Evidence" });
{
  const s = content("Evidence", "Nike's full-year guide implies the next three quarters decline about twice as fast as Q1",
    "Arithmetic: FY26 revenue $46,398M. Q1 FY27 $11,213M, down 4.3%. A full-year decline of 7% to 9% (our read of 'high-single digits'; the release does not say whether reported or currency-neutral) requires Q2 to Q4 to fall 7.9% to 10.6%. Outside China the range assumes Greater China falls 26% to 40% for the rest of the year. If the guide is currency-neutral, the figures improve by about 1 point and the conclusion still holds. Performance (about $16B) and its growth are management statements on the call. Nike landed inside or above its guided range on revenue and gross margin 16 of 16 times in the last eight quarters, but Q1 FY27 revenue (-4.3% against a midpoint of about -3.5%) was the first to fall below the midpoint, so we do not rely on a Q2 miss.");
  const rows = [
    [hdr("Revenue change vs prior year"), hdr("Q1 FY27 (actual)", "right"), hdr("Q2 to Q4 FY27 (implied by guide)", "right")],
    [cell("All of Nike", { bold: true }), cell("-4.3%", { align: "right", fontSize: 18, bold: true }), cell("-7.9% to -10.6%", { align: "right", fontSize: 18, bold: true, color: RED })],
    [cell("NIKE Brand outside Greater China", { bold: true }), cell("-0.8%", { align: "right", fontSize: 18, bold: true }), cell("-2.6% to -7.8%", { align: "right", fontSize: 18, bold: true, color: RED })],
  ];
  s.addTable(rows, { x: 0.6, y: 1.65, w: 12.13, colW: [4.9, 3.0, 4.23], rowH: [0.42, 0.7, 0.7], fontFace: FONT, fontSize: 12 });
  s.addText([
    { text: "Performance (running, football; about $16B) is growing high single digits. If it keeps growing 5% to 9%, the other roughly $30B of Nike must fall about 13% to 18.5% for the guide to hold.", options: { bullet: true, breakLine: true, paraSpaceAfter: 12 } },
    { text: "Nike landed inside or above its guided range on revenue and gross margin 16 of 16 times in eight quarters, but Q1 FY27 revenue was the first below the midpoint. We do not rely on a Q2 miss; the case is FY28.", options: { bullet: true, breakLine: true, paraSpaceAfter: 12 } },
    { text: "Gross margin: Q2 FY27 laps a quarter that took a 360 bp tariff hit (40.6%), and Q4 FY27 laps 49.2%, which included about 900 bp of one-off tariff refund. Reported margin will look good, then bad.", options: { bullet: true } },
  ], { x: 0.6, y: 3.85, w: 12.13, h: 2.45, fontFace: FONT, fontSize: 15, color: INK, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: Nike Q1 FY27 release (guide read as -7% to -9%; wording does not specify reported vs currency-neutral) and 10-Q p.25; Q1 FY27 call; guidance record scored against call transcripts and releases (research_notes/Smoking gun hunt/G9_guidance_record.md). Implied ranges are team arithmetic.");
}

// =============== 9. CHINA ===============
{
  const s = content("Evidence", "In China, Nike's two largest partners have closed 26% of their doors in three years, faster than most domestic brands",
    "Topsports plus Pou Sheng: 9,932 doors (Jun/Aug 2023) to about 7,322 (Jun 2026). The June 2026 Topsports count is an estimate from May selling area; Topsports reports August doors on Oct 28. No source counts Nike-only doors; the partners also sell adidas and others, and sales per door are rising (Topsports Nike-plus-adidas revenue per average door RMB 3.91m, 4.18m, 4.76m for FY24 to FY26), so some closures are cleanup. 361 and the kids lines are also closing stores, so 'domestic brands hold' applies only to ANTA, Li-Ning and Xtep adult. Nike's store-locator count of 2,438 is stale and must not be cited. China overall is our strongest grade because of Nike's own guide and the peer-set share series.");
  s.addChart(pres.charts.BAR, [{ name: "Change in doors, 3 years (%)", labels: ["Topsports + Pou Sheng (Nike's largest partners)", "361 Degrees core", "361 Degrees Kids", "Xtep Kids", "ANTA KIDS", "Xtep Adult", "Li-Ning", "ANTA"], values: [-26.0, -10.0, -10.0, -8.4, -4.9, -2.1, -1.7, 2.6] }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 7.6, h: 4.55, barDir: "bar", barGapWidthPct: 40, catAxisOrientation: "maxMin", catAxisLabelPos: "low", chartColors: [RED, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '0.0"%"', title: "Change in store doors, mid-2023 to mid-2026 (%)", valAxisMinVal: -32, valAxisMaxVal: 8, catAxisLabelFontSize: 11,
  }));
  const stats = [
    ["-26%", "Greater China revenue, Q1 FY27, currency-neutral. Ninth straight decline."],
    ["65% to 50%", "Nike's share of a 14-company China peer set, 2022 to H1 2026."],
    ["$2.31B to $1.28B", "Greater China EBIT, FY24 to FY26 (-45%)."],
  ];
  stats.forEach((st, i) => {
    const y = 1.75 + i * 1.5;
    s.addText(st[0], { x: 8.6, y, w: 4.1, h: 0.6, fontFace: FONT, fontSize: 28, bold: true, color: i === 2 ? RED : NAVY, margin: 0, isTextBox: true });
    s.addText(st[1], { x: 8.6, y: y + 0.62, w: 4.1, h: 0.75, fontFace: FONT, fontSize: 12, color: INK, margin: 0, valign: "top", isTextBox: true });
  });
  source(s, "Sources: HKEX annual and interim reports (Topsports 6110, Pou Sheng 3813, ANTA, Li-Ning, Xtep, 361 Degrees) through Jun 2026; Nike Q1 FY27 10-Q; FY24 and FY26 10-Ks. No source counts Nike-only doors; partners also sell adidas. Topsports reports Aug 2026 doors on Oct 28.");
}

// =============== 9b. UNITS VS PRICE ===============
{
  const s = content("Evidence", "Footwear volume is back where it was in FY19; every dollar of growth since then was price, and price is now falling",
    "From Nike's 10-K unit and ASP disclosures (NIKE Brand footwear, percent change by year; indices are team arithmetic from the rounded integers, so each year carries about half a point of rounding). Units: FY19 = 100, FY26 = 99.9. Reported revenue per pair: 122.0, currency-neutral ASP 127.2. From the FY23 unit peak, units are -10.7% and revenue -10.9%, so revenue per pair is flat and the volume cut is not being recovered in price. ASP contribution turned negative in FY25 (-3 points), FY26 (-1) and Q1 FY27 (-1), while Q1 FY27 units fell 5%. Apparel is the opposite: units -12.7% from FY23 with revenue per unit +11.3%. Lost footwear units since FY23 split about 45% North America, 30% EMEA, 25% Greater China. Nike's unit sales are recognized sales, so deliberate supply cuts and weaker sell-through cannot be separated from filings; Circana or GfK sell-through would decide it.");
  s.addChart(pres.charts.LINE, [
    { name: "Footwear units (FY19 = 100)", labels: ["FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"], values: [100.0, 92.0, 102.1, 99.1, 111.9, 109.7, 100.9, 99.9] },
    { name: "Reported revenue per pair (FY19 = 100)", labels: ["FY19", "FY20", "FY21", "FY22", "FY23", "FY24", "FY25", "FY26"], values: [100.0, 104.6, 113.3, 121.5, 122.2, 125.8, 120.7, 122.0] },
  ], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 7.2, h: 4.55, chartColors: [NAVY, RED], lineSize: 2.5, lineDataSymbol: "circle", lineDataSymbolSize: 7,
    showValue: false, showLegend: true, legendPos: "b", legendFontSize: 11, legendFontFace: FONT, title: "NIKE Brand footwear: units vs revenue per pair, indexed (FY19 = 100)", valAxisMinVal: 80, valAxisMaxVal: 130,
  }));
  label(s, "Quarterly footwear: units and price contribution (year on year)", 8.2, 1.75, 4.5);
  const rows = [
    [hdr("Quarter"), hdr("Units", "right"), hdr("ASP (pts)", "right")],
    [cell("Q1 FY26"), cell("+2%", { align: "right" }), cell("-4", { align: "right", color: RED })],
    [cell("Q2 FY26"), cell("0%", { align: "right" }), cell("-1", { align: "right", color: RED })],
    [cell("Q3 FY26"), cell("-2%", { align: "right", color: RED }), cell("+1", { align: "right" })],
    [cell("Q1 FY27"), cell("-5%", { align: "right", bold: true, color: RED }), cell("-1", { align: "right", color: RED })],
  ];
  s.addTable(rows, { x: 8.2, y: 2.15, w: 4.53, colW: [1.73, 1.4, 1.4], rowH: 0.4, fontFace: FONT, fontSize: 12 });
  s.addText("Seven years, zero unit growth. The FY28 consensus needs the rest of Nike outside China to grow 3% to 4%, in units or price, while both are falling.", { x: 8.2, y: 4.35, w: 4.53, h: 1.6, fontFace: FONT, fontSize: 14, bold: true, color: NAVY, margin: 0, valign: "top", isTextBox: true });
  source(s, "Sources: Nike 10-Ks FY16 to FY26 (NIKE Brand footwear unit and ASP percent changes, e.g. FY26 10-K p.33) and 10-Qs through Q1 FY27 (p.23); indices and regional split are team arithmetic (research_notes/Smoking gun hunt/G3_units_factories.md). Q4 quarters are not disclosed.");
}

// =============== 9c. FORENSIC HUNT ===============
{
  const s = content("Evidence", "Independent data contradicts the 'deliberate' explanation for digital, and Nike has withdrawn the disclosures that would settle the rest",
    "Traffic: Semrush public trending pages for August 2026, the last month of Q1 FY27, read from the embedded page data; one month only, no multi-year series was obtainable free. Nike says the digital decline is a deliberate cut in off-price volume. If so, visits should hold while revenue falls. Globally visits fell 11.4% against digital revenue -13%, and in North America visits fell 11.4% against revenue -6%, while adidas.com rose 12.5% and DICK'S 15.2%. Only EMEA fits the deliberate story. Disclosures: a full diff of every 10-K, 10-Q and release FY18 to Q1 FY27 found 16 KPI-type disclosure families withdrawn in the last nine quarters against about five in the prior 24 (Poisson probability about 2e-10); of the 12 with a clear direction, 11 were deteriorating when pulled (Fisher one-sided p = 0.003). Nike also added adverse disclosures in the same period, SEC rules explain four removals, and peers drop tags too, so we say 'withdrawn while deteriorating', not 'hiding'. Receivables: wholesale DSO rose 4.5 to 9.7 days year on year from Q3 FY26 to Q1 FY27 after tariff-refund and FX adjustments, more than any peer, and the segment receivables table that would show where was withdrawn in FY25. Reserves: the sales-related reserve fell from $1,834M (May 2025) to $1,488M (Aug 2026); lapping the FY25 build is worth up to $797M of revenue year on year if usage was unchanged, a base effect management pre-announced. A skeptic check rejected the stronger claim that it explains the guidance beats.");
  s.addChart(pres.charts.BAR, [{ name: "Website visits, Aug 2026 vs Aug 2025 (%)", labels: ["nike.com", "Puma", "Under Armour", "New Balance", "Decathlon", "ASICS", "adidas.com", "DICK'S"], values: [-11.4, -5.6, -3.7, 0.4, 0.2, 0.9, 12.5, 15.2] }], Object.assign({}, chartBase, {
    x: 0.6, y: 1.65, w: 6.1, h: 4.55, barDir: "bar", barGapWidthPct: 40, catAxisOrientation: "maxMin", catAxisLabelPos: "low", chartColors: [RED, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE, LSLATE],
    dataLabelPosition: "outEnd", dataLabelFormatCode: '0.0"%"', title: "Global website visits, Aug 2026 year on year (%)", valAxisMinVal: -16, valAxisMaxVal: 20, catAxisLabelFontSize: 11,
  }));
  label(s, "What else the forensic pass found (Nike filings)", 7.1, 1.75, 5.6);
  const rows = [
    [hdr("Item"), hdr("Finding")],
    [cell("Disclosures withdrawn", { bold: true }), cell("16 KPI disclosure families dropped in 9 quarters vs about 5 in the prior 24; 11 of 12 with a clear direction were deteriorating (receivables by segment, returns-reserve rollforward, comparable store sales, Men's/Women's/Kids' split, ASP line of the margin bridge)")],
    [cell("Wholesale receivable days", { bold: true }), cell("+4.5 to +9.7 days year on year, Q3 FY26 to Q1 FY27, after tariff-refund and FX adjustments; larger than any peer; cause not separable (timing, slow pay or longer terms)")],
    [cell("Sales-related reserve", { bold: true }), cell("$1,834M (May 2025) to $1,488M (Aug 2026). Lapping the FY25 build is a tailwind worth up to about $0.30 to $0.43 of FY26 EPS if usage was unchanged, and it fades in FY27")],
    [cell("Unreserved contingency", { bold: true }), cell("Belgian customs claim, EUR 1.5B per Belgian press, no amount or accrual in Nike's filings; bank guarantees rose from $289M (FY22) to about $1.3B (FY26); hearing listed Nov 30")],
  ];
  s.addTable(rows, { x: 7.1, y: 2.15, w: 5.63, colW: [1.55, 4.08], rowH: [0.36, 1.05, 0.8, 0.8, 0.85], fontFace: FONT, fontSize: 10 });
  source(s, "Sources: Semrush public trending pages (Aug 2026, read Oct 15, 2026); Nike 10-Ks FY18 to FY26, 10-Qs through Q1 FY27 and releases (full-text diffs); TV Limburg (Aug 28, 2026) for the hearing date. Notes: research_notes/Smoking gun hunt/G6, G11, G2, G12 (with G12_check) and G10.");
}

// =============== 10. RISKS ===============
pres.addSection({ title: "Risks and catalysts" });
{
  const s = content("Risks and catalysts", "The main risks to the short are running momentum, tariff relief and a crowded position; none outweighs the FY28 gap",
    "Crowded short: 99.2M shares short at Sep 30, 2026 is 8.2% of the 1,203.9M Class B shares that trade (the repo's earlier 6.7% used all share classes). Borrow is cheap (Interactive Brokers 0.41%, Ortex 0.53%), lendable supply is about five times the short, and on Oct 1 to 2 255M shares traded without a squeeze. After record short interest in 27 consumer stocks (2021 to 2026), shorts won 81 of 119 at 6 months, but about 12% of cases ended more than 25% above the market, mostly on earnings-day jumps. Express the idea with puts or a limited-loss structure. Insider buying did not predict returns in historical tests, and the checker found two Form 144 sale notices by the former CFO.");
  const rows = [
    [hdr("Risk to our view"), hdr("Evidence"), hdr("Our assessment")],
    [cell("Running recovery is real", { bold: true }), cell("Dick's running reviews +48.6% vs Hoka +21.6%, Brooks +15.8% (Jun to Jul 2026); Pegasus 42 and Vomero 18 rated 4.8"), cell("Real volume, but Pegasus 42 is marked down and growth lags ASICS and adidas; offsets lifestyle, not the FY28 gap")],
    [cell("Tariffs lower than planned", { bold: true }), cell("About 11.4% blended in force vs 15% plan; worth about +$0.08 to $0.12 of FY28 EPS"), cell("Probably in the Oct 1 guide already; FY28 tail is two-sided (about +/-$0.10 to $0.25)")],
    [cell("Crowded short", { bold: true }), cell("99.2M shares short, 8.2% of tradable shares; 2.6 to 3.8 days to cover; borrow about 0.4% to 0.5%"), cell("Not a squeeze setup; shorts won 81 of 119 at 6 months after past records, with a fat right tail. Use puts")],
    [cell("Insider buying", { bold: true }), cell("$5.96M (2025) and $2.73M (2026 YTD), largest in 20 years"), cell("Did not predict returns historically; ex-CFO filed two Form 144 sale notices")],
    [cell("Guidance is conservative", { bold: true }), cell("Inside or above the guided range 16 of 16 times (revenue and gross margin, 8 quarters); Q1 FY27 first below midpoint"), cell("We do not rely on a Q2 miss; the thesis is FY28")],
    [cell("Product pipeline is rebuilding", { bold: true }), cell("21 intent-to-use US trademark filings for new product names in Jan to Sep 2026; prior 15-year high was 7. Names typically ship within about 3 months of filing"), cell("Supports a late FY27 to FY28 launch wave; volume effect cannot be sized from filings. The main long argument")],
  ];
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.13, colW: [2.4, 5.0, 4.73], rowH: [0.38, 0.72, 0.62, 0.72, 0.55, 0.55, 0.78], fontFace: FONT, fontSize: 11 });
  source(s, "Sources: Dick's/Foot Locker review feed (Jun to Jul 2026); tariff gap sizing (USTR Section 301 notice, Jul 2026; Nike 10-Q); FINRA (Sep 30, 2026), Ortex, Interactive Brokers borrow data; SEC Form 4 and 13F data; guidance record (G9); USPTO trademark search (G7).");
}

// =============== 11. CATALYSTS ===============
{
  const s = content("Risks and catalysts", "Investor Day on Nov 16 to 17 is the decisive event, two days before finals",
    "Decision rules written in advance. Investor Day: a dated long-term operating margin target of 13% or more with an interim bridge would falsify the margin argument; an undated target or one below about 12% supports it. Feng Tay October revenue is published on Taiwan's MOPS around the 10th of each month; thresholds are on a two-year US-dollar basis. Q2 FY27 results arrive around Dec 17, after finals. The dividend is usually declared between Nov 14 and 20; a freeze or token raise is the likely outcome and a mild positive; a large raise would work against us.");
  const rows = [
    [hdr("Date"), hdr("Event"), hdr("Supports the short if"), hdr("Supports a long if")],
    [cell("Oct 28"), cell("Topsports interim results", { bold: true }), cell("Door decline continues; China wholesale weak"), cell("Doors stabilize")],
    [cell("About Nov 10"), cell("Feng Tay October revenue", { bold: true }), cell("Worse than -8% (two-year, USD) while peer factories hold"), cell("Better than -3%")],
    [cell("Nov 14 to 20"), cell("Dividend declaration", { bold: true }), cell("Cut"), cell("Raise well above token level")],
    [cell("Nov 16 to 17", { bold: true, color: RED }), cell("Nike Investor Day", { bold: true }), cell("FY28 EPS framed below about $1.50, or revenue below flat"), cell("FY28 held, plus FY29 margin target above about 9%")],
    [cell("Nov 19"), cell("Finals", { bold: true }), cell("Update pitch for Investor Day"), cell("Update pitch for Investor Day")],
    [cell("Nov 30"), cell("Belgian customs case, merits hearing (press)", { bold: true }), cell("Adverse ruling on EUR 1.5B claim: $0.23 to $0.36 one-time EPS in the base case, unreserved by Nike"), cell("Nike wins or the claim is cut sharply")],
    [cell("About Dec 17"), cell("Q2 FY27 results", { bold: true }), cell("Gross margin below 40.6%; wholesale receivable days still rising"), cell("Gross margin well above 41% with pricing positive")],
  ];
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.13, colW: [1.7, 2.7, 4.1, 3.63], rowH: [0.38, 0.55, 0.55, 0.5, 0.65, 0.5, 0.7, 0.6], fontFace: FONT, fontSize: 11 });
  source(s, "Sources: Nike Q4 FY26 call (Investor Day date, Jun 30, 2026); Taiwan MOPS; HKEX; team decision rules (research_notes/Long or short cruxes/00_SCOREBOARD.md). Belgian hearing date from Belgian press (TV Limburg, Aug 28, 2026); Nike discloses the claim without an amount (10-Q Note 11). Dates for peer and supplier releases are expected, not confirmed.");
}

// =============== 12. METHOD AND DOWNGRADES ===============
pres.addSection({ title: "Appendix" });
{
  const s = content("Appendix", "Appendix: independent checkers downgraded several early findings, and the deck uses the corrected grades",
    "Twelve free-data areas were collected, then seven deep dives (D1 to D7) and twelve forensic hunts (G1 to G12, each with an alternatives log) were run; every candidate smoking gun was given to a separate skeptic. None survived as a single decisive fact, so the pitch rests on the mosaic. Earlier: (stores, hiring, trade, resale, pricing, attention, apps, reviews, insiders and funds, market size, peers, marketing), plus earnings calls, tariffs, history and short-interest checks. A separate checker re-pulled samples and re-ran tests for each area. These are the main corrections. Items that could not be measured: Nike's own US shipment volumes (Nike's name is masked in public bills of lading), and Census trade data needs an email registration which was not used.");
  const rows = [
    [hdr("Early claim"), hdr("After checking")],
    [cell("Resale decline has stopped (Nike + Jordan -2.3% YoY)"), cell("Mostly the weaker yen; about -9.5% in USD, rivals -5.5%. Launch-premium gain disappears for men's sizes")],
    [cell("Market size: strong short on North America volume"), cell("Not supported for the last four quarters (Nike units at or above real spending); rests on FY24 to FY25 and price")],
    [cell("Factory vs US imports: strong"), cell("Moderate; four of seven benchmarks are the same goods from the same countries")],
    [cell("Product hiring share doubled to 36%"), cell("Overstated; October open postings are about 5% to 6% below last year")],
    [cell("Store closures: 33 of 73 US in-line stores (45%)"), cell("Confirmed, but all small Well Collective doors; about 0.15% to 0.35% of revenue, so weak as a revenue signal")],
    [cell("Positioning (13F exits, short interest, insider buying)"), cell("Did not predict returns in historical tests; fund exits overstated about fivefold")],
    [cell("Reserve releases explain the FY26 guidance beats ($0.30 to $0.43 EPS)"), cell("Skeptic check: a pre-announced base effect; filings cannot separate lower provision from higher usage; beat and reserve swing correlate -0.08 over eight quarters")],
    [cell("Nike's 63% P/E premium is unjustified; dividend cut likely; 86% of declines are China and Converse"), cell("Premium is mostly trough earnings (at FY24 margin Nike trades 8% below peers); balance sheet covers the dividend for years; gross share is 70%")],
  ];
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.13, colW: [4.6, 7.53], rowH: [0.38, 0.5, 0.5, 0.45, 0.45, 0.5, 0.45, 0.62, 0.62], fontFace: FONT, fontSize: 11 });
  source(s, "Sources: checker reviews in data/hunt/*/README.md and research_notes/Long or short cruxes/. Unmeasurable: Nike US shipment volumes (masked consignee), Census API (registration required).");
}

// =============== 13. SOURCES ===============
{
  const s = content("Appendix", "Appendix: primary sources and where the data lives", "All numbers trace to the documents below or to labeled team arithmetic. The repo holds the cleaned data, scripts and notes.");
  const rows = [
    [hdr("Category"), hdr("Sources")],
    [cell("Nike filings and calls", { bold: true }), cell("FY24, FY25, FY26 Form 10-K; Q1 FY27 Form 10-Q and earnings release (Oct 1, 2026); official call transcripts Q1 FY21 to Q1 FY27 (investors.nike.com)")],
    [cell("Peers and market", { bold: true }), cell("adidas, On, Deckers, ASICS results; HKEX filings (Topsports, Pou Sheng, ANTA, Li-Ning, Xtep, 361); Taiwan MOPS (Feng Tay and others); Yahoo Finance; FINRA; BEA; BLS; China NBS")],
    [cell("Alternative data", { bold: true }), cell("Common Crawl nike.com panel; Nike store API; SNKRDUNK resale; Dick's, Foot Locker and Fleet Feet product feeds; Google Play reviews; Wikipedia pageviews")],
    [cell("Analysis in the repo", { bold: true }), cell("research_notes/Long or short cruxes/ (scoreboard and eight question notes); data/hunt/ (cleaned data and scripts); research_notes/Deep dives Oct 14/ (FY28 bridge, long case, valuation, dividend, Investor Day study); research_notes/Smoking gun hunt/ (units, receivables, reserves, disclosures, traffic, IP, credit, tax, litigation, Belgian customs); research_notes/Refinitiv pull list.md")],
  ];
  s.addTable(rows, { x: 0.6, y: 1.6, w: 12.13, colW: [2.7, 9.43], rowH: [0.38, 0.75, 0.75, 0.75, 0.75], fontFace: FONT, fontSize: 12 });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("wrote", OUT);
})();
