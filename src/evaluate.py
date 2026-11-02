"""
Houlihan Lokey Technology Group — End-to-End Evaluation & M&A Pitchbook Table Runner
Author: Bhupesh Chandra Dimri
"""

import os
from data_pipeline import generate_software_comps, get_target_company_profile
from lbo_engine import generate_lbo_sensitivity_table, run_sponsor_lbo
from valuation_engine import build_dcf_model, compute_valuation_football_field
import pandas as pd


def run_evaluation():
    comps_df = generate_software_comps(n_peers=50, seed=42)
    target = get_target_company_profile()

    dcf_res = build_dcf_model(target)
    ff_df = compute_valuation_football_field(comps_df, target)
    lbo_base = run_sponsor_lbo(target)
    lbo_sens = generate_lbo_sensitivity_table(target)

    print("=== 1. HOULIHAN LOKEY TECH M&A VALUATION FOOTBALL FIELD ===")
    print(ff_df.to_string(index=False))

    print("\n=== 2. UNLEVERED DCF SUMMARY (PROJECT APEX) ===")
    print(f"PV of 5-Year UFCF: ${dcf_res['sum_pv_ufcf']}M")
    print(f"PV of Terminal Value (WACC 10.5%, g 3.0%): ${dcf_res['pv_terminal_value']}M")
    print(f"Implied Enterprise Value: ${dcf_res['enterprise_value']}M")
    print(f"Implied Equity Value (less $12M Net Debt): ${dcf_res['equity_value']}M")

    print("\n=== 3. FINANCIAL SPONSOR LBO RETURNS (BASE CASE) ===")
    print(f"Entry Enterprise Value (7.5x ARR): ${lbo_base['entry_ev_m']}M")
    print(f"Sponsor Equity Check: ${lbo_base['sponsor_equity_m']}M")
    print(f"Initial Debt: ${lbo_base['initial_debt_m']}M | Ending Debt: ${lbo_base['ending_debt_m']}M")
    print(f"5-Year Exit Equity Value: ${lbo_base['exit_equity_m']}M")
    print(f"Sponsor MoIC: {lbo_base['moic']}x | 5-Year Net IRR: {lbo_base['irr_pct']}%")

    print("\n=== 4. LBO SENSITIVITY TABLE (LEVERAGE VS. EXIT MULTIPLE) ===")
    print(lbo_sens.to_string(index=False))

    rep_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
    os.makedirs(rep_dir, exist_ok=True)
    report_path = os.path.join(rep_dir, "model_report.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Houlihan Lokey Technology Group — Project Apex M&A Valuation & LBO Report\n\n")
        f.write("## 1. Valuation Football Field Summary\n\n")
        f.write(ff_df.to_markdown(index=False) + "\n\n")
        f.write("## 2. Unlevered Discounted Cash Flow (DCF)\n\n")
        f.write(f"- **PV of 5-Year Cash Flows**: `${dcf_res['sum_pv_ufcf']}M`\n")
        f.write(f"- **PV of Terminal Value**: `${dcf_res['pv_terminal_value']}M`\n")
        f.write(f"- **Implied Enterprise Value**: `${dcf_res['enterprise_value']}M`\n")
        f.write(f"- **Implied Equity Value**: `${dcf_res['equity_value']}M`\n\n")
        f.write("## 3. Financial Sponsor LBO Sensitivity Matrix\n\n")
        f.write(lbo_sens.to_markdown(index=False) + "\n")

    print(f"\n[OK] Saved M&A report to {report_path}")


if __name__ == "__main__":
    run_evaluation()

