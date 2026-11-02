"""
Houlihan Lokey Technology Group — Valuation Engine (Trading Comps, DCF & Football Field)
Author: Bhupesh Chandra Dimri
"""

import numpy as np
import pandas as pd


def build_dcf_model(target: dict, wacc: float = 0.105, lt_growth: float = 0.03) -> dict:
    """
    Builds a 5-year Unlevered Free Cash Flow (UFCF) DCF model.
    Years: 2027E, 2028E, 2029E, 2030E, 2031E
    """
    rev_0 = target["ltm_revenue_m"]
    growth_rates = [0.24, 0.20, 0.17, 0.14, 0.12]
    ebit_margins = [0.18, 0.21, 0.23, 0.25, 0.26]
    tax_rate = 0.25
    reinvestment_rate_pct = 0.04  # CapEx + NWC % of revenue

    projected_rev = []
    projected_ufcf = []
    pv_ufcf = []

    current_rev = rev_0
    for i, (g, m) in enumerate(zip(growth_rates, ebit_margins)):
        current_rev *= (1 + g)
        ebit = current_rev * m
        nopat = ebit * (1 - tax_rate)
        # UFCF = NOPAT - Net CapEx/NWC reinvestment
        ufcf = nopat - (current_rev * reinvestment_rate_pct)
        discount_factor = 1.0 / ((1 + wacc) ** (i + 0.5))  # Mid-year convention

        projected_rev.append(round(current_rev, 1))
        projected_ufcf.append(round(ufcf, 1))
        pv_ufcf.append(round(ufcf * discount_factor, 1))

    sum_pv_ufcf = sum(pv_ufcf)
    terminal_ufcf = projected_ufcf[-1] * (1 + lt_growth)
    terminal_value = terminal_ufcf / (wacc - lt_growth)
    pv_terminal_value = terminal_value / ((1 + wacc) ** len(growth_rates))

    enterprise_value = sum_pv_ufcf + pv_terminal_value
    equity_value = enterprise_value - target["net_debt_m"]

    return {
        "sum_pv_ufcf": round(sum_pv_ufcf, 1),
        "terminal_value": round(terminal_value, 1),
        "pv_terminal_value": round(pv_terminal_value, 1),
        "enterprise_value": round(enterprise_value, 1),
        "equity_value": round(equity_value, 1),
        "projected_revenues": projected_rev,
        "projected_ufcf": projected_ufcf,
    }


def compute_valuation_football_field(comps_df: pd.DataFrame, target: dict) -> pd.DataFrame:
    """
    Computes 25th, Median, and 75th percentile valuation ranges across:
    1. Public Trading Comps (EV / NTM Revenue)
    2. Public Trading Comps (EV / NTM EBITDA)
    3. Precedent M&A Transactions (EV / ARR)
    4. Unlevered DCF Analysis (WACC 9.5% - 11.5%)
    """
    # 1. Trading Comps - NTM Rev
    p25_arr = comps_df["ev_arr_multiple"].quantile(0.25)
    med_arr = comps_df["ev_arr_multiple"].median()
    p75_arr = comps_df["ev_arr_multiple"].quantile(0.75)

    # Precedent M&A typically carries 15-20% control premium over public comps
    mna_p25_arr = p25_arr * 1.15
    mna_med_arr = med_arr * 1.18
    mna_p75_arr = p75_arr * 1.20

    # 2. Trading Comps - EBITDA
    p25_ebitda = comps_df["ev_ebitda_multiple"].quantile(0.25)
    med_ebitda = comps_df["ev_ebitda_multiple"].median()
    p75_ebitda = comps_df["ev_ebitda_multiple"].quantile(0.75)

    # 3. DCF Scenarios
    dcf_low = build_dcf_model(target, wacc=0.115, lt_growth=0.025)["enterprise_value"]
    dcf_base = build_dcf_model(target, wacc=0.105, lt_growth=0.030)["enterprise_value"]
    dcf_high = build_dcf_model(target, wacc=0.095, lt_growth=0.035)["enterprise_value"]

    football_field = [
        {
            "Methodology": "Public Trading Comps (EV / ARR)",
            "Metric Base ($M)": target["arr_m"],
            "Multiple Range": f"{p25_arr:.1f}x - {p75_arr:.1f}x (Med: {med_arr:.1f}x)",
            "Low EV ($M)": round(target["arr_m"] * p25_arr, 1),
            "Median EV ($M)": round(target["arr_m"] * med_arr, 1),
            "High EV ($M)": round(target["arr_m"] * p75_arr, 1),
        },
        {
            "Methodology": "Precedent Tech M&A Transactions",
            "Metric Base ($M)": target["arr_m"],
            "Multiple Range": f"{mna_p25_arr:.1f}x - {mna_p75_arr:.1f}x (Med: {mna_med_arr:.1f}x)",
            "Low EV ($M)": round(target["arr_m"] * mna_p25_arr, 1),
            "Median EV ($M)": round(target["arr_m"] * mna_med_arr, 1),
            "High EV ($M)": round(target["arr_m"] * mna_p75_arr, 1),
        },
        {
            "Methodology": "Public Comps (EV / NTM EBITDA)",
            "Metric Base ($M)": target["ntm_ebitda_m"],
            "Multiple Range": f"{p25_ebitda:.1f}x - {p75_ebitda:.1f}x (Med: {med_ebitda:.1f}x)",
            "Low EV ($M)": round(target["ntm_ebitda_m"] * p25_ebitda, 1),
            "Median EV ($M)": round(target["ntm_ebitda_m"] * med_ebitda, 1),
            "High EV ($M)": round(target["ntm_ebitda_m"] * p75_ebitda, 1),
        },
        {
            "Methodology": "Unlevered DCF Analysis (WACC 9.5-11.5%)",
            "Metric Base ($M)": target["ltm_revenue_m"],
            "Multiple Range": "g: 2.5% - 3.5% | WACC: 9.5% - 11.5%",
            "Low EV ($M)": round(dcf_low, 1),
            "Median EV ($M)": round(dcf_base, 1),
            "High EV ($M)": round(dcf_high, 1),
        },
    ]

    return pd.DataFrame(football_field)

