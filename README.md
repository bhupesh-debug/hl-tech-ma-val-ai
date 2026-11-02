# HL-TechMA-ValAI: Houlihan Lokey Technology M&A Valuation, SaaS Operating Benchmark & LBO Return Engine

> **One-Liner**: An institutional Tech M&A financial engineering platform purpose-built for **Houlihan Lokey's Technology Group (#1 Global M&A Advisor)** to automate 3-statement SaaS projections, Trading & Precedent M&A comps, Unlevered DCF with Monte Carlo sensitivity, and 5-year Sponsor LBO returns across Software & Digital Media targets.

- **Author**: Bhupesh Chandra Dimri (`M.S. Accounting Analytics & Data Technology, Pace University — Beta Alpha Psi | F-1 STEM OPT`)
- **Target Role**: Senior Analyst — Corporate Finance, Technology Group (Software & Digital Media), Houlihan Lokey, Inc.
- **Repository**: [https://github.com/bhupesh-debug/hl-tech-ma-val-ai](https://github.com/bhupesh-debug/hl-tech-ma-val-ai)

---

## 1. Business Problem & Houlihan Lokey Technology Group Mandate
Houlihan Lokey's Technology Group is the **No. 1 technology M&A advisor globally by transaction count**. Covering high-growth and sponsor-backed Software & Digital Media companies requires rapid, error-free valuation analysis across fast transaction timelines:
1. **Dynamic SaaS Unit Economics Modeling**: Evaluating targets across Annual Recurring Revenue (ARR), Net Retention Rate (NRR), Gross Margins, Rule of 40 (Growth % + FCF Margin %), and CAC Payback.
2. **Multi-Method M&A Valuation Triangulation**: Synthesizing Public Comps (EV/ARR, EV/NTM Rev), Precedent M&A Transactions, and Unlevered DCF into an executive Valuation Football Field for sell-side CIMs and pitchbooks.
3. **Financial Sponsor LBO & Debt Capacity Structuring**: Stress-testing target debt capacity (Senior Secured Term Loan + Mezzanine) and sponsor exit returns (5-year IRR and MoIC) across multiple exit multiple expansion/contraction scenarios.

---

## 2. Technical & Quantitative Architecture
1. **Module 1: Integrated 3-Statement & SaaS Operating Model (`src/saas_operating_model.py`)**:
   - 5-year monthly and annual driver-based projections tied to ARR waterfalls, churn, deferred revenue, and operating expense leverage.
2. **Module 2: Automated Comps & Valuation Football Field Engine (`src/valuation_engine.py`)**:
   - Public trading comps + precedent transaction benchmarking across 50 software peers, deriving 25th, Median, and 75th percentile valuation ranges and WACC-sensitized DCF.
3. **Module 3: Sponsor LBO Return & Debt Schedule Model (`src/lbo_engine.py`)**:
   - 5-year dynamic debt paydown, cash sweep, exit enterprise value decomposition, and Sponsor IRR / MoIC returns.
4. **Module 4: Executive Pitchbook & Evaluation Runner (`src/evaluate.py`)**:
   - Compiles transaction summaries, football field tables, and generates the empirical model report.

---

## 3. Repository Structure
```text
ml-project-hl-tech-ma/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── synthetic/              # 50-peer Software & Digital Media comps panel
├── src/
│   ├── data_pipeline.py        # Peer financial comps & target financial generator
│   ├── saas_operating_model.py # 3-statement integrated driver-based model
│   ├── valuation_engine.py     # DCF, Trading Comps & Football Field generator
│   ├── lbo_engine.py           # 5-year Sponsor LBO returns & debt sweep
│   ├── evaluate.py             # Valuation output & pitchbook tables
│   └── generate_pdf_playbook.py# 4-page executive PDF deliverable builder
└── reports/
    ├── model_report.md         # Valuation summary & sensitivity tables
    └── Houlihan_Lokey_Tech_Senior_Analyst_Mastery_Playbook.pdf
```

## 4. Quick Start
```bash
pip install -r requirements.txt
python src/data_pipeline.py
python src/evaluate.py
```
