"""
Generates the Executive 4-Page PDF Deliverable for Houlihan Lokey — Corporate Finance Senior Analyst (Technology Group, M&A):
10-Step JD-to-ML Project (HL-TechMA-ValAI), 8-Phase Mastery SOPs, Resume Alignment & Open-to-Close Interview Playbook.
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


def build_pdf(output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title="Houlihan Lokey — Technology Senior Analyst: 10-Step Project & Mastery Playbook",
        author="Bhupesh Chandra Dimri",
    )

    styles = getSampleStyleSheet()
    hl_navy = colors.HexColor("#0A192F")
    hl_gold = colors.HexColor("#C5A059")
    slate = colors.HexColor("#1E293B")
    light_bg = colors.HexColor("#F8FAFC")
    border_col = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=hl_navy,
        alignment=0,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13.5,
        textColor=hl_gold,
        spaceAfter=7,
    )
    h1_style = ParagraphStyle(
        "SectionH1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14.5,
        textColor=hl_navy,
        spaceBefore=9,
        spaceAfter=4,
    )
    h2_style = ParagraphStyle(
        "SectionH2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=12.5,
        textColor=hl_gold,
        spaceBefore=6,
        spaceAfter=3,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.0,
        leading=12.0,
        textColor=slate,
        spaceAfter=3.5,
    )
    bullet_style = ParagraphStyle(
        "BulletItem",
        parent=body_style,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3,
    )
    cell_style = ParagraphStyle(
        "Cell",
        parent=body_style,
        fontSize=8.2,
        leading=10.8,
        spaceAfter=0,
    )
    cell_bold = ParagraphStyle(
        "CellBold",
        parent=cell_style,
        fontName="Helvetica-Bold",
        textColor=colors.white,
    )

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
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 3.5),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                ]
            )
        )
        return t

    story = []

    # HEADER
    story.append(
        Paragraph(
            "HOULIHAN LOKEY — CORPORATE FINANCE SENIOR ANALYST (TECHNOLOGY GROUP)",
            title_style,
        )
    )
    story.append(
        Paragraph(
            "Complete 10-Step Project (HL-TechMA-ValAI), 8-Phase Mastery SOPs & Open-to-Close Interview Playbook",
            subtitle_style,
        )
    )
    story.append(
        Paragraph(
            "<b>Prepared for &amp; Authored by:</b> Bhupesh Chandra Dimri (M.S. Accounting Analytics &amp; Data Technology, Pace University — Beta Alpha Psi | F-1 STEM OPT) &nbsp;|&nbsp; <b>Date:</b> November 2, 2026 &nbsp;|&nbsp; <b>Target Comp:</b> $130,000 Base + Discretionary Bonus ($180K–$220K+ Total)",
            body_style,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.5, color=hl_navy, spaceBefore=2, spaceAfter=6))

    # 0. EXECUTIVE SUMMARY
    story.append(Paragraph("0. EXECUTIVE SUMMARY: HOULIHAN LOKEY TECH M&amp;A THESIS", h1_style))
    story.append(
        Paragraph(
            "• <b>The Mandate at Houlihan Lokey (#1 Global M&amp;A Advisor):</b> HL's Technology Group is the <b>No. 1 technology advisor globally by number of transactions</b> (LSEG #1 M&amp;A rank), providing sell-side M&amp;A, buy-side advisory, and capital raises across Software &amp; Digital Media (Supply Chain, PropTech, EdTech, HCM, Semi, AdTech).",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>The Core Senior Analyst Responsibilities:</b> Leading complex financial modeling (3-statement dynamic models, DCF, Trading Comps, Precedent Transactions, Sponsor LBO returns), preparing Confidential Information Memorandums (CIMs) and pitchbooks, and quarterbacking buyer due diligence across rapid transaction timelines.",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>The Deliverable Built (HL-TechMA-ValAI):</b> A comprehensive Tech M&amp;A valuation and LBO platform modeling <b>Project Apex ($92M ARR Supply Chain SaaS)</b> against a 50-peer universe, generating a live 4-method Valuation Football Field ($265M–$1,137M range) and a 5-year Sponsor LBO return matrix (<b>20.1% Net IRR / 2.50x MoIC</b> at 4.5x leverage).",
            bullet_style,
        )
    )

    # STEP 1
    story.append(Paragraph("STEP 1: DEEP JD DECONSTRUCTION (TOP 1% INVESTMENT BANKING LENS)", h1_style))
    step1_data = [
        ["Category", "Extracted Requirements &amp; Operational Meaning at Houlihan Lokey Tech"],
        [
            "<b>Core Responsibilities</b>",
            "1. Support M&amp;A and equity/debt capital raise transactions for Software &amp; Digital Media clients.<br/>2. Build dynamic financial models: 3-statement operating forecasts, DCF, Trading Comps, Precedent M&amp;A, LBO.<br/>3. Research economic, market, and technology industry developments across Vertical SaaS, HCM, PropTech.<br/>4. Analyze financial statements and SaaS unit economics of public and sponsor-backed private companies.<br/>5. Prepare marketing presentations, CIMs, management presentations, and valuation pitchbooks.",
        ],
        [
            "<b>Technical Stack</b>",
            "Advanced Excel (dynamic arrays, financial modeling, debt schedules, sensitivity tables), PowerPoint, FactSet / CapIQ, PitchBook, LSEG, <b>Python, SQL, DuckDB</b>.",
        ],
        [
            "<b>Hidden Expectations</b>",
            "Houlihan Lokey closes more tech deals than any bank in the world. Deal teams run lean (Managing Director, Director/VP, Associate, Senior Analyst). Senior Analysts must produce zero-defect, board-ready pitchbook slides and dynamic models without hand-holding.",
        ],
        [
            "<b>KPIs &amp; Success Metrics</b>",
            "1. Zero formula errors or plug imbalances in financial models.<br/>2. Rapid turnaround of buyer diligence requests and data room requests.<br/>3. High client presentation quality and executive readiness under compressed timelines.",
        ],
    ]
    story.append(make_table(step1_data, [1.50 * inch, 5.90 * inch]))

    # STEP 2
    story.append(Paragraph("STEP 2: TECH M&amp;A VALUATION &amp; LBO PROBLEM FRAMING", h1_style))
    step2_data = [
        ["Methodology", "Inputs (X) &amp; Drivers", "Model Architecture", "Transaction Output &amp; Role in Deal"],
        [
            "<b>1. Public Trading Comps (EV / ARR &amp; EBITDA)</b>",
            "50 peers; ARR growth, NRR, Gross Margin, Rule of 40.",
            "<b>Peer Regression &amp; Quartiles</b>.<br/>EV/ARR &amp; EV/EBITDA benchmarking.",
            "Establishes public market baseline for Pitchbooks &amp; Fairness Opinions.",
        ],
        [
            "<b>2. Precedent Tech M&amp;A Transactions</b>",
            "Recent strategic &amp; sponsor software deals with control premiums.",
            "<b>M&amp;A Multiple Distribution</b><br/>(15–20% premium over comps).",
            "Guides sell-side valuation expectations and auction reserve prices.",
        ],
        [
            "<b>3. Unlevered Discounted Cash Flow (DCF)</b>",
            "5-year UFCF, WACC (9.5–11.5%), Terminal Growth (2.5–3.5%).",
            "<b>Mid-Year UFCF DCF Engine</b> + Gordon Growth Terminal Value.",
            "Provides intrinsic standalone valuation independent of cycles.",
        ],
        [
            "<b>4. Financial Sponsor LBO Model</b>",
            "Target debt capacity, 85% cash sweep, exit multiples.",
            "<b>5-Year Debt Paydown Engine</b><br/>computing Sponsor Net IRR &amp; MoIC.",
            "Evaluates private equity sponsor bidding power and floor valuation.",
        ],
    ]
    story.append(make_table(step2_data, [1.50 * inch, 1.95 * inch, 1.95 * inch, 2.00 * inch]))

    story.append(PageBreak())

    # STEPS 3, 4 & 5
    story.append(Paragraph("STEPS 3, 4 &amp; 5: VALUATION FOOTBALL FIELD &amp; SPONSOR LBO BENCHMARKS", h1_style))
    story.append(Paragraph("3.1 Project Apex Valuation Football Field ($92M ARR Target)", h2_style))
    ff_data = [
        ["Methodology", "Metric Base", "Multiple Range", "Low EV ($M)", "Median EV ($M)", "High EV ($M)"],
        ["<b>Public Trading Comps (EV/ARR)</b>", "$92.0M ARR", "7.5x - 10.3x (Med: 9.3x)", "$690.0M", "$855.6M", "$947.6M"],
        ["<b>Precedent Tech M&amp;A Deals</b>", "$92.0M ARR", "8.6x - 12.4x (Med: 11.0x)", "$793.5M", "$1,009.6M", "$1,137.1M"],
        ["<b>Public Comps (EV/EBITDA)</b>", "$25.0M NTM", "15.0x - 20.2x (Med: 18.0x)", "$373.8M", "$450.0M", "$505.6M"],
        ["<b>Unlevered DCF (WACC 9.5-11.5%)</b>", "$85.0M Rev", "WACC: 9.5-11.5% | g: 2.5-3.5%", "$265.5M", "$318.0M", "$396.9M"],
    ]
    story.append(make_table(ff_data, [1.85 * inch, 0.95 * inch, 1.85 * inch, 0.90 * inch, 0.95 * inch, 0.90 * inch]))

    story.append(Paragraph("4.1 Sponsor LBO Sensitivity Matrix (Leverage vs. Exit Multiple)", h2_style))
    lbo_sens_data = [
        ["Entry Leverage (x EBITDA)", "Exit @ 6.5x ARR", "Exit @ 7.5x ARR (Base)", "Exit @ 8.5x ARR"],
        ["<b>4.0x Leverage ($74.0M Debt)</b>", "16.4% Net IRR (2.14x MoIC)", "19.8% Net IRR (2.47x MoIC)", "22.8% Net IRR (2.80x MoIC)"],
        ["<b>4.5x Leverage ($83.2M Debt)</b>", "16.7% Net IRR (2.17x MoIC)", "<b>20.1% Net IRR (2.50x MoIC)</b>", "23.2% Net IRR (2.84x MoIC)"],
        ["<b>5.0x Leverage ($92.5M Debt)</b>", "16.9% Net IRR (2.18x MoIC)", "20.3% Net IRR (2.52x MoIC)", "23.4% Net IRR (2.86x MoIC)"],
    ]
    story.append(make_table(lbo_sens_data, [1.85 * inch, 1.85 * inch, 1.85 * inch, 1.85 * inch]))

    story.append(PageBreak())

    # STEP 6

    story.append(Paragraph("4.2 Key Banker Takeaways for Managing Director &amp; Client Pitches", h2_style))
    story.append(
        Paragraph(
            "• <b>Valuation Synthesis:</b> Project Apex commands an implied M&amp;A enterprise value of <b>$850M–$1,010M (9.2x–11.0x ARR)</b> in a competitive sell-side auction, driven by its premium <b>44.5% Rule of 40 score</b> and <b>118% Net Retention Rate</b>.<br/>"
            "• <b>Sponsor Bidding Floor:</b> Financial sponsors can comfortably bid <b>7.5x ARR ($690M EV)</b> using 4.5x EBITDA leverage and achieve a <b>20.1% Net IRR / 2.50x MoIC</b>, creating a strong valuation floor for strategic acquirors.",
            body_style,
        )
    )

    # STEP 6
    story.append(Paragraph("STEP 6: RESUME ALIGNMENT ENGINE (BHUPESH CHANDRA DIMRI -> HOULIHAN LOKEY)", h1_style))
    story.append(
        Paragraph(
            "<b>Pre-Project Alignment Score:</b> 8.1 / 10 &nbsp;&rarr;&nbsp; <b>Post-Project Alignment Score: 9.4 / 10</b>",
            body_style,
        )
    )
    step6_table = [
        ["HL Senior Analyst JD Requirement", "Bhupesh's Verified Evidence (ENT-001)", "Strategic Positioning for Tech Corporate Finance"],
        [
            "<b>Analyze financial statements, M&amp;A modeling &amp; valuation attributes</b>",
            "10+ years in FP&A, multi-entity financial consolidation, sensitivity modeling across $50M+ portfolios (Virtual Infotech, Bankers Life).",
            "Advanced 3-statement modeling, working capital adjustments, and EBITDA bridges guarantee 100% accounting and arithmetic integrity.",
        ],
        [
            "<b>Advanced knowledge of Excel and PowerPoint</b>",
            "Architected automated reporting models cutting reporting latency from 48 hrs to &lt;2 hrs; Goldman Sachs Controllers simulation.",
            "Position financial modeling speed and clean executive slide design as immediate capacity-relief for Associates and VPs.",
        ],
        [
            "<b>Manage rapid timelines &amp; act independently on high-stakes deliverables</b>",
            "Led cross-department financial close and commercial portfolio reconciliations with 99.5% accuracy under SOX 404 / GAAP controls.",
            "Proven track record of managing high-stress deadlines with zero defect rate under audit-grade scrutiny.",
        ],
    ]
    story.append(make_table(step6_table, [1.85 * inch, 2.70 * inch, 2.85 * inch]))

    story.append(Paragraph("Ready-to-Paste Resume Project Block:", h2_style))
    story.append(
        Paragraph(
            "<b>Technology M&amp;A Valuation, SaaS Operating Benchmark &amp; LBO Return Engine (HL-TechMA-ValAI)</b> | <i>Python, Financial Modeling, DCF, Comps, LBO</i><br/>"
            "• Engineered a comprehensive Tech M&amp;A financial modeling suite benchmarking a <b>$92M ARR enterprise SaaS target</b> against 50 public peers across EV/ARR, NRR, and Rule of 40 unit economics.<br/>"
            "• Built integrated 3-statement operating models, 5-year Unlevered DCF with WACC/growth sensitivity ($265M–$397M EV range), and a 5-year Sponsor LBO debt sweep model delivering <b>20.1% Net IRR / 2.50x MoIC</b> at 4.5x leverage.",
            body_style,
        )
    )

    story.append(PageBreak())

    # STEPS 7, 8, 9
    story.append(Paragraph("STEPS 7, 8 &amp; 9: ARCHITECTURE, 10-SLIDE EXECUTIVE DECK &amp; GITHUB REPOSITORY", h1_style))
    story.append(
        Paragraph(
            "• <b>Financial Engineering Architecture (Step 7):</b> [CapIQ / SEC 10-K Data Ingestion] &rarr; [Driver-Based 3-Statement Forecast Engine] &rarr; [Public Comps &amp; Precedent M&amp;A Multiples Generator] &rarr; [Unlevered DCF &amp; WACC Matrix] &rarr; [Sponsor LBO &amp; Debt Schedule Engine] &rarr; [Executive Pitchbook Valuation Football Field].",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>10-Slide Pitchbook Presentation Structure (Step 8):</b> (1) Executive Title | (2) Transaction Overview &amp; Executive Summary | (3) Target Business &amp; SaaS Operating Profile | (4) Industry Trends &amp; End-Market Tailwinds | (5) Historical &amp; Projected 3-Statement Financials | (6) Public Trading Comps (EV/ARR, Rule of 40) | (7) Precedent Tech M&amp;A Transactions | (8) Unlevered Discounted Cash Flow Analysis | (9) Valuation Football Field &amp; Strategic Implications | (10) Financial Sponsor LBO Analysis &amp; Debt Capacity.",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>Verified GitHub Repository on Disk (Step 9):</b> <i>Job4/projects/ml-project-hl-tech-ma/</i> containing <b>README.md</b>, <b>requirements.txt</b>, <b>src/data_pipeline.py</b>, <b>src/valuation_engine.py</b>, <b>src/lbo_engine.py</b>, <b>src/evaluate.py</b>, and <b>reports/model_report.md</b>.",
            bullet_style,
        )
    )

    # STEP 10
    story.append(Paragraph("STEP 10: TOP 1% DIFFERENTIATION, MASTERY SOP &amp; ARP INTERVIEW PLAYBOOK", h1_style))
    story.append(
        Paragraph(
            "• <b>Mastery 9-Stage Tech M&amp;A Sell-Side Mandate Workflow SOP (MTH-005):</b><br/>"
            "1. <i>Trigger:</i> Executed engagement letter for sell-side M&amp;A or capital raise.<br/>"
            "2. <i>Inputs:</i> Historical financial statements (3-5 years), monthly ARR waterfall, customer cohort retention data, Cap Table.<br/>"
            "3. <i>Preparation:</i> Normalize EBITDA (addbacks for non-recurring expenses, sponsor management fees, founder comp).<br/>"
            "4. <i>Execution:</i> Build integrated 3-statement model; pull peer comps; run DCF and Sponsor LBO returns.<br/>"
            "5. <i>Validation:</i> Balance sheet balance check (Assets == Liabilities + Equity), debt schedule tie-outs.<br/>"
            "6. <i>Marketing Collateral:</i> Draft Executive Teaser and 40-page Confidential Information Memorandum (CIM).<br/>"
            "7. <i>Approval:</i> Internal Senior Banker (MD/VP) model audit and fairness review.<br/>"
            "8. <i>Delivery:</i> Launch auction process, distribute CIM to vetted buyers, open Virtual Data Room (VDR).<br/>"
            "9. <i>Documentation:</i> Maintain transaction log, IOI/LOI bid tracking matrix, and compliance records.",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>Word-for-Word ARP Dodge Script ('Why FP&amp;A / Accounting Analytics to Investment Banking?'):</b><br/>"
            "<b>1. Acknowledge (5s):</b> <i>'That is an important question, and I appreciate you raising it directly.'</i><br/>"
            "<b>2. Reframe (15s):</b> <i>'Investment banking analyst work lives and dies by financial modeling integrity: dynamic 3-statement models, working capital adjustments, debt schedules, and valuation football fields. Over 10 years in FP&amp;A and accounting analytics, I have audited balance sheets, reconciled over 1,000 daily transactions at 99.5% accuracy, and built sensitivity models across $50M+ portfolios. While many lateral candidates need months to understand how GAAP cash flows connect to balance sheets, I have mastered that accounting mechanics for years.'</i><br/>"
            "<b>3. Pivot to Proof (25s):</b> <i>'To prove day-one readiness for Houlihan Lokey, I built HL-TechMA-ValAI—a complete financial engineering platform that models a $92M ARR SaaS target against 50 comps, generates a multi-method football field, and runs a 5-year Sponsor LBO with dynamic debt sweep delivering 20.1% IRR. I would love to walk through the model mechanics in 60 seconds.'</i>",
            bullet_style,
        )
    )
    story.append(
        Paragraph(
            "• <b>Top 3 Executive Questions for Houlihan Lokey Senior Bankers (SYN-002):</b><br/>"
            "1. <i>'As the No. 1 tech M&amp;A advisor globally, Houlihan Lokey sees incredible deal flow across mid-market software. In the current M&amp;A environment, where are you seeing the biggest bid-ask spread between founder ARR multiple expectations and financial sponsor LBO return hurdles?'</i><br/>"
            "2. <i>'In software subsectors like Vertical SaaS vs. PropTech or Supply Chain, how heavily are buyers weighting Rule of 40 balance (FCF margin vs. pure top-line growth) compared to 12 months ago?'</i><br/>"
            "3. <i>'Based on our discussion today and the HL-TechMA-ValAI financial model I shared, is there anything that gives you pause about my ability to immediately hit the desk and execute for the team?'</i>",
            bullet_style,
        )
    )

    doc.build(story)
    print(f"[OK] Generated PDF at: {output_path}")


if __name__ == "__main__":
    p1 = r"C:\Users\bhupe\Downloads\Liquidity flow and Outguess\Job4\projects\ml-project-hl-tech-ma\reports\Houlihan_Lokey_Tech_Senior_Analyst_Mastery_Playbook.pdf"
    p2 = r"C:\Users\bhupe\Downloads\Houlihan_Lokey_Tech_Senior_Analyst_Mastery_Playbook.pdf"
    build_pdf(p1)
    build_pdf(p2)
