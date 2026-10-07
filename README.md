# Fremont Motor Companies — AI Dealership Visibility Audit (2026)

**Executive Report & Measured Evidence:**  
👉 **[View Live Interactive Audit Report](https://fremont-web.github.io/ai-visibility-audit-2026/)**  
📦 **[Download Complete Evidence Archive (.zip)](./audit_evidence.zip)**

---

## Executive Summary

This repository contains the complete, reproducible dataset and interactive executive report for the **2026 AI Dealership Visibility Audit** evaluating **Fremont Motor Companies** across text AI models in Wyoming.

### Key Measured Benchmarks

| Metric | Score / Result | Fraction / Details |
| :--- | :---: | :--- |
| **Primary Recommendation Coverage** | **99.44%** | **179 of 180** primary questions recommended Fremont |
| **Recommendation Share of Voice (SOV)** | **34.10%** | **179 of 525** total named dealership appearances across Wyoming |
| **Cited-URL Domain Share** | **33.02%** | **320 of 969** web citations were verified Fremont-owned domains |
| **Repeat Stability Agreement** | **97.22%** | **35 of 36** paired repeat questions produced matching recommendations |
| **Integrity & Execution Audit** | **100% Completed** | **230 of 230** scheduled runs completed, validated, and SHA-256 hashed |

---

## Repository Structure & Deliverables

- [`index.html`](./index.html) / [`report.html`](./report.html): Full interactive executive report with KPI cards, competitive landscape breakdowns, fact-check validation tables, and a searchable 230-question evidence explorer.
- [`audit_evidence.zip`](./audit_evidence.zip): Packaged standalone archive containing all report assets, raw markdown answers, and CSV scorecards.
- **Scorecard CSVs**:
  - [`scorecard_model.csv`](./scorecard_model.csv): Overall coverage, SOV, and cited-URL metrics.
  - [`scorecard_city.csv`](./scorecard_city.csv): Visibility breakdown across Casper, Cody, Lander, Powell, Rawlins, Riverton, Rock Springs, Sheridan, and Statewide.
  - [`scorecard_oem.csv`](./scorecard_oem.csv): Visibility across Ford, CDJR, Chevrolet, GMC, Toyota, Honda, VW, and All-Makes.
  - [`scorecard_intent.csv`](./scorecard_intent.csv): Breakdown across 16 consumer purchase, service, warranty, and trade-in intents.
- **Verification & Audit Tables**:
  - [`repeat_comparison.csv`](./repeat_comparison.csv): 36-question paired baseline vs. repeat stability analysis.
  - [`alias_table.csv`](./alias_table.csv): 219 raw dealer name strings mapped to canonical identities and categories.
  - [`owned_domains.csv`](./owned_domains.csv): 18 verified Fremont domains and citation frequencies.
  - [`attempt_log.csv`](./attempt_log.csv): Execution log for all 230 attempts.
  - [`manifest.json`](./manifest.json): Audit controller parameters, model labels, and isolation controls.
- **Reproducible Scoring Code**:
  - [`scripts/score_audit.py`](./scripts/score_audit.py): Python scoring engine.
  - [`scripts/generate_report.py`](./scripts/generate_report.py): Executive HTML generator.

---

## Top 5 Practical Action Items for Leadership

1. **Deploy Casper Honda Recall & Warranty Schema**: Optimize `fremonthondaofcasper.com` with explicit `AutomotiveBusiness` schema to eliminate search leakage to Cheyenne on warranty queries (Ref: Q128).
2. **Clarify Fiat Dual-Franchise Authorization**: Add a dedicated Fiat & Mopar certified warranty/service FAQ to Casper and Rock Springs CDJR websites to prevent consumer defection to Denver and Salt Lake City (Ref: Q181–Q188).
3. **Publish "Fremont Elite" vs OEM CPO Comparison**: Structure an interactive comparison hub contrasting dealer-backed Fremont Elite (103-point) with factory CPO programs to capture organic search and AI overview grounding.
4. **Unify "Sell Your Car Wyoming" Entity Authority**: Implement JSON-LD `sameAs` schema linking `sellyourcarwyoming.com` to Fremont Motor Companies and emphasize instant in-person Wyoming payment.
5. **Launch Statewide Warranty & Recall Routing Guide**: Publish a consumer-facing tool explaining where each vehicle brand's factory recalls are authorized within the 8 Fremont city network.
