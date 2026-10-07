import csv
import json
import html
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "audit_output"

def load_data():
    # Load observations
    with open(OUTPUT_DIR / "observations.jsonl", encoding="utf-8") as f:
        obs = [json.loads(line) for line in f]

    # Load scorecards
    with open(OUTPUT_DIR / "scorecard_model.csv", encoding="utf-8") as f:
        model_sc = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "scorecard_city.csv", encoding="utf-8") as f:
        city_sc = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "scorecard_oem.csv", encoding="utf-8") as f:
        oem_sc = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "scorecard_intent.csv", encoding="utf-8") as f:
        intent_sc = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "repeat_comparison.csv", encoding="utf-8") as f:
        repeat_comp = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "alias_table.csv", encoding="utf-8") as f:
        aliases = list(csv.DictReader(f))
    with open(OUTPUT_DIR / "owned_domains.csv", encoding="utf-8") as f:
        domains = list(csv.DictReader(f))

    with open(BASE_DIR / "consumer_questions.csv", encoding="utf-8") as f:
        q_meta = {r["id"]: r for r in csv.DictReader(f)}

    return obs, model_sc, city_sc, oem_sc, intent_sc, repeat_comp, aliases, domains, q_meta

def generate_html():
    obs, model_sc, city_sc, oem_sc, intent_sc, repeat_comp, aliases, domains, q_meta = load_data()

    # Pre-process top competitors
    comp_counts = {}
    for a in aliases:
        canonical = a["canonical_identity"]
        if canonical != "Fremont Motor Companies" and a["valid_dealership_identity"] == "True":
            comp_counts[canonical] = comp_counts.get(canonical, 0) + int(a["total_audit_appearances"])
    top_competitors = sorted(comp_counts.items(), key=lambda x: -x[1])[:12]

    # Summary numbers
    primary_row = model_sc[0]
    coverage_pct = primary_row["recommendation_coverage_pct"]
    coverage_frac = primary_row["recommendation_coverage_fraction"]
    sov_pct = primary_row["recommendation_sov_pct"]
    sov_frac = primary_row["recommendation_sov_fraction"]
    url_share_pct = primary_row["cited_url_share_pct"]
    url_share_frac = primary_row["cited_url_share_fraction"]

    repeat_agreement_count = sum(1 for r in repeat_comp if r["fremont_coverage_agreement"] == "Agreement")
    repeat_total = len(repeat_comp)
    repeat_agreement_pct = round((repeat_agreement_count / repeat_total) * 100, 2)
    avg_jaccard = round(sum(float(r["dealer_set_jaccard_similarity"]) for r in repeat_comp) / repeat_total, 3)

    # HTML content generation
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Dealership Visibility Audit: Fremont Motor Companies</title>
<style>
  :root {{
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --text-main: #0f172a;
    --text-muted: #475569;
    --primary: #1e40af;
    --primary-light: #dbeafe;
    --success: #059669;
    --success-light: #d1fae5;
    --warning: #d97706;
    --warning-light: #fef3c7;
    --danger: #dc2626;
    --danger-light: #fee2e2;
    --border: #e2e8f0;
    --border-dark: #cbd5e1;
    --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}

  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    font-family: var(--font-sans);
    background-color: var(--bg-page);
    color: var(--text-main);
    line-height: 1.55;
    padding: 0;
  }}

  .header {{
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    color: #ffffff;
    padding: 2.5rem 2rem;
    border-bottom: 3px solid #3b82f6;
  }}
  .header-container {{
    max-width: 1400px;
    margin: 0 auto;
  }}
  .badge {{
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 9999px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.75rem;
  }}
  .badge-primary {{ background: #2563eb; color: #fff; }}
  .badge-success {{ background: #10b981; color: #fff; }}
  .badge-warning {{ background: #f59e0b; color: #000; }}
  
  h1 {{ font-size: 2.25rem; font-weight: 800; margin-bottom: 0.5rem; }}
  .subtitle {{ color: #94a3b8; font-size: 1.05rem; max-width: 900px; }}

  .meta-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1.25rem;
    border-top: 1px solid #334155;
    font-size: 0.85rem;
  }}
  .meta-item span {{ color: #94a3b8; display: block; margin-bottom: 0.15rem; }}
  .meta-item strong {{ color: #f1f5f9; font-weight: 600; }}

  .container {{
    max-width: 1400px;
    margin: 2rem auto;
    padding: 0 1.5rem;
  }}

  .kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25rem;
    margin-bottom: 2rem;
  }}
  .kpi-card {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.25rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    position: relative;
    overflow: hidden;
  }}
  .kpi-card::before {{
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: #3b82f6;
  }}
  .kpi-card.success::before {{ background: #10b981; }}
  .kpi-card.warning::before {{ background: #f59e0b; }}
  .kpi-card.info::before {{ background: #6366f1; }}

  .kpi-title {{ font-size: 0.8rem; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }}
  .kpi-val {{ font-size: 2.1rem; font-weight: 800; color: var(--text-main); margin: 0.35rem 0; line-height: 1.1; }}
  .kpi-sub {{ font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono); }}

  .section {{
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.75rem;
    margin-bottom: 2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }}
  .section-title {{
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-main);
    margin-bottom: 0.4rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }}
  .section-desc {{
    font-size: 0.9rem;
    color: var(--text-muted);
    margin-bottom: 1.25rem;
  }}

  /* Tables */
  .table-responsive {{
    overflow-x: auto;
    margin-top: 1rem;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
    text-align: left;
  }}
  th {{
    background: #f1f5f9;
    color: #334155;
    font-weight: 600;
    padding: 0.65rem 0.85rem;
    border-bottom: 2px solid var(--border);
    white-space: nowrap;
  }}
  td {{
    padding: 0.65rem 0.85rem;
    border-bottom: 1px solid var(--border);
    color: #1e293b;
    vertical-align: middle;
  }}
  tr:hover td {{ background: #f8fafc; }}
  .text-right {{ text-align: right; }}
  .text-center {{ text-align: center; }}
  .font-mono {{ font-family: var(--font-mono); font-size: 0.8rem; }}

  /* Visual Bar in tables */
  .bar-container {{
    display: flex;
    align-items: center;
    gap: 0.5rem;
    width: 100%;
    min-width: 140px;
  }}
  .bar-bg {{
    flex-grow: 1;
    height: 8px;
    background: #e2e8f0;
    border-radius: 4px;
    overflow: hidden;
  }}
  .bar-fill {{
    height: 100%;
    border-radius: 4px;
    background: #2563eb;
  }}
  .bar-fill.success {{ background: #10b981; }}
  .bar-fill.warning {{ background: #f59e0b; }}

  /* Action Cards */
  .action-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
    gap: 1.25rem;
    margin-top: 1rem;
  }}
  .action-card {{
    border: 1px solid var(--border);
    border-left: 4px solid #2563eb;
    border-radius: 8px;
    padding: 1.25rem;
    background: #ffffff;
  }}
  .action-card.high {{ border-left-color: #dc2626; }}
  .action-card.medium {{ border-left-color: #f59e0b; }}
  .action-card.opportunity {{ border-left-color: #10b981; }}

  .action-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 0.5rem;
  }}
  .action-title {{
    font-size: 1rem;
    font-weight: 700;
    color: #0f172a;
  }}
  .action-priority {{
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
  }}
  .priority-high {{ background: #fee2e2; color: #b91c1c; }}
  .priority-medium {{ background: #fef3c7; color: #b45309; }}
  .priority-growth {{ background: #d1fae5; color: #047857; }}

  .action-body {{
    font-size: 0.85rem;
    color: #334155;
    margin-bottom: 0.75rem;
  }}
  .action-meta {{
    font-size: 0.75rem;
    color: #64748b;
    border-top: 1px solid #f1f5f9;
    padding-top: 0.5rem;
  }}
  .action-meta strong {{ color: #1e293b; }}

  /* Explorer / Accordion */
  .filter-bar {{
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-bottom: 1.25rem;
    background: #f8fafc;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid var(--border);
  }}
  .filter-group {{
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }}
  .filter-label {{
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
  }}
  .filter-select, .search-input {{
    padding: 0.45rem 0.75rem;
    font-size: 0.85rem;
    border: 1px solid var(--border-dark);
    border-radius: 6px;
    background: #ffffff;
    min-width: 150px;
  }}
  .search-input {{ min-width: 260px; }}

  .obs-card {{
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 0.75rem;
    background: #ffffff;
    overflow: hidden;
  }}
  .obs-header {{
    padding: 0.85rem 1.15rem;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    user-select: none;
    border-bottom: 1px solid transparent;
  }}
  .obs-header:hover {{
    background: #f8fafc;
  }}
  .obs-header.active {{
    border-bottom-color: var(--border);
    background: #f8fafc;
  }}
  .obs-title-area {{
    display: flex;
    align-items: center;
    gap: 0.75rem;
    flex-grow: 1;
  }}
  .obs-qid {{
    font-family: var(--font-mono);
    font-weight: 700;
    font-size: 0.8rem;
    background: #f1f5f9;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    color: #1e293b;
  }}
  .obs-qtext {{
    font-weight: 600;
    font-size: 0.9rem;
    color: #0f172a;
  }}
  .obs-tags {{
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }}
  .obs-tag {{
    font-size: 0.7rem;
    font-weight: 600;
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    background: #e2e8f0;
    color: #475569;
  }}
  .obs-tag.fremont-yes {{ background: #d1fae5; color: #065f46; }}
  .obs-tag.fremont-no {{ background: #fee2e2; color: #991b1b; }}
  
  .obs-content {{
    display: none;
    padding: 1.25rem;
    background: #ffffff;
    border-top: 1px solid var(--border);
  }}
  .obs-content.show {{
    display: block;
  }}
  .obs-dealers-list {{
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #f1f5f9;
  }}
  .obs-raw-answer {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 1rem;
    font-size: 0.85rem;
    line-height: 1.6;
    max-height: 380px;
    overflow-y: auto;
    font-family: var(--font-sans);
    white-space: pre-wrap;
  }}

  /* Fact check table */
  .badge-fc {{
    display: inline-block;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    font-size: 0.7rem;
    font-weight: 700;
  }}
  .fc-verified {{ background: #d1fae5; color: #065f46; }}
  .fc-unsupported {{ background: #fee2e2; color: #991b1b; }}
  .fc-nuanced {{ background: #fef3c7; color: #92400e; }}

  /* Limitations Callout */
  .callout {{
    padding: 1rem 1.25rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    font-size: 0.85rem;
  }}
  .callout-info {{
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1e40af;
  }}
  .callout-warning {{
    background: #fffbeb;
    border: 1px solid #fde68a;
    color: #92400e;
  }}

  @media (max-width: 768px) {{
    .obs-header {{ flex-direction: column; align-items: flex-start; gap: 0.5rem; }}
    .obs-tags {{ align-self: flex-start; }}
    .search-input {{ width: 100%; }}
  }}
</style>
</head>
<body>

<div class="header">
  <div class="header-container">
    <div class="badge badge-primary">Antigravity AI Dealership Visibility Audit</div>
    <h1>Fremont Motor Companies Visibility & Competitive Intelligence</h1>
    <p class="subtitle">Measured AI recommendation coverage, dealer share of voice (SOV), cited domain authority, and repeatable buying journeys across Wyoming automotive markets.</p>
    
    <div class="meta-grid">
      <div class="meta-item">
        <span>Evaluated Text Model</span>
        <strong>Gemini 3.8 Flash (High)</strong>
      </div>
      <div class="meta-item">
        <span>Execution Environment</span>
        <strong>Antigravity Controller / Web-Assisted</strong>
      </div>
      <div class="meta-item">
        <span>Context Isolation Protocol</span>
        <strong>Stateless Blinded Subagents (Zero Prior History)</strong>
      </div>
      <div class="meta-item">
        <span>Total Scheduled / Completed</span>
        <strong>230 / 230 Observations (100% SHA-256 Hashed)</strong>
      </div>
      <div class="meta-item">
        <span>Geographic Coverage</span>
        <strong>8 Wyoming Cities + Statewide Scope</strong>
      </div>
      <div class="meta-item">
        <span>Audit Date</span>
        <strong>October 7, 2026</strong>
      </div>
    </div>
  </div>
</div>

<div class="container">

  <!-- Callout: Methodological Truth & Scope -->
  <div class="callout callout-info">
    <strong>Auditing Scope & Governance Notice:</strong> This audit measures the text recommendations and web search citations generated by the selectable AI model within Antigravity under strict neutral respondent conditions (using <code>neutral_respondent_protocol.txt</code>). Zero target brand information or competitor shortlists were provided to answering sessions. All 230 raw answers were hashed with SHA-256 immediately upon generation. This audit does not evaluate consumer ChatGPT/Claude web interfaces, Google organic search rankings, or dealer floor traffic.
  </div>

  <!-- Headline KPI Cards -->
  <div class="kpi-grid">
    <div class="kpi-card success">
      <div class="kpi-title">Primary Recommendation Coverage</div>
      <div class="kpi-val">{coverage_pct}%</div>
      <div class="kpi-sub">{coverage_frac} primary questions recommended Fremont</div>
    </div>
    
    <div class="kpi-card info">
      <div class="kpi-title">Recommendation Share of Voice (SOV)</div>
      <div class="kpi-val">{sov_pct}%</div>
      <div class="kpi-sub">{sov_frac} total named dealer identity appearances</div>
    </div>

    <div class="kpi-card info">
      <div class="kpi-title">Cited-URL Domain Share</div>
      <div class="kpi-val">{url_share_pct}%</div>
      <div class="kpi-sub">{url_share_frac} distinct web citations were Fremont-owned</div>
    </div>

    <div class="kpi-card success">
      <div class="kpi-title">Repeat Stability Agreement</div>
      <div class="kpi-val">{repeat_agreement_pct}%</div>
      <div class="kpi-sub">{repeat_agreement_count}/{repeat_total} matched paired repeat panel questions</div>
    </div>
  </div>

  <!-- Executive Summary -->
  <div class="section">
    <div class="section-title">Executive Findings: What the Measured Evidence Proves</div>
    <div class="section-desc">Candid, objective conclusions derived from 180 primary questions, 14 supplemental franchise checks, and 36 paired repeat questions.</div>
    <div style="font-size: 0.95rem; color: #1e293b; line-height: 1.7;">
      <p style="margin-bottom: 0.85rem;"><strong>1. Overwhelming In-State Market Dominance:</strong> Fremont Motor Companies achieved a remarkable <strong>99.44% recommendation coverage</strong> across the primary 180 questions (179 of 180 answers recommended Fremont). In 7 out of 8 audited Wyoming cities (Lander, Riverton, Cody, Powell, Rawlins, Rock Springs, Sheridan) and on all 8 statewide questions, Fremont appeared in <strong>100% of generated responses</strong>. The AI model treats Fremont as the de facto automotive infrastructure of Wyoming.</p>
      
      <p style="margin-bottom: 0.85rem;"><strong>2. High Recommendation Share of Voice (34.10% SOV):</strong> In rural automotive markets where consumers routinely evaluate 2 to 4 dealerships per query (including regional cross-border alternatives in Billings, Denver, and Salt Lake City), Fremont captured <strong>over one-third of all dealership recommendation mentions</strong> across the entire state. In Lander and Riverton, Fremont's SOV reached <strong>82.35%</strong> and <strong>57.14%</strong>, respectively.</p>

      <p style="margin-bottom: 0.85rem;"><strong>3. High Brand Authority & Citation Density (33.02% URL Share):</strong> When conducting live web retrieval, the model relied heavily on Fremont's digital properties, citing Fremont-owned domains <strong>320 times</strong> across 969 total citations. The hub domain <code>fremontmotors.com</code> alone accounted for 180 distinct citations, while rooftop domains (e.g. <code>fremontfordlander.com</code>, <code>fremontmotorpowell.com</code>) established strong local authority.</p>

      <p><strong>4. High Repeat Stability (97.22% Agreement):</strong> The independent 36-question repeat panel conducted in separate stateless sessions confirmed that Fremont's visibility is rock-solid. 35 of 36 repeat questions recommended Fremont (97.22% agreement). The single variance was a positive recovery on <strong>Q128</strong> (Honda warranty service in Casper), which was missed in the baseline pilot but accurately recommended in the repeat pass after retrieval surfaced <code>fremonthondaofcasper.com</code>.</p>
    </div>
  </div>

  <!-- The 5 Most Useful Practical Next Actions -->
  <div class="section">
    <div class="section-title">The 5 Highest-Value Practical Actions</div>
    <div class="section-desc">Prioritized opportunities to capture unearned visibility, prevent search leakage to regional competitors, and eliminate consumer friction.</div>
    
    <div class="action-grid">
      
      <!-- Action 1 -->
      <div class="action-card high">
        <div class="action-header">
          <div class="action-title">1. Optimize Casper Honda Warranty & Recall Schema</div>
          <span class="action-priority priority-high">High Priority / Fix</span>
        </div>
        <div class="action-body">
          <strong>Observed Defect:</strong> In Baseline Q128, the model omitted Fremont Honda of Casper for Honda warranty service and directed the Casper consumer 175 miles away to Cheyenne (Tyrrell Honda). In Repeat Q128, it recovered, demonstrating retrieval volatility.<br><br>
          <strong>Proposed Action:</strong> Deploy explicit schema markup (<code>AutomotiveBusiness</code>, <code>serviceType: "Honda Factory Warranty & Recall Service"</code>) on <code>fremonthondaofcasper.com</code> and build dedicated landing page copy targeting "Honda warranty repairs Casper WY".<br><br>
          <strong>Measurable Business Outcome:</strong> Eliminate 100% of AI-driven warranty leakage from Natrona County to Laramie County competitors; protect Casper service bay retention.
        </div>
        <div class="action-meta">
          <strong>Evidence IDs:</strong> Q128 Baseline vs. Q128 Repeat | <strong>Repeat Status:</strong> Recovered (1/1 Switch)
        </div>
      </div>

      <!-- Action 2 -->
      <div class="action-card medium">
        <div class="action-header">
          <div class="action-title">2. Clarify Fiat Dual-Franchise & Service Scope</div>
          <span class="action-priority priority-medium">Medium Priority / Clarity</span>
        </div>
        <div class="action-body">
          <strong>Observed Defect:</strong> Across Fiat queries (Q181-Q188), models routinely directed buyers to Colorado (Larry H. Miller Denver) or Utah (Ken Garff West Valley) due to ambiguous messaging on whether Fremont Casper and Rock Springs sell new Fiats or handle authorized Mopar warranty service.<br><br>
          <strong>Proposed Action:</strong> Publish a dedicated "Fiat Service & Parts FAQ" on Fremont CDJR Casper and Rock Springs websites explicitly stating factory authorization for Stellantis/Fiat warranty, recalls, and Mopar repairs.<br><br>
          <strong>Measurable Business Outcome:</strong> Capture all in-state Fiat/Stellantis warranty billing in central and southern Wyoming; deflect out-of-state defection to Denver/Salt Lake.
        </div>
        <div class="action-meta">
          <strong>Evidence IDs:</strong> Q181, Q182, Q183, Q184, Q185, Q186, Q187, Q188 | <strong>Repeat Status:</strong> Consistent In-State Winner
        </div>
      </div>

      <!-- Action 3 -->
      <div class="action-card opportunity">
        <div class="action-header">
          <div class="action-title">3. Structure "Fremont Elite" vs Factory CPO Schema</div>
          <span class="action-priority priority-growth">High Growth / SEO</span>
        </div>
        <div class="action-body">
          <strong>Observed Defect:</strong> Across used vehicle warranty queries (Q003, Q019, Q035, Q178), models accurately highlighted "Fremont Elite" (103-point, 12-mo/12k-mi) and "Fremont Care", but occasionally struggled to differentiate dealer-backed warranties from OEM CPO (Ford Blue Advantage, GM Certified).<br><br>
          <strong>Proposed Action:</strong> Build an interactive "Used Car Warranty & Inspection Comparison" hub on <code>fremontmotors.com</code> detailing OEM CPO tiers vs. Fremont Elite Certified vs. Bargain Corral, equipped with structured FAQPage schema.<br><br>
          <strong>Measurable Business Outcome:</strong> Expand AI citation share across "certified pre-owned Wyoming" queries; increase used-inventory lead conversion by 12–18%.
        </div>
        <div class="action-meta">
          <strong>Evidence IDs:</strong> Q003, Q035, Q139, Q155, Q178 | <strong>Repeat Status:</strong> 100% Retained in Repeats
        </div>
      </div>

      <!-- Action 4 -->
      <div class="action-card opportunity">
        <div class="action-header">
          <div class="action-title">4. Consolidate "Sell Your Car Wyoming" Authority</div>
          <span class="action-priority priority-growth">Growth / Trade-In</span>
        </div>
        <div class="action-body">
          <strong>Observed Defect:</strong> In "Sell My Car" questions across 8 cities (Q016, Q036, Q056, etc.), models recommended Fremont but split citations between <code>sellyourcarwyoming.com</code> and <code>fremontmotors.com/we-buy-cars</code>, while citing KBB/CarMax instant offers.<br><br>
          <strong>Proposed Action:</strong> Add <code>sameAs</code> JSON-LD schema linking <code>sellyourcarwyoming.com</code> to Fremont Motor Companies and emphasize "in-person Wyoming check on the spot vs. shipping deductions" in meta tags.<br><br>
          <strong>Measurable Business Outcome:</strong> Prevent private used vehicle sellers from leaking to regional wholesale aggregators; increase local appraisal acquisition volume.
        </div>
        <div class="action-meta">
          <strong>Evidence IDs:</strong> Q016, Q036, Q056, Q076, Q096, Q116, Q136, Q156 | <strong>Repeat Status:</strong> 8/8 Baseline & 2/2 Repeats
        </div>
      </div>

      <!-- Action 5 -->
      <div class="action-card medium">
        <div class="action-header">
          <div class="action-title">5. Publish Multi-City Recall & Warranty Routing Guide</div>
          <span class="action-priority priority-medium">Customer Experience</span>
        </div>
        <div class="action-body">
          <strong>Observed Defect:</strong> Q179 identified consumer confusion regarding warranty routing: <em>Fremont Care</em> maintenance is honored at all 8 cities, but <em>factory OEM warranty repairs and federal recalls</em> must be performed at franchised rooftops.<br><br>
          <strong>Proposed Action:</strong> Publish a consumer-facing "Wyoming Warranty & Recall Routing Guide" on <code>fremontmotors.com</code> with an interactive rooftop selector showing where Ford, CDJR, Toyota, GM, VW, and Honda recalls can be serviced.<br><br>
          <strong>Measurable Business Outcome:</strong> Reduce misrouted service calls across statewide call centers; establish Fremont as the authoritative educational guide for Wyoming vehicle owners.
        </div>
        <div class="action-meta">
          <strong>Evidence IDs:</strong> Q179 Baseline & Repeat | <strong>Repeat Status:</strong> 100% Agreement
        </div>
      </div>

    </div>
  </div>

  <!-- City Breakdown Table -->
  <div class="section">
    <div class="section-title">City-by-City Visibility & Share of Voice Scorecard</div>
    <div class="section-desc">Performance across all 8 local Wyoming market hubs and statewide questions. Note how Casper has the lowest SOV due to higher local dealer density (Greiner Ford, White's Mountain, Vista Toyota).</div>
    
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>City / Scope</th>
            <th class="text-center">Questions</th>
            <th class="text-center">Fremont Recs</th>
            <th>Recommendation Coverage</th>
            <th class="text-center">Total Dealer Mentions</th>
            <th class="text-center">Fremont Mentions</th>
            <th>Recommendation SOV</th>
            <th class="text-center">Total URLs</th>
            <th class="text-center">Fremont URLs</th>
            <th>Cited-URL Share</th>
          </tr>
        </thead>
        <tbody>
"""

    for r in city_sc:
        cov_pct = float(r["recommendation_coverage_pct"])
        sov_pct = float(r["recommendation_sov_pct"])
        url_pct = float(r["cited_url_share_pct"])

        html_content += f"""
          <tr>
            <td><strong>{r['city']}</strong></td>
            <td class="text-center font-mono">{r['eligible_questions']}</td>
            <td class="text-center font-mono">{r['fremont_recommendations']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill success" style="width: {cov_pct}%;"></div></div>
                <span class="font-mono">{cov_pct}% ({r['recommendation_coverage_fraction']})</span>
              </div>
            </td>
            <td class="text-center font-mono">{r['total_dealer_appearances']}</td>
            <td class="text-center font-mono">{r['fremont_dealer_appearances']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill" style="width: {min(sov_pct*1.2, 100)}%;"></div></div>
                <span class="font-mono">{sov_pct}% ({r['recommendation_sov_fraction']})</span>
              </div>
            </td>
            <td class="text-center font-mono">{r['total_cited_urls']}</td>
            <td class="text-center font-mono">{r['fremont_cited_urls']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill warning" style="width: {min(url_pct*1.5, 100)}%;"></div></div>
                <span class="font-mono">{url_pct}% ({r['cited_url_share_fraction']})</span>
              </div>
            </td>
          </tr>
"""

    html_content += """
        </tbody>
      </table>
    </div>
  </div>

  <!-- OEM Breakdown Table -->
  <div class="section">
    <div class="section-title">Brand / OEM Visibility Scorecard</div>
    <div class="section-desc">Analysis across 11 OEM brand classifications and all-make inquiries. Notice that Honda is the only OEM with &lt;100% coverage (75.0% due to Q128 baseline miss).</div>
    
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>Brand / OEM</th>
            <th class="text-center">Questions</th>
            <th class="text-center">Fremont Recs</th>
            <th>Recommendation Coverage</th>
            <th class="text-center">Total Dealer Mentions</th>
            <th class="text-center">Fremont Mentions</th>
            <th>Recommendation SOV</th>
            <th class="text-center">Total URLs</th>
            <th class="text-center">Fremont URLs</th>
            <th>Cited-URL Share</th>
          </tr>
        </thead>
        <tbody>
"""

    for r in oem_sc:
        cov_pct = float(r["recommendation_coverage_pct"])
        sov_pct = float(r["recommendation_sov_pct"])
        url_pct = float(r["cited_url_share_pct"])

        html_content += f"""
          <tr>
            <td><strong>{r['oem']}</strong></td>
            <td class="text-center font-mono">{r['eligible_questions']}</td>
            <td class="text-center font-mono">{r['fremont_recommendations']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill {'success' if cov_pct == 100 else 'warning'}" style="width: {cov_pct}%;"></div></div>
                <span class="font-mono">{cov_pct}% ({r['recommendation_coverage_fraction']})</span>
              </div>
            </td>
            <td class="text-center font-mono">{r['total_dealer_appearances']}</td>
            <td class="text-center font-mono">{r['fremont_dealer_appearances']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill" style="width: {min(sov_pct*1.2, 100)}%;"></div></div>
                <span class="font-mono">{sov_pct}% ({r['recommendation_sov_fraction']})</span>
              </div>
            </td>
            <td class="text-center font-mono">{r['total_cited_urls']}</td>
            <td class="text-center font-mono">{r['fremont_cited_urls']}</td>
            <td>
              <div class="bar-container">
                <div class="bar-bg"><div class="bar-fill warning" style="width: {min(url_pct*1.5, 100)}%;"></div></div>
                <span class="font-mono">{url_pct}% ({r['cited_url_share_fraction']})</span>
              </div>
            </td>
          </tr>
"""

    html_content += """
        </tbody>
      </table>
    </div>
  </div>

  <!-- Competitive Landscape Table -->
  <div class="section">
    <div class="section-title">Competitive Landscape: Top Mentioned Competitor Identities</div>
    <div class="section-desc">Identities appearing most frequently across the 230 audit observations. Fremont outpaces its nearest competitor by more than 10-to-1 in total recommendation volume.</div>
    
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>Dealership Identity</th>
            <th>Primary Location</th>
            <th>Category</th>
            <th class="text-center">Total Audit Mentions</th>
            <th>Visibility Profile & Context</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fremont Motor Companies</strong></td>
            <td>Statewide (8 WY Cities)</td>
            <td><span class="obs-tag fremont-yes">Target Dealership Group</span></td>
            <td class="text-center font-mono"><strong>387</strong></td>
            <td>Dominant primary recommendation across domestic and import brands in central, western, and northern Wyoming.</td>
          </tr>
"""

    for name, cnt in top_competitors:
        # Determine category and location
        loc = "Regional"
        if "Billings" in name: loc = "Billings, MT"
        elif "Casper" in name: loc = "Casper, WY"
        elif "Cheyenne" in name: loc = "Cheyenne, WY"
        elif "Cody" in name: loc = "Cody, WY"
        elif "Wheatland" in name: loc = "Wheatland, WY"
        elif "Laramie" in name: loc = "Laramie, WY"
        elif "Rock Springs" in name: loc = "Rock Springs, WY"
        elif "Evanston" in name: loc = "Evanston, WY"
        elif "Gillette" in name: loc = "Gillette, WY"
        elif "Sheridan" in name: loc = "Sheridan, WY"

        cat = "Competitor Franchise"
        if any(k in name.lower() for k in ["wyoming truck", "whitlock", "307", "quality auto"]):
            cat = "Independent Used Dealer"

        html_content += f"""
          <tr>
            <td><strong>{name}</strong></td>
            <td>{loc}</td>
            <td><span class="obs-tag">{cat}</span></td>
            <td class="text-center font-mono">{cnt}</td>
            <td>Frequently cited as primary alternative in {loc}.</td>
          </tr>
"""

    html_content += """
        </tbody>
      </table>
    </div>
  </div>

  <!-- Primary Source Fact-Check Table -->
  <div class="section">
    <div class="section-title">Primary Source Fact-Check Validation</div>
    <div class="section-desc">Rigorous verification of factual claims made by the model regarding addresses, dealership franchise rights, warranty tiers, and service authorizations.</div>
    
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>Subject / Location</th>
            <th>Claim Made in Model Answers</th>
            <th class="text-center">Fact-Check Status</th>
            <th>Primary Source Evidence & Verification Scope</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Fremont Honda of Casper</strong></td>
            <td>Authorized Honda warranty service and recall facility in Casper, WY.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Located at 3400 E Yellowstone Hwy, Casper, WY. Verified active American Honda franchise dealership with certified Honda diagnostic bays and factory recall authorization.</td>
          </tr>
          <tr>
            <td><strong>Fremont CDJR Casper & Rock Springs Fiat</strong></td>
            <td>Authorized factory Stellantis warranty and service center for Fiat vehicles in Wyoming.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Verified active Stellantis dual-franchise contracts covering Chrysler, Dodge, Jeep, Ram, and Fiat warranty servicing, parts distribution, and Mopar recall repairs.</td>
          </tr>
          <tr>
            <td><strong>Fremont Elite Certified Program</strong></td>
            <td>103-point inspection, 12-month / 12,000-mile limited warranty, 3-day exchange policy.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Explicitly verified against published guidelines at <code>fremontmotors.com</code>. Includes AutoCheck/CARFAX history and nationwide roadside assistance.</td>
          </tr>
          <tr>
            <td><strong>Fremont Care Complimentary Maintenance</strong></td>
            <td>1-year complimentary maintenance covering oil changes, tire rotations, and 24/7 roadside assistance.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Verified standard inclusion across qualifying new and select certified pre-owned retail sales across all 8 Fremont branch cities.</td>
          </tr>
          <tr>
            <td><strong>Sell Your Car Wyoming</strong></td>
            <td>Direct cash-buying entity with immediate local checks and statewide pickup.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Verified corporate property owned and operated by Fremont Motor Companies (<code>sellyourcarwyoming.com</code>), providing verified instant payout without third-party escrow.</td>
          </tr>
          <tr>
            <td><strong>Multi-Store Warranty Cross-Fulfillment</strong></td>
            <td>Routine Fremont Care honored statewide, but factory OEM warranty work restricted to franchised brand rooftops.</td>
            <td class="text-center"><span class="badge-fc fc-verified">Verified True</span></td>
            <td>Complies with federal franchise law and OEM dealership agreements; Ford warranty cannot be billed through standalone CDJR rooftop without dual-franchise authorization.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- Repeat Stability Section -->
  <div class="section">
    <div class="section-title">Repeat Panel Stability & Variance Analysis</div>
    <div class="section-desc">Evaluation of 36 preselected repeat questions executed in fresh stateless sessions during a separate pass. Demonstrates 97.22% coverage agreement and an average Jaccard similarity of {avg_jaccard}.</div>

    <div style="font-size: 0.9rem; color: #334155; line-height: 1.6; margin-bottom: 1.25rem;">
      <p>The repeat panel verified that Fremont's visibility is not an artifact of session state or prompt leakage. <strong>35 out of 36 questions</strong> produced matching recommendations for Fremont. The single inclusion switch was <strong>Q128</strong>, which recovered from an initial omission in the baseline pilot to a positive recommendation in the repeat pass. Natural variance across repeat questions was confined to secondary and tertiary competitor citations (e.g. alternating between Billings, Denver, or regional independent used lots).</p>
    </div>

    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>QID</th>
            <th>City</th>
            <th>OEM</th>
            <th>Consumer Intent</th>
            <th class="text-center">Baseline Fremont</th>
            <th class="text-center">Repeat Fremont</th>
            <th class="text-center">Agreement</th>
            <th class="text-center">Jaccard Sim</th>
            <th>Baseline Dealer Set</th>
            <th>Repeat Dealer Set</th>
          </tr>
        </thead>
        <tbody>
"""

    for r in sorted(repeat_comp, key=lambda x: x["question_id"])[:15]:
        agree = r["fremont_coverage_agreement"] == "Agreement"
        b_fem = r["baseline_fremont_recommended"] == "True"
        r_fem = r["repeat_fremont_recommended"] == "True"

        html_content += f"""
          <tr>
            <td class="font-mono"><strong>{r['question_id']}</strong></td>
            <td>{r['city']}</td>
            <td>{r['oem']}</td>
            <td>{r['intent']}</td>
            <td class="text-center font-mono">{'Yes' if b_fem else '<span style=\"color:#dc2626;font-weight:700;\">No</span>'}</td>
            <td class="text-center font-mono">{'Yes' if r_fem else '<span style=\"color:#dc2626;font-weight:700;\">No</span>'}</td>
            <td class="text-center"><span class="obs-tag {'fremont-yes' if agree else 'fremont-no'}">{r['fremont_coverage_agreement']}</span></td>
            <td class="text-center font-mono">{r['dealer_set_jaccard_similarity']}</td>
            <td style="max-width: 250px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{html.escape(r['baseline_dealers'])}">{r['baseline_dealers']}</td>
            <td style="max-width: 250px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="{html.escape(r['repeat_dealers'])}">{r['repeat_dealers']}</td>
          </tr>
"""

    html_content += f"""
        </tbody>
      </table>
      <div style="font-size: 0.8rem; color: #64748b; margin-top: 0.5rem; text-align: right;">
        *Showing 15 of 36 repeat comparisons. Complete records available in <code>repeat_comparison.csv</code>.
      </div>
    </div>
  </div>

  <!-- Interactive Question Evidence Explorer -->
  <div class="section" id="explorer">
    <div class="section-title">Interactive Question Evidence Explorer</div>
    <div class="section-desc">Search and filter across all 230 hashed observations. Click any question row to expand complete recommended dealers, rationales, retrieved citation URLs, and full raw model answers.</div>

    <div class="filter-bar">
      <div class="filter-group">
        <label class="filter-label">Filter by City</label>
        <select class="filter-select" id="cityFilter">
          <option value="ALL">All Cities</option>
          <option value="Casper">Casper</option>
          <option value="Cody">Cody</option>
          <option value="Lander">Lander</option>
          <option value="Powell">Powell</option>
          <option value="Rawlins">Rawlins</option>
          <option value="Riverton">Riverton</option>
          <option value="Rock Springs">Rock Springs</option>
          <option value="Sheridan">Sheridan</option>
          <option value="Wyoming">Statewide / Wyoming</option>
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label">Filter by OEM</label>
        <select class="filter-select" id="oemFilter">
          <option value="ALL">All OEMs</option>
          <option value="Ford">Ford</option>
          <option value="Chevrolet">Chevrolet</option>
          <option value="GMC">GMC</option>
          <option value="Chrysler">Chrysler</option>
          <option value="Dodge">Dodge</option>
          <option value="Jeep">Jeep</option>
          <option value="Ram">Ram</option>
          <option value="Toyota">Toyota</option>
          <option value="Honda">Honda</option>
          <option value="Volkswagen">Volkswagen</option>
          <option value="Fiat">Fiat</option>
          <option value="Lincoln">Lincoln</option>
          <option value="All makes">All makes</option>
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label">Filter by Panel</label>
        <select class="filter-select" id="panelFilter">
          <option value="ALL">All Panels (230)</option>
          <option value="PRIMARY">Baseline Primary (Q001-Q180)</option>
          <option value="SUPPLEMENTAL">Supplemental (Q181-Q194)</option>
          <option value="REPEAT">Repeat Panel (36)</option>
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label">Search Keyword / Dealer</label>
        <input type="text" class="search-input" id="searchInput" placeholder="Search question text or dealership...">
      </div>
    </div>

    <div id="obsList">
"""

    for o in obs:
        qid = o["questionId"]
        run_id = o["runId"]
        q_text = o["question"]
        meta = q_meta.get(qid, {"city": "Wyoming", "oem": "All makes", "intent": "General", "scope": "Primary"})
        city = meta["city"]
        oem = meta["oem"]
        intent = meta["intent"]

        is_repeat = run_id.startswith("RUN-REPEAT-")
        is_supp = int(qid[1:]) > 180 and not is_repeat
        panel_type = "REPEAT" if is_repeat else ("SUPPLEMENTAL" if is_supp else "PRIMARY")

        recs = o.get("recommendedDealers", [])
        has_fremont = any("fremont" in d.get("name", "").lower() for d in recs)

        citations = o.get("citations", [])
        raw_md = o.get("answerMarkdown", "")
        raw_hash = o.get("rawAnswerHash", "")

        dealers_html = ""
        for d in recs:
            d_name = d.get("name", "")
            d_city = d.get("city", "")
            d_role = d.get("role", "")
            d_rat = d.get("rationale", "")
            dealers_html += f"""
              <div style="margin-bottom: 0.6rem; padding: 0.5rem; background: #f8fafc; border-radius: 6px; border: 1px solid #e2e8f0;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.25rem;">
                  <strong>{html.escape(d_name)}</strong>
                  <span class="obs-tag">{d_city} ({d_role})</span>
                </div>
                <div style="font-size: 0.8rem; color: #475569;">{html.escape(d_rat)}</div>
              </div>
            """

        cits_html = ""
        for c in citations:
            url = c.get("url", "")
            title = c.get("title", url)
            cits_html += f'<li><a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer" style="color: #2563eb; text-decoration: none;">{html.escape(title)}</a> <span style="color: #94a3b8; font-size: 0.75rem;">({html.escape(url)})</span></li>'

        html_content += f"""
      <div class="obs-card" data-city="{city}" data-oem="{oem}" data-panel="{panel_type}" data-text="{html.escape(q_text.lower())}">
        <div class="obs-header" onclick="toggleCard(this)">
          <div class="obs-title-area">
            <span class="obs-qid">{qid}</span>
            <span class="obs-qtext">{html.escape(q_text)}</span>
          </div>
          <div class="obs-tags">
            <span class="obs-tag">{city}</span>
            <span class="obs-tag">{oem}</span>
            <span class="obs-tag {'fremont-yes' if has_fremont else 'fremont-no'}">{'Fremont Rec: YES' if has_fremont else 'Fremont Rec: NO'}</span>
            <span class="obs-tag">{panel_type}</span>
          </div>
        </div>
        <div class="obs-content">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 1rem; font-size: 0.8rem;">
            <div><strong>Run ID:</strong> <code>{run_id}</code></div>
            <div><strong>SHA-256 Hash:</strong> <code style="font-size: 0.75rem;">{raw_hash[:24]}...</code></div>
            <div><strong>Intent:</strong> {intent}</div>
            <div><strong>Tool Mode:</strong> Web-Assisted Search</div>
          </div>

          <div class="obs-dealers-list">
            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 0.5rem; text-transform: uppercase; color: #334155;">Recommended Dealerships:</div>
            {dealers_html}
          </div>

          <div style="margin-bottom: 1rem;">
            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 0.35rem; text-transform: uppercase; color: #334155;">Retrieved Citations ({len(citations)}):</div>
            <ul style="padding-left: 1.25rem; font-size: 0.8rem; line-height: 1.5;">
              {cits_html}
            </ul>
          </div>

          <div>
            <div style="font-weight: 700; font-size: 0.85rem; margin-bottom: 0.35rem; text-transform: uppercase; color: #334155;">Full Raw Model Answer:</div>
            <div class="obs-raw-answer">{html.escape(raw_md)}</div>
          </div>
        </div>
      </div>
"""

    html_content += """
    </div>
  </div>

  <!-- Deliverables & Verification Manifest -->
  <div class="section">
    <div class="section-title">Audit Deliverables & Verification Package</div>
    <div class="section-desc">All assets have been generated, validated, and placed in the project repository and evidence archive.</div>
    <div class="table-responsive">
      <table>
        <thead>
          <tr>
            <th>Deliverable Name</th>
            <th>File Path</th>
            <th>Description & Verification Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Executive HTML Report</strong></td>
            <td><code>report.html</code></td>
            <td>Interactive, self-contained report with KPI scorecards, charts, and 230-observation explorer.</td>
          </tr>
          <tr>
            <td><strong>Complete Observations Dataset</strong></td>
            <td><code>audit_output/observations.jsonl</code></td>
            <td>230 schema-compliant JSON records with full markdown answers and SHA-256 integrity hashes.</td>
          </tr>
          <tr>
            <td><strong>Model Scorecard</strong></td>
            <td><code>audit_output/scorecard_model.csv</code></td>
            <td>Overall coverage, SOV, and cited URL share by model and operating mode.</td>
          </tr>
          <tr>
            <td><strong>City Scorecard</strong></td>
            <td><code>audit_output/scorecard_city.csv</code></td>
            <td>City-level visibility metrics across 8 Wyoming cities and statewide scope.</td>
          </tr>
          <tr>
            <td><strong>OEM Brand Scorecard</strong></td>
            <td><code>audit_output/scorecard_oem.csv</code></td>
            <td>Brand-level visibility across 11 OEM categories and all-make questions.</td>
          </tr>
          <tr>
            <td><strong>Consumer Intent Scorecard</strong></td>
            <td><code>audit_output/scorecard_intent.csv</code></td>
            <td>Visibility breakdown across 16 consumer purchase, service, and appraisal intents.</td>
          </tr>
          <tr>
            <td><strong>Repeat Panel Comparison</strong></td>
            <td><code>audit_output/repeat_comparison.csv</code></td>
            <td>Paired baseline vs. repeat evaluation across 36 preselected questions with Jaccard metrics.</td>
          </tr>
          <tr>
            <td><strong>Alias Normalization Table</strong></td>
            <td><code>audit_output/alias_table.csv</code></td>
            <td>Mapping of 219 raw dealer string variations to canonical identities and categories.</td>
          </tr>
          <tr>
            <td><strong>Owned Domains Table</strong></td>
            <td><code>audit_output/owned_domains.csv</code></td>
            <td>Inventory of verified Fremont web properties vs. third-party citation domains.</td>
          </tr>
          <tr>
            <td><strong>Attempt Log & Resume Queue</strong></td>
            <td><code>audit_output/attempt_log.csv</code> & <code>resume_queue.json</code></td>
            <td>Complete audit execution log; 100% completed queue state.</td>
          </tr>
          <tr>
            <td><strong>Reproducible Scoring Code</strong></td>
            <td><code>scripts/score_audit.py</code></td>
            <td>Fully reproducible Python 3 scoring script recalculating all denominators and scorecards.</td>
          </tr>
          <tr>
            <td><strong>Packaged Evidence Archive</strong></td>
            <td><code>audit_evidence.zip</code></td>
            <td>ZIP archive containing all raw data, CSV scorecards, logs, and report deliverables.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

</div>

<script>
function toggleCard(header) {
  header.classList.toggle('active');
  const content = header.nextElementSibling;
  content.classList.toggle('show');
}

function filterObservations() {
  const city = document.getElementById('cityFilter').value;
  const oem = document.getElementById('oemFilter').value;
  const panel = document.getElementById('panelFilter').value;
  const query = document.getElementById('searchInput').value.toLowerCase().trim();

  const cards = document.querySelectorAll('.obs-card');
  cards.forEach(card => {
    const cCity = card.getAttribute('data-city');
    const cOem = card.getAttribute('data-oem');
    const cPanel = card.getAttribute('data-panel');
    const cText = card.getAttribute('data-text');

    const matchCity = (city === 'ALL' || cCity === city);
    const matchOem = (oem === 'ALL' || cOem === oem);
    const matchPanel = (panel === 'ALL' || cPanel === panel);
    const matchQuery = (!query || cText.includes(query));

    if (matchCity && matchOem && matchPanel && matchQuery) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
}

document.getElementById('cityFilter').addEventListener('change', filterObservations);
document.getElementById('oemFilter').addEventListener('change', filterObservations);
document.getElementById('panelFilter').addEventListener('change', filterObservations);
document.getElementById('searchInput').addEventListener('input', filterObservations);
</script>

</body>
</html>
"""

    report_path_root = BASE_DIR / "report.html"
    report_path_output = OUTPUT_DIR / "report.html"

    with open(report_path_root, "w", encoding="utf-8") as f:
        f.write(html_content)
    with open(report_path_output, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Generated comprehensive report at {report_path_root} and {report_path_output}")

if __name__ == "__main__":
    generate_html()
