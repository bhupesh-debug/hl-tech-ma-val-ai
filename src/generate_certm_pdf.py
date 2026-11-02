"""
Generates the Executive 4-Page PDF Deliverable for certM:
Senior Analyst Mastery Coach — Software & Digital Media Investment Banking
Houlihan Lokey Technology Group (#1 Global Technology M&A Advisor)
Includes complete Diagnostic Exercise, Answer Key, Model Review Rubric, and Banker Critique.
Author: Bhupesh Chandra Dimri
"""

import os
import subprocess
import sys

try:
    import reportlab
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


def build_certm_pdf(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.50 * inch,
        bottomMargin=0.50 * inch,
        title="certM: Senior Analyst Mastery Coach — Houlihan Lokey Software & Digital Media",
        author="Bhupesh Chandra Dimri",
    )

    styles = getSampleStyleSheet()
    hl_navy = colors.HexColor("#0A192F")
    hl_gold = colors.HexColor("#C5A059")
    slate = colors.HexColor("#1E293B")
    light_bg = colors.HexColor("#F8FAFC")
    border_col = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=hl_navy, spaceAfter=3)
    subtitle_style = ParagraphStyle("DocSub", fontName="Helvetica-Bold", fontSize=9.5, leading=13, textColor=hl_gold, spaceAfter=6)
    h1_style = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=hl_navy, spaceBefore=8, spaceAfter=3)
    h2_style = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=hl_gold, spaceBefore=5, spaceAfter=2)
    body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=8.8, leading=11.8, textColor=slate, spaceAfter=3)
    bullet_style = ParagraphStyle("Bullet", parent=body_style, leftIndent=10, firstLineIndent=-7, spaceAfter=2.5)
    cell_style = ParagraphStyle("Cell", parent=body_style, fontSize=8.0, leading=10.5, spaceAfter=0)
    cell_bold = ParagraphStyle("CellBold", parent=cell_style, fontName="Helvetica-Bold", textColor=colors.white)

    def make_table(data, col_widths):
        formatted = []
        for r_idx, row in enumerate(data):
            formatted_row = []
            for item in row:
                st = cell_bold if r_idx == 0 else cell_style
                formatted_row.append(Paragraph(str(item), st))
            formatted.append(formatted_row)
        t = Table(formatted, colWidths=col_widths, repeatRows=1)
        t.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), hl_navy),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, light_bg]),
                    ("GRID", (0, 0), (-1, -1), 0.5, border_col),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
        return t

    story = []

    # PAGE 1: OVERVIEW & STANDARDS
    story.append(Paragraph("CERTM: SENIOR ANALYST MASTERY COACH — TECH M&amp;A", title_style))
    story.append(Paragraph("Houlihan Lokey Software &amp; Digital Media Investment Banking Franchise (#1 Global Technology M&amp;A Advisor)", subtitle_style))
    story.append(Paragraph("<b>Author &amp; Candidate:</b> Bhupesh Chandra Dimri (M.S. Accounting Analytics, Pace University | F-1 STEM OPT) &nbsp;|&nbsp; <b>HL Track Record:</b> 128 Deals in 2025 (LSEG #1 Rank)", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=hl_navy, spaceBefore=1, spaceAfter=5))

    story.append(Paragraph("1. THE HOULIHAN LOKEY WORK PRODUCT STANDARD", h1_style))
    story.append(Paragraph("• <b>The Lean Deal Team Reality:</b> Houlihan Lokey's Technology Group is the <b>No. 1 technology M&amp;A advisor globally based on number of transactions (128 deals in 2025 based on LSEG data)</b>. Deal teams operate leanly (Managing Director, Director/VP, Associate, Senior Analyst). Senior bankers expect accurate, board-ready work with minimal supervision.", bullet_style))
    story.append(Paragraph("• <b>The 5 Pillars of Model Defensibility:</b><br/>"
                           "1. <b>Numerically Correct &amp; Auditable:</b> Zero formula errors (#REF!, #VALUE!), no unexplained plugs, and transparent formulas.<br/>"
                           "2. <b>Dynamic &amp; Non-Circular:</b> Hardcoded historicals in blue font (#0000FF), formulas in black (#000000), dynamic assumptions, and zero hardcoded outputs.<br/>"
                           "3. <b>Board &amp; Client-Ready:</b> Professional executive formatting, consistent units ($M vs. $K vs. bps), and clean alignments.<br/>"
                           "4. <b>Transaction Speed:</b> Capable of turning around buyer diligence requests, VDR Q&amp;A, and multiple sensitivities under tight auction deadlines.<br/>"
                           "5. <b>Commercially Decisive:</b> Every analysis must lead with a clear strategic conclusion for the Managing Director or client board.", bullet_style))

    story.append(Paragraph("2. CORE SENIOR ANALYST RESPONSIBILITY SPECTRUM", h1_style))
    resp_data = [
        ["Core Responsibility", "Key Methodologies &amp; Tools", "Senior Banker Standards &amp; Review Focus"],
        [
            "<b>1. M&amp;A Transaction Execution</b>",
            "Sell-side/buy-side M&amp;A, equity/debt raises, CIMs, VDR management, process trackers, bid matrices.",
            "Zero errors in CIM financial tables; 100% data room audit defensibility; rapid diligence turnaround.",
        ],
        [
            "<b>2. Dynamic Financial Modeling</b>",
            "3-statement integrated forecasts, SaaS revenue builds, DCF, Trading Comps, Precedents, LBO debt sweeps.",
            "Balance sheet checks (`Assets == Liab + Equity`); non-circular debt/cash sweep mechanics; sensitivity tables.",
        ],
        [
            "<b>3. SaaS Unit Economics</b>",
            "ARR vs MRR, ASC 606 revenue recognition, GRR, NRR, CAC Payback, LTV/CAC, Rule of 40.",
            "Rigorous cohort analysis; understanding limitations of ARR vs GAAP revenue; gross margin impact.",
        ],
        [
            "<b>4. Sector Research &amp; Comps</b>",
            "Vertical SaaS, HCM, PropTech, Supply Chain, AdTech; FactSet, CapIQ, PitchBook, LSEG.",
            "Distinguish verified reported metrics from management estimates; date and cite all market multiples.",
        ],
    ]
    story.append(make_table(resp_data, [1.70 * inch, 2.70 * inch, 3.00 * inch]))

    story.append(PageBreak())

    # PAGE 2: DIAGNOSTIC EXERCISE
    story.append(Paragraph("3. LIVE DIAGNOSTIC EXERCISE: 'PROJECT CLOUDSCALE' (PROPTECH SAAS)", h1_style))
    story.append(Paragraph("<b>Scenario:</b> You are a Senior Analyst staffing a live sell-side M&amp;A mandate for <b>Project CloudScale</b>, a founder-owned Vertical SaaS / PropTech platform. The Managing Director hands you the following reported CY2025A numbers from the company's preliminary financial model:", body_style))

    cs_data = [
        ["Reported Metric (CY2025A)", "Value", "Metric Description &amp; Source"],
        ["<b>Beginning ARR (Jan 1, 2025)</b>", "$40.0M", "Contracted Annual Recurring Revenue run-rate entering the year."],
        ["<b>Ending ARR (Dec 31, 2025)</b>", "$52.0M", "Contracted Annual Recurring Revenue run-rate exiting the year (+$12.0M net change)."],
        ["<b>New Logo ARR Added</b>", "$8.0M", "New annual contract value closed from newly acquired customers in 2025."],
        ["<b>Contraction ARR (Downgrades)</b>", "$1.5M", "Annual recurring revenue lost from existing customer seat/tier downgrades."],
        ["<b>Churned ARR (Cancellations)</b>", "$2.5M", "Annual recurring revenue lost from complete customer account cancellations."],
        ["<b>CY2025 GAAP Subscription Revenue</b>", "$45.0M", "Ratable revenue recognized under ASC 606 (vs. $36.0M in CY2024A, +25.0% YoY)."],
        ["<b>CY2025 Cost of Goods Sold (COGS)</b>", "$9.0M", "Hosting, customer support, and software infrastructure costs (Gross Profit: $36.0M)."],
        ["<b>CY2025 Sales &amp; Marketing (S&amp;M)</b>", "$16.0M", "Total fully burdened acquisition expenses (sales commissions, marketing, SDRs)."],
        ["<b>CY2025 Free Cash Flow (FCF)</b>", "$6.75M", "Cash flow from operations ($8.25M) less capital expenditures ($1.50M)."],
    ]
    story.append(make_table(cs_data, [2.30 * inch, 0.90 * inch, 4.20 * inch]))

    story.append(Paragraph("Diagnostic Questions Assigned by Managing Director:", h2_style))
    story.append(Paragraph("<b>Q1. ARR Waterfall &amp; Retention:</b> (a) What was the dollar amount of <b>Expansion ARR</b> from existing customers? (b) What are CloudScale's <b>Gross Retention Rate (GRR %)</b> and <b>Net Retention Rate (NRR %)</b>?<br/>"
                           "<b>Q2. SaaS Growth Quality &amp; Efficiency:</b> (a) What is CloudScale's <b>Rule of 40 score</b> using GAAP Revenue Growth and FCF Margin? (b) What is the company's <b>CAC Payback Period</b> (in months) applied to New ARR?<br/>"
                           "<b>Q3. Valuation Synthesis:</b> If the PropTech / Vertical SaaS peer median trades at <b>7.5x EV / Ending ARR</b> for a 30% Rule of 40 profile, but CloudScale commands a <b>2.0x multiple premium</b> for top-decile retention, what is CloudScale's <b>implied Enterprise Value ($M)</b>?<br/>"
                           "<b>Q4. Senior Banker Audit Check:</b> The company's CFO claims: <i>'Because GAAP revenue grew +25.0%, our ARR grew at the exact same 25.0%.'</i> Is the CFO correct? Explain the discrepancy.", body_style))

    story.append(PageBreak())

    # PAGE 3: OFFICIAL SOLUTION & MATHEMATICAL PROOFS
    story.append(Paragraph("4. OFFICIAL SENIOR BANKER SOLUTION &amp; MATHEMATICAL PROOFS", h1_style))
    sol_data = [
        ["Question &amp; Metric", "Formula &amp; Arithmetic Steps", "Correct Output", "Senior Banker Commentary"],
        [
            "<b>1a. Expansion ARR</b>",
            "Ending ARR = Beg ARR + New Logo + Expansion - Contraction - Churn<br/>"
            "$52.0M = $40.0M + $8.0M + Exp - $1.5M - $2.5M &rarr; $52.0M = $44.0M + Exp",
            "<b>$8.0M</b>",
            "Expansion perfectly matched New Logo ARR ($8.0M each), proving high upsell velocity across the installed base.",
        ],
        [
            "<b>1b. Gross Retention (GRR)</b>",
            "GRR = (Beg ARR - Contraction - Churn) / Beg ARR<br/>"
            "GRR = ($40.0M - $1.5M - $2.5M) / $40.0M = $36.0M / $40.0M",
            "<b>90.0%</b>",
            "90% GRR is solid tier-1 for middle-market Vertical SaaS (benchmark &gt;88%), reflecting strong product stickiness.",
        ],
        [
            "<b>1c. Net Retention (NRR)</b>",
            "NRR = (Beg ARR + Expansion - Contraction - Churn) / Beg ARR<br/>"
            "NRR = ($40.0M + $8.0M - $1.5M - $2.5M) / $40.0M = $44.0M / $40.0M",
            "<b>110.0%</b>",
            "110% NRR indicates the existing cohort expands by 10% net annually without adding a single new customer.",
        ],
        [
            "<b>2a. Rule of 40 Score</b>",
            "YoY Rev Growth = ($45.0M - $36.0M) / $36.0M = <b>25.0%</b><br/>"
            "FCF Margin = $6.75M / $45.0M = <b>15.0%</b><br/>"
            "Rule of 40 = 25.0% + 15.0%",
            "<b>40.0%</b>",
            "Hits the elite Rule of 40 threshold exactly! Balances strong 25% top-line growth with highly disciplined 15% FCF generation.",
        ],
        [
            "<b>2b. CAC Payback Period</b>",
            "Gross Margin = ($45.0M - $9.0M) / $45.0M = <b>80.0%</b><br/>"
            "Annual Gross Profit Added = $8.0M New ARR * 80% = $6.4M/yr<br/>"
            "CAC Payback = ($16.0M S&amp;M / $6.4M GP) * 12 months = 2.5 yrs * 12",
            "<b>30.0 Months</b><br/>(2.5 Years)",
            "<b>CRITICAL BANKER CAVEAT:</b> 30 months is high for mid-market SaaS (&lt;18-24 mo desired). Buyers will scrutinize S&amp;M efficiency.",
        ],
        [
            "<b>3. Implied Enterprise Value</b>",
            "Implied EV Multiple = Peer Median (7.5x) + Premium (2.0x) = <b>9.5x EV / Ending ARR</b><br/>"
            "Implied Enterprise Value = $52.0M Ending ARR * 9.5x",
            "<b>$494.0M</b>",
            "Implies an enterprise value of ~$494M (or 11.0x on LTM GAAP revenue), establishing the upper-half auction target.",
        ],
    ]
    story.append(make_table(sol_data, [1.40 * inch, 2.70 * inch, 1.10 * inch, 2.20 * inch]))

    story.append(Paragraph("4. Audit Check: Why the CFO's Claim Was Arithmetically False", h2_style))
    story.append(
        Paragraph(
            "• <b>The Error:</b> The CFO claimed ARR grew at the exact same +25.0% rate as GAAP revenue ($36M &rarr; $45M).<br/>"
            "• <b>The Truth:</b> CloudScale's ARR grew from $40.0M to $52.0M, which is <b>+30.0% YoY ARR Growth</b> ($12M / $40M).<br/>"
            "• <b>Why This Discrepancy Occurs:</b> GAAP subscription revenue under ASC 606 recognizes subscription contracts <i>ratably</i> over the 12-month contract term. If sales are backend-weighted (Q3/Q4), ARR reflects the annualized exit run-rate immediately, whereas GAAP revenue only captures a fraction of that expansion in the current calendar year.<br/>"
            "• <b>Why Buyers Care:</b> A private equity or strategic buyer values the business on the forward run-rate of contracted cash flows (ARR). Underestimating ARR growth by 500 bps depresses CloudScale's standalone momentum in buyer marketing materials.",
            body_style,
        )
    )

    story.append(PageBreak())

    # PAGE 4: MANAGING DIRECTOR CRITIQUE & REVIEW CHECKLIST
    story.append(Paragraph("5. SENIOR BANKER CRITIQUE &amp; MANAGING DIRECTOR PUSHBACK", h1_style))
    story.append(
        Paragraph(
            "Here is the exact review conversation a Houlihan Lokey Managing Director will have with you when reviewing this slide:",
            body_style,
        )
    )

    md_critique = [
        ["Banker Scrutiny Area", "Managing Director Challenge &amp; Buyer Objection", "Senior Analyst Response &amp; Model Defense"],
        [
            "<b>S&amp;M Efficiency &amp; 30-Month Payback</b>",
            "<i>'30 months CAC payback is bloated for a $50M Vertical SaaS business. Strategic buyers like Roper or PE sponsors will immediately challenge this in Phase II diligence. Why is S&amp;M running at 35% of revenue if CAC payback is 2.5 years?'</i>",
            "<i>'That is an accurate observation. However, our $16.0M S&amp;M budget includes significant upfront headcount investment for enterprise enterprise sales reps hired in Q3 who have not yet hit full quota productivity. If we blend New Logo ARR with Expansion ARR ($16.0M total ARR added), the blended Magic Number is 1.0x and blended payback drops to 15.0 months. We should present both blended and new logo payback in the CIM.'</i>",
        ],
        [
            "<b>9.5x ARR Multiple Justification</b>",
            "<i>'You have CloudScale modeled at 9.5x ARR versus 7.5x peer median. In the current interest rate environment, how do we defend a 2.0x turn premium to an investment committee?'</i>",
            "<i>'CloudScale clears the Rule of 40 at 40.0% with 15% pure FCF margin, whereas the 7.5x peer median is averaging sub-30% Rule of 40 with negative FCF. Combined with 110% NRR and 90% GRR in mission-critical PropTech workflows, buyers are paying for high-visibility cash conversion and low churn.'</i>",
        ],
    ]
    story.append(make_table(md_critique, [1.50 * inch, 2.95 * inch, 2.95 * inch]))

    story.append(Paragraph("6. COMPREHENSIVE FINANCIAL MODELING AUDIT CHECKLIST", h1_style))
    story.append(
        Paragraph(
            "Before handing any deliverable to an Associate or VP, run this 7-point audit:<br/>"
            "1. <b>ARR Continuity Check:</b> Verify `Beginning ARR + New Logo + Expansion - Contraction - Churn == Ending ARR` with an automated zero-variance formula cell.<br/>"
            "2. <b>Ratable Revenue vs ARR Link:</b> Check whether `GAAP Subscription Revenue / Average ARR` falls between 0.85 and 1.05. A ratio outside this band indicates severe contract timing distortions or unbilled bookings.<br/>"
            "3. <b>Balance Sheet Balance:</b> Ensure `ABS(Total Assets - Total Liabilities &amp; Equity) &lt; $0.001` across all 5 projection years.<br/>"
            "4. <b>Cash Flow Sign Convention:</b> CapEx and debt repayments MUST be negative outflows; cash from operations must properly reflect non-cash D&amp;A addback and change in working capital.<br/>"
            "5. <b>Debt Amortization &amp; Sweep:</b> Mandatory term loan amortization must precede the discretionary FCF cash sweep. Revolver borrowing must be non-circular.<br/>"
            "6. <b>Units &amp; Formatting:</b> Blue font (#0000FF) for inputs, black (#000000) for formulas, green for external links. Consistent units ($M vs $K) labeled on every header.<br/>"
            "7. <b>No Hardcoded Plugs:</b> Eliminate all unexplained plugs, manual number overwrites, and `#REF!` errors across every tab.",
            body_style,
        )
    )

    doc.build(story)
    print(f"[OK] Generated certM Mastery PDF at: {output_path}")


if __name__ == "__main__":
    p1 = r"C:\Users\bhupe\Downloads\Liquidity flow and Outguess\Job4\projects\ml-project-hl-tech-ma\reports\certM_Senior_Analyst_Mastery_Coach_Playbook.pdf"
    p2 = r"C:\Users\bhupe\Downloads\certM_Senior_Analyst_Mastery_Coach_Playbook.pdf"
    build_certm_pdf(p1)
    build_certm_pdf(p2)
