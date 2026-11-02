"""
Houlihan Lokey Technology Group — Sponsor LBO Model & Returns Engine
Computes 5-Year Sponsor Returns (IRR & MoIC) under varying exit multiples and leverage structures.
Author: Bhupesh Chandra Dimri
"""

import numpy as np
import pandas as pd


def run_sponsor_lbo(target: dict, entry_ev_multiple: float = 7.5, debt_leverage_ebitda: float = 4.5, exit_ev_multiple: float = 7.5) -> dict:
    """
    Simulates a 5-year Financial Sponsor LBO of Project Apex.
    - Entry Enterprise Value = Entry Multiple * ARR
    - Debt Financing = Leverage * LTM EBITDA
    - Sponsor Equity Check = Entry EV + Net Debt + Fees - Total Debt
    """
    entry_ev = target["arr_m"] * entry_ev_multiple
    transaction_fees = 15.0  # M&A advisory, legal, debt financing fees
    initial_debt = target["ltm_ebitda_m"] * debt_leverage_ebitda
    sponsor_equity = entry_ev + target["net_debt_m"] + transaction_fees - initial_debt

    # 5-Year Operating Forecast (EBITDA growth)
    ebitda_0 = target["ltm_ebitda_m"]
    ebitda_growth_rates = [0.28, 0.24, 0.20, 0.16, 0.14]
    current_ebitda = ebitda_0

    debt_balance = initial_debt
    interest_rate = 0.085  # SOFR + 350 bps
    tax_rate = 0.25

    annual_fcf_for_debt_paydown = []

    for g in ebitda_growth_rates:
        current_ebitda *= (1 + g)
        interest_exp = debt_balance * interest_rate
        ebt = current_ebitda - interest_exp - (current_ebitda * 0.10)  # D&A ~ 10%
        taxes = max(0, ebt * tax_rate)
        # FCF for sweep = EBITDA - Interest - Taxes - CapEx/NWC
        fcf_sweep = current_ebitda - interest_exp - taxes - (current_ebitda * 0.12)
        debt_paydown = min(debt_balance, max(0, fcf_sweep * 0.85))  # 85% cash sweep
        debt_balance -= debt_paydown
        annual_fcf_for_debt_paydown.append(round(debt_paydown, 1))

    exit_ebitda = current_ebitda
    # In software LBOs, exit EV is often benchmarked to ARR or EBITDA
    exit_arr = target["arr_m"] * 2.3  # projected 2.3x ARR expansion over 5 years
    exit_ev = exit_arr * exit_ev_multiple
    exit_equity_value = exit_ev - debt_balance

    moic = exit_equity_value / sponsor_equity
    irr = (moic ** (1.0 / 5.0)) - 1.0

    return {
        "entry_ev_m": round(entry_ev, 1),
        "sponsor_equity_m": round(sponsor_equity, 1),
        "initial_debt_m": round(initial_debt, 1),
        "ending_debt_m": round(debt_balance, 1),
        "exit_ev_m": round(exit_ev, 1),
        "exit_equity_m": round(exit_equity_value, 1),
        "moic": round(moic, 2),
        "irr_pct": round(irr * 100, 1),
    }


def generate_lbo_sensitivity_table(target: dict) -> pd.DataFrame:
    """Builds a 3x3 sensitivity matrix of Exit Multiple vs. Leverage on Sponsor IRR."""
    exit_multiples = [6.5, 7.5, 8.5]
    leverages = [4.0, 4.5, 5.0]

    matrix_rows = []
    for lev in leverages:
        row = {"Leverage (x EBITDA)": f"{lev:.1f}x"}
        for mult in exit_multiples:
            res = run_sponsor_lbo(target, entry_ev_multiple=7.5, debt_leverage_ebitda=lev, exit_ev_multiple=mult)
            row[f"Exit {mult:.1f}x ARR"] = f"{res['irr_pct']:.1f}% ({res['moic']:.2f}x)"
        matrix_rows.append(row)

    return pd.DataFrame(matrix_rows)

