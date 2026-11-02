"""
Houlihan Lokey Technology Group — Target & Software Comps Data Pipeline
Simulates SaaS operating metrics and 50 public & precedent transaction peers.
Author: Bhupesh Chandra Dimri
"""

import os
import numpy as np
import pandas as pd


def generate_software_comps(n_peers: int = 50, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    subsectors = rng.choice(
        ["Vertical SaaS", "PropTech", "Supply Chain Software", "EdTech", "HCM Software", "Digital Media / AdTech"],
        size=n_peers,
    )

    arr_m = np.round(rng.uniform(75, 850, size=n_peers), 1)
    rev_growth_pct = np.round(rng.uniform(12, 45, size=n_peers), 1)
    nrr_pct = np.round(rng.uniform(102, 128, size=n_peers), 1)
    gross_margin_pct = np.round(rng.uniform(68, 86, size=n_peers), 1)
    fcf_margin_pct = np.round(rng.uniform(-5, 28, size=n_peers), 1)
    rule_of_40 = rev_growth_pct + fcf_margin_pct

    # Valuation multiples correlated with Rule of 40 and NRR
    ev_arr_multiple = np.round(np.clip(3.5 + 0.12 * rule_of_40 + 0.08 * (nrr_pct - 100) + rng.normal(0, 0.8, n_peers), 3.0, 14.5), 1)
    ev_ebitda_multiple = np.round(np.clip(14.0 + 0.35 * fcf_margin_pct + rng.normal(0, 2.5, n_peers), 12.0, 32.0), 1)

    df = pd.DataFrame({
        "ticker": [f"SW-{i:02d}" for i in range(1, n_peers + 1)],
        "company_name": [f"TechPeer-{i:02d}" for i in range(1, n_peers + 1)],
        "subsector": subsectors,
        "arr_usd_m": arr_m,
        "rev_growth_pct": rev_growth_pct,
        "nrr_pct": nrr_pct,
        "gross_margin_pct": gross_margin_pct,
        "fcf_margin_pct": fcf_margin_pct,
        "rule_of_40_pct": rule_of_40,
        "ev_arr_multiple": ev_arr_multiple,
        "ev_ebitda_multiple": ev_ebitda_multiple,
    })
    return df


def get_target_company_profile() -> dict:
    """Returns baseline financials for our target SaaS M&A sell-side mandate: Project Apex (Supply Chain SaaS)."""
    return {
        "name": "Project Apex (Enterprise Supply Chain SaaS)",
        "ltm_revenue_m": 85.0,
        "ntm_revenue_m": 105.0,
        "arr_m": 92.0,
        "arr_growth_pct": 26.5,
        "nrr_pct": 118.0,
        "gross_margin_pct": 78.5,
        "ltm_ebitda_m": 18.5,
        "ntm_ebitda_m": 25.0,
        "fcf_margin_pct": 18.0,
        "rule_of_40": 44.5,
        "net_debt_m": 12.0,
    }


if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "synthetic")
    os.makedirs(out_dir, exist_ok=True)
    comps_df = generate_software_comps(n_peers=50)
    comps_path = os.path.join(out_dir, "software_comps_universe.csv")
    comps_df.to_csv(comps_path, index=False)
    print(f"[OK] Saved 50 comps to {comps_path}")
    print(comps_df.head(5).to_string(index=False))
