"""
Generates the complete Injobman ATS Application Suite & HireMe PDF Package for Houlihan Lokey:
1. Tailored 1-Page ATS Resume (PDF)
2. Targeted 1-Page Executive Cover Letter (PDF)
3. 4-Page HireMe Interview & Salary Negotiation Mastery Playbook (PDF)
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


def generate_resume_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.45 * inch,
        rightMargin=0.45 * inch,
        topMargin=0.40 * inch,
        bottomMargin=0.40 * inch,
        title="Bhupesh Chandra Dimri - Houlihan Lokey Technology Senior Analyst Resume",
        author="Bhupesh Chandra Dimri",
    )

    styles = getSampleStyleSheet()
    hl_navy = colors.HexColor("#0A192F")
    slate = colors.HexColor("#1E293B")
    border_col = colors.HexColor("#94A3B8")

    name_style = ParagraphStyle(
        "Name",
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=hl_navy,
        alignment=1,
    )
    contact_style = ParagraphStyle(
        "Contact",
        fontName="Helvetica",
        fontSize=8.5,
        leading=11.5,
        textColor=slate,
        alignment=1,
        spaceAfter=5,
    )
    section_title = ParagraphStyle(
        "SecTitle",
        fontName="Helvetica-Bold",
        fontSize=9.8,
        leading=12.5,
        textColor=hl_navy,
        spaceBefore=5,
        spaceAfter=2,
    )
    job_title = ParagraphStyle(
        "JobTitle",
        fontName="Helvetica-Bold",
        fontSize=8.8,
        leading=11.5,
        textColor=hl_navy,
    )
    job_meta = ParagraphStyle(
        "JobMeta",
        fontName="Helvetica-Oblique",
        fontSize=8.2,
        leading=11.0,
        textColor=slate,
        alignment=2,
    )
    bullet = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=8.2,
        leading=10.8,
        textColor=slate,
        leftIndent=10,
        firstLineIndent=-7,
        spaceAfter=2,
    )

    story = []
    story.append(Paragraph("BHUPESH CHANDRA DIMRI", name_style))
    story.append(
        Paragraph(
            "New York, NY &nbsp;|&nbsp; 917-818-6198 &nbsp;|&nbsp; bhupeshcdimri@pace.edu &nbsp;|&nbsp; "
            "linkedin.com/in/bhupeshdimri &nbsp;|&nbsp; github.com/bhupesh-debug &nbsp;|&nbsp; <b>U.S. Work Authorization: F-1 STEM OPT (3 Years)</b>",
            contact_style,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1.2, color=hl_navy, spaceBefore=1, spaceAfter=4))

    # SUMMARY
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_title))
    story.append(
        Paragraph(
            "Quantitative financial analyst and modeling specialist with 10+ years of progressive experience across corporate FP&A, "
            "integrated 3-statement modeling, multi-entity portfolio valuation, and dynamic sensitivity analysis. Advanced expertise in "
            "Software & Digital Media unit economics (ARR, NRR, Rule of 40), DCF, Trading Comps, and LBO returns. Built "
            "<b>HL-TechMA-ValAI</b>, an institutional valuation engine modeling a $92M ARR SaaS target against 50 peers. Holds an M.S. in "
            "Accounting Analytics & Data Technology from Pace University (Beta Alpha Psi); Bloomberg BMC & BFF Certified.",
            bullet,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_col, spaceBefore=3, spaceAfter=3))

    # TECH M&A PROJECT
    story.append(Paragraph("SELECT TECH M&A & FINANCIAL MODELING PROJECT", section_title))
    story.append(
        Paragraph(
            "<b>Technology M&A Valuation, SaaS Operating Benchmark & LBO Return Engine (HL-TechMA-ValAI)</b>",
            job_title,
        )
    )
    story.append(
        Paragraph(
            "• Built an institutional M&A financial engineering platform benchmarking a <b>$92M ARR enterprise SaaS target</b> against 50 public peers across EV/ARR, NRR, Gross Margin, and Rule of 40 unit economics.<br/>"
            "• Engineered integrated 3-statement operating models, 5-year Unlevered DCF with WACC/growth sensitivity ($265M–$397M EV range), and a 5-year Sponsor LBO debt sweep delivering <b>20.1% Net IRR / 2.50x MoIC</b> at 4.5x leverage.<br/>"
            "• Automated multi-method Valuation Football Field ($265M–$1,137M range) and dynamic pitchbook tables for senior banker readouts.",
            bullet,
        )
    )
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_col, spaceBefore=3, spaceAfter=3))

    # EXPERIENCE
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_title))

    # Simms Tax
    t1 = Table([[Paragraph("<b>Simms Tax Services</b> — <i>Financial & Portfolio Valuation Analyst</i>", job_title), Paragraph("New York, NY | Apr 2026 – Present", job_meta)]], colWidths=[5.4 * inch, 2.2 * inch])
    t1.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    story.append(t1)
    story.append(Paragraph("• Built multi-entity financial consolidation and cash flow models tracking budget-vs-actuals, reducing manual preparation time by <b>40%</b>.<br/>• Executed ROI and capital-allocation models evaluating multi-asset portfolio investments, improving forecast reliability.", bullet))

    # Bankers Life
    t2 = Table([[Paragraph("<b>Bankers Life</b> — <i>Financial Planning & Analysis (FP&A) Analyst</i>", job_title), Paragraph("New York, NY | Jul 2025 – Mar 2026", job_meta)]], colWidths=[5.4 * inch, 2.2 * inch])
    t2.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    story.append(t2)
    story.append(Paragraph("• Architected automated financial dashboards and variance diagnostic models integrating SAP/Oracle ERP and market data, cutting reporting turnaround from <b>48 hours to &lt;2 hours</b>.<br/>• Built multi-scenario financial sensitivity models under SOX 404 controls, reducing controllable variance leakages by <b>16%</b>.", bullet))

    # Virtual Infotech
    t3 = Table([[Paragraph("<b>Virtual Infotech</b> — <i>Financial Modeling & Analysis Analyst</i>", job_title), Paragraph("New York, NY | Jan 2025 – Jun 2025", job_meta)]], colWidths=[5.4 * inch, 2.2 * inch])
    t3.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    story.append(t3)
    story.append(Paragraph("• Built integrated 3-statement operating and cash flow models across <b>$50M+ annual budget portfolios</b> (+24% forecast accuracy).<br/>• Automated recurring valuation, variance, and financial close packs in SQL and Excel VBA, reducing manual workload by <b>50%</b>.", bullet))

    # Genpact
    t4 = Table([[Paragraph("<b>Genpact India Pvt. Ltd.</b> — <i>Senior Financial Process Associate</i>", job_title), Paragraph("India | Jan 2014 – Dec 2024", job_meta)]], colWidths=[5.4 * inch, 2.2 * inch])
    t4.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BOTTOMPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0)]))
    story.append(t4)
    story.append(Paragraph("• Reconciled <b>1,000+ daily financial transactions</b> in Oracle ERP and SQL at <b>99.5% accuracy</b> across multi-department operating budgets.<br/>• Prepared monthly executive cash flow summaries, balance sheet tie-outs, and P&L bridge analyses under strict US GAAP compliance.", bullet))
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_col, spaceBefore=3, spaceAfter=3))

    # EDUCATION & CERTIFICATIONS
    story.append(Paragraph("EDUCATION & CERTIFICATIONS", section_title))
    story.append(Paragraph("• <b>M.S. in Accounting Analytics & Data Technology</b> — Pace University, Lubin School of Business, New York, NY (Dec 2025 | Beta Alpha Psi)<br/>"
                           "• <b>MBA in Finance & Accounting</b> — Sikkim Manipal University (2015) &nbsp;|&nbsp; <b>B.Com</b> — HNB Garhwal University (2010)<br/>"
                           "• <b>Certifications:</b> Bloomberg BMC & BFF Certified &nbsp;|&nbsp; Oracle Fusion Cloud ERP/EPM Certified &nbsp;|&nbsp; CPA Candidate", bullet))
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_col, spaceBefore=3, spaceAfter=3))

    # SKILLS
    story.append(Paragraph("TECHNICAL & FINANCIAL MODELING SKILLS", section_title))
    story.append(Paragraph("• <b>Financial Modeling:</b> 3-Statement Dynamic Modeling, DCF, Trading Comps, Precedent M&A, LBO (Debt Schedule & Sweep), Valuation Football Fields.<br/>"
                           "• <b>Software & Tools:</b> Advanced Excel (Dynamic Arrays, Sensitivity Tables, Power Query, VBA), PowerPoint, Bloomberg Terminal, SQL, Python, FactSet/CapIQ.<br/>"
                           "• <b>Domain Knowledge:</b> SaaS Metrics (ARR, NRR, Rule of 40, CAC Payback), US GAAP, Working Capital Normalization, EBITDA Adjustments.", bullet))

    doc.build(story)
    print(f"[OK] Generated Resume PDF at: {output_path}")


def generate_cover_letter_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
        title="Bhupesh Chandra Dimri - Houlihan Lokey Cover Letter",
        author="Bhupesh Chandra Dimri",
    )

    styles = getSampleStyleSheet()
    hl_navy = colors.HexColor("#0A192F")
    slate = colors.HexColor("#1E293B")

    header_name = ParagraphStyle("HName", fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=hl_navy)
    header_meta = ParagraphStyle("HMeta", fontName="Helvetica", fontSize=8.5, leading=11, textColor=slate, spaceAfter=8)
    p_style = ParagraphStyle("PStyle", fontName="Helvetica", fontSize=9.0, leading=12.6, textColor=slate, spaceAfter=7)
    p_bold = ParagraphStyle("PBold", fontName="Helvetica-Bold", fontSize=9.0, leading=12.6, textColor=hl_navy, spaceAfter=7)

    story = []
    story.append(Paragraph("BHUPESH CHANDRA DIMRI", header_name))
    story.append(Paragraph("New York, NY &nbsp;|&nbsp; 917-818-6198 &nbsp;|&nbsp; bhupeshcdimri@pace.edu &nbsp;|&nbsp; linkedin.com/in/bhupeshdimri", header_meta))
    story.append(HRFlowable(width="100%", thickness=1.0, color=hl_navy, spaceBefore=0, spaceAfter=8))

    story.append(Paragraph("November 2, 2026", p_style))
    story.append(Paragraph("<b>Technology Group Recruiting Committee</b><br/>Houlihan Lokey, Inc.<br/>245 Park Avenue, 20th Floor, New York, NY 10167", p_style))
    story.append(Paragraph("<b>RE: Corporate Finance Senior Analyst — Technology Group (Software &amp; Digital Media)</b>", p_bold))

    story.append(Paragraph("Dear Members of the Technology Group Selection Committee,", p_style))

    story.append(
        Paragraph(
            "I am writing to express my strong enthusiasm for the Senior Analyst position within Houlihan Lokey’s Technology Group in New York. "
            "As the undisputed <b>No. 1 technology M&amp;A advisor globally by transaction volume</b>, Houlihan Lokey provides unmatched advisory "
            "leadership across Software and Digital Media. Having spent over a decade building complex financial models, auditing 3-statement "
            "ledgers under GAAP/SOX controls, and evaluating corporate valuations, I am excited to bring my financial modeling rigor, "
            "accounting fluency, and relentless work ethic to your high-velocity transaction teams.",
            p_style,
        )
    )

    story.append(
        Paragraph(
            "To demonstrate immediate day-one technical capability, I engineered <b>HL-TechMA-ValAI</b>, an institutional financial modeling suite "
            "purpose-built for Houlihan Lokey’s software practice. The platform models <b>Project Apex ($92M ARR Enterprise Supply Chain SaaS target)</b> "
            "against a 50-peer Software universe, generating an automated 4-method Valuation Football Field ($265M–$1,137M range), a 5-year Unlevered "
            "DCF with dynamic WACC sensitivity, and a comprehensive 5-year Financial Sponsor LBO model. The LBO model demonstrates that a "
            "sponsor can bid <b>7.5x ARR ($690M EV)</b> with 4.5x EBITDA leverage and clear a <b>20.1% Net IRR / 2.50x MoIC</b> with full cash sweep debt paydown. "
            "This project reflects my ability to rapidly deconstruct software unit economics (ARR, NRR, Rule of 40) and translate raw data into board-ready presentation materials.",
            p_style,
        )
    )

    story.append(
        Paragraph(
            "My background directly addresses the core operational demands of Houlihan Lokey deal teams:<br/>"
            "• <b>Zero-Defect 3-Statement Modeling:</b> Over 10 years in corporate FP&amp;A and accounting analytics, I have reconciled over 1,000 daily transactions at 99.5% accuracy, built integrated P&amp;L/balance sheet/cash flow models across $50M+ portfolios, and eliminated typical junior balance breaks.<br/>"
            "• <b>Rapid Turnaround &amp; Process Automation:</b> At Bankers Life and Virtual Infotech, I built automated SQL, Python, and advanced Excel pipelines that slashed executive reporting turnaround from 48 hours to under 2 hours, demonstrating the speed and independence required during compressed auction timelines.<br/>"
            "• <b>Rigorous Foundation &amp; Work Authorization:</b> Completed my M.S. in Accounting Analytics &amp; Data Technology at Pace University (Beta Alpha Psi), hold Bloomberg BMC &amp; BFF certifications, and possess 3 continuous years of full-time U.S. work authorization under F-1 STEM OPT with zero visa sponsorship required.",
            p_style,
        )
    )

    story.append(
        Paragraph(
            "I thrive in entrepreneurial, high-stakes environments where intellectual curiosity, attention to detail, and team dedication are paramount. "
            "I welcome the opportunity to discuss how my modeling toolkit can provide immediate capacity relief and analytical leverage to Houlihan Lokey's "
            "Technology Group.",
            p_style,
        )
    )

    story.append(Paragraph("Sincerely,<br/><b>Bhupesh Chandra Dimri</b><br/>Enclosures: Resume &amp; HL-TechMA-ValAI Playbook", p_style))

    doc.build(story)
    print(f"[OK] Generated Cover Letter PDF at: {output_path}")


def generate_hireme_playbook_pdf(output_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.55 * inch,
        rightMargin=0.55 * inch,
        topMargin=0.50 * inch,
        bottomMargin=0.50 * inch,
        title="HireMe: Houlihan Lokey Technology Senior Analyst Interview Mastery Playbook",
        author="Bhupesh Chandra Dimri",
    )

    styles = getSampleStyleSheet()
    hl_navy = colors.HexColor("#0A192F")
    hl_gold = colors.HexColor("#C5A059")
    slate = colors.HexColor("#1E293B")
    light_bg = colors.HexColor("#F8FAFC")
    border_col = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle("HTitle", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=hl_navy, spaceAfter=3)
    subtitle_style = ParagraphStyle("HSub", fontName="Helvetica-Bold", fontSize=9.5, leading=13, textColor=hl_gold, spaceAfter=6)
    h1_style = ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=hl_navy, spaceBefore=8, spaceAfter=3)
    h2_style = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=hl_gold, spaceBefore=5, spaceAfter=2)
    body_style = ParagraphStyle("HBody", fontName="Helvetica", fontSize=8.8, leading=11.8, textColor=slate, spaceAfter=3)
    bullet_style = ParagraphStyle("HBullet", parent=body_style, leftIndent=10, firstLineIndent=-7, spaceAfter=2.5)
    cell_style = ParagraphStyle("HCell", parent=body_style, fontSize=8.0, leading=10.5, spaceAfter=0)
    cell_bold = ParagraphStyle("HCellBold", parent=cell_style, fontName="Helvetica-Bold", textColor=colors.white)

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

    # PAGE 1: 6-PHASE FLOW & 60-SEC PITCH
    story.append(Paragraph("HIREME: HOULIHAN LOKEY TECH SENIOR ANALYST INTERVIEW PLAYBOOK", title_style))
    story.append(Paragraph("Open-to-Close Flow Control, Technical Defense, ARP Dodge Protocols & Word-for-Word Negotiation", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=hl_navy, spaceBefore=1, spaceAfter=5))

    story.append(Paragraph("1. THE 6-PHASE OPEN-TO-CLOSE INTERVIEW ARCHITECTURE (SYN-002)", h1_style))
    story.append(Paragraph("• <b>Phase 1: First 120 Seconds (Warm Insider Rapport):</b> <i>'Good morning [Interviewer Name]. I have been closely tracking Houlihan Lokey’s tech franchise, particularly maintaining the #1 global M&A transaction ranking. With middle-market software M&A bifurcating around Rule of 40 quality, HL’s transaction volume gives you differentiated real-time valuation perspectives. I have been very excited for our conversation today.'</i>", bullet_style))
    story.append(Paragraph("• <b>Phase 2: 60-Second Brand Hook ('Tell Me About Yourself'):</b><br/>"
                           "<i>'Over the past 10 years, I have specialized in financial modeling, dynamic 3-statement projections, and multi-entity portfolio valuation across corporate finance and FP&A. Most recently, I completed my M.S. in Accounting Analytics at Pace University with Beta Alpha Psi honors. To demonstrate immediate day-one technical capability for Houlihan Lokey’s Tech Group, I engineered <b>HL-TechMA-ValAI</b>—a complete financial engineering platform that benchmarks a $92M ARR SaaS target against 50 peers, generates an automated Valuation Football Field ($265M–$1,137M), and runs a 5-year Sponsor LBO model delivering 20.1% Net IRR at 4.5x leverage. I am looking to bring this financial modeling rigor, balance sheet fluency, and rapid execution stamina to your Tech M&A deal teams.'</i>", bullet_style))
    story.append(Paragraph("• <b>Phase 3: Active-Ownership STAR Rules:</b> Ban passive language ('we helped', 'involved in'). Use active verbs: <i>'I architected', 'I reconciled', 'I modeled', 'I structured'</i>. Conclude every technical answer with a 90-second Steering Hook handing control back to your turf.", bullet_style))
    story.append(Paragraph("• <b>Phase 4: ARP Dodge Protocol:</b> For non-traditional background or tricky questions, follow <i>Acknowledge (5s) &rarr; Reframe (15s) &rarr; Pivot to Live Proof (25s)</i>.", bullet_style))
    story.append(Paragraph("• <b>Phase 5: Executive Closing:</b> Ask 3 strategic transaction questions + deploy the <b>Commitment Lock-In Question</b>.", bullet_style))
    story.append(Paragraph("• <b>Phase 6: Salary Maximization:</b> Defer early salary anchoring, take 48 hours on verbal offers, and sequence non-salary levers.", bullet_style))

    story.append(Paragraph("2. TECH M&A TECHNICAL QUESTION BANK (MUST-MASTER Q&A)", h1_style))
    q_data = [
        ["Question & Category", "Top 1% Model Answer & Core Formula", "Senior Banker Intent"],
        [
            "<b>1. Three-Statement Flow: $10 Depreciation</b><br/><i>(Core Accounting)</i>",
            "<b>IS:</b> Operating Income (EBIT) drops by $10. At 25% tax rate, Net Income drops by <b>$7.50</b>.<br/>"
            "<b>CFS:</b> Net Income down $7.50, add back $10 non-cash D&A &rarr; Cash Flow from Ops increases by <b>+$2.50</b> (tax shield).<br/>"
            "<b>BS:</b> Cash is up $2.50, PP&E down $10 &rarr; Total Assets down <b>-$7.50</b>. Retained Earnings down <b>-$7.50</b> &rarr; Balance Sheet balances.",
            "Tests instant balance sheet tie-out intuition. Must be answered cleanly in 30 seconds with zero hesitation.",
        ],
        [
            "<b>2. Enterprise Value vs. Equity Value</b><br/><i>(Valuation Mechanics)</i>",
            "<b>Enterprise Value (EV)</b> = Equity Value + Total Debt + Preferred Stock + Minority Interest - Cash &amp; Equivalents.<br/>"
            "EV represents total value of operating assets available to all capital providers. Operating metrics (EBITDA, ARR, Revenue) pair with EV. Net Income and FCF to Equity pair with Equity Value.",
            "Checks capital structure literacy and multiple consistency (never say EV/Net Income).",
        ],
        [
            "<b>3. Why EV/ARR for High-Growth SaaS?</b><br/><i>(Tech Group Specialized)</i>",
            "High-growth software companies invest heavily in upfront S&amp;M to acquire multi-year subscription contracts (recognized ratably under ASC 606). This creates GAAP net losses and negative EBITDA despite highly profitable customer cohort lifetime economics (LTV/CAC &gt; 3x). EV/ARR standardizes contracted annualized recurring revenue run-rate across peers.",
            "Tests deep comprehension of software unit economics and ASC 606 revenue recognition.",
        ],
    ]
    story.append(make_table(q_data, [1.85 * inch, 3.65 * inch, 1.90 * inch]))

    story.append(PageBreak())

    # PAGE 2: ADVANCED VALUATION & LBO QUESTIONS
    story.append(Paragraph("3. ADVANCED VALUATION, LBO & SAAS METRICS DEFENSE", h1_style))
    q2_data = [
        ["Question & Category", "Top 1% Model Answer & Core Formula", "Senior Banker Intent"],
        [
            "<b>4. Walk Me Through an Unlevered DCF</b><br/><i>(Intrinsic Valuation)</i>",
            "1. Project Unlevered Free Cash Flow (UFCF = EBIT*(1-t) + D&A - CapEx - &Delta;NWC) for 5-10 years.<br/>"
            "2. Discount UFCFs to present using WACC with mid-year convention.<br/>"
            "3. Compute Terminal Value via Gordon Growth ($TV = UFCF_{T+1} / (WACC - g)$) or Exit Multiple.<br/>"
            "4. Sum PV of UFCF + PV of TV = Enterprise Value. Subtract Net Debt = Equity Value.",
            "Verifies end-to-end DCF mechanics, reinvestment rate assumptions, and terminal sensitivity.",
        ],
        [
            "<b>5. Primary Levers in a Sponsor LBO</b><br/><i>(Private Equity Modeling)</i>",
            "1. <b>Debt Paydown &amp; Deleveraging:</b> 85% FCF cash sweep reduces debt, transferring value to equity.<br/>"
            "2. <b>EBITDA / Operational Growth:</b> Organic revenue growth and margin expansion.<br/>"
            "3. <b>Multiple Expansion:</b> Selling at a higher exit EV multiple than entry (conservative models assume flat or contraction).",
            "Tests whether you understand how PE sponsors generate 20%+ target IRRs.",
        ],
        [
            "<b>6. The Rule of 40 in Tech M&A</b><br/><i>(SaaS Benchmarking)</i>",
            "<b>Rule of 40 = YoY Revenue Growth % + FCF (or EBITDA) Margin %</b>.<br/>"
            "Software targets exceeding 40% command premium EV/ARR multiples (e.g. Project Apex at 44.5% trades at 9.3x ARR vs. 5.5x for sub-30% peers). It measures capital efficiency and balance between growth and cash generation.",
            "Tests familiarity with Houlihan Lokey tech valuation pitchbook benchmarks.",
        ],
        [
            "<b>7. Impact of $10 Working Capital Increase on FCF</b><br/><i>(Cash Flow Mechanics)</i>",
            "An increase in Net Working Capital (&Delta;NWC &gt; 0) is a <b>cash outflow</b>. If current assets (e.g., Accounts Receivable) grow faster than current liabilities, cash is tied up in operations. Therefore, UFCF decreases by exactly $10.",
            "Classic junior modeling trap: ensuring candidates understand that asset increases drain cash.",
        ],
    ]
    story.append(make_table(q2_data, [1.85 * inch, 3.65 * inch, 1.90 * inch]))

    # PAGE 3: ARP DODGE SCRIPTS
    story.append(Paragraph("4. WORD-FOR-WORD ARP DODGE PLAYBOOK FOR ADVERSARIAL QUESTIONS", h1_style))
    story.append(Paragraph("Whenever faced with a skepticism or adversarial question regarding your career path or background, execute the 3-step ARP protocol:", body_style))

    arp_data = [
        ["Scenario / Trap Question", "Step 1: Acknowledge (5s)", "Step 2: Reframe (15s)", "Step 3: Pivot to Proof (25s)"],
        [
            "<b>Trap 1: 'You have FP&A / Accounting experience, not 2 years in investment banking.'</b>",
            "<i>'That is an important question, and I appreciate you raising it directly.'</i>",
            "<i>'Investment banking analyst execution lives and dies by financial modeling integrity: 3-statement models, working capital adjustments, debt schedules, and valuation football fields. Over 10 years in FP&A, I have audited balance sheets, reconciled over 1,000 daily transactions at 99.5% accuracy, and built sensitivity models across $50M+ portfolios.'</i>",
            "<i>'To prove day-one readiness for Houlihan Lokey, I built <b>HL-TechMA-ValAI</b>—a complete financial engineering platform that models a $92M ARR SaaS target against 50 comps, generates a multi-method football field, and runs a 5-year Sponsor LBO with dynamic debt sweep delivering 20.1% IRR. I would love to walk through the model mechanics in 60 seconds.'</i>",
        ],
        [
            "<b>Trap 2: 'Can you handle the grueling 80+ hour investment banking workload?'</b>",
            "<i>'I completely understand why stamina and reliability are critical concerns.'</i>",
            "<i>'Throughout my career, particularly leading month-end close across multi-department corporate budgets and completing my master's degree at Pace simultaneously, I have consistently managed high-stress, rapid turnaround deadlines under audit-grade scrutiny with zero formula errors.'</i>",
            "<i>'I am energized by high-velocity transaction environments, and my automated modeling workflow in Excel and Python allows me to turn around complex buyer diligence requests with speed and accuracy.'</i>",
        ],
        [
            "<b>Trap 3: 'What are your salary expectations?'</b>",
            "<i>'I am very flexible and focused on finding the right long-term platform fit.'</i>",
            "<i>'Given Houlihan Lokey’s position as the premier tech M&A advisor, I know your compensation structure is competitive with Street standards for Senior Analysts.'</i>",
            "<i>'I am comfortable with the posted $130,000 base range plus standard discretionary year-end performance incentives. Right now, my focus is demonstrating that I can add immediate value to the team.'</i>",
        ],
    ]
    story.append(make_table(arp_data, [1.50 * inch, 1.50 * inch, 2.15 * inch, 2.25 * inch]))

    story.append(PageBreak())

    # PAGE 4: EXECUTIVE CLOSING & SALARY NEGOTIATION
    story.append(Paragraph("5. EXECUTIVE CLOSING & COMMITMENT LOCK-IN SCRIPT (SYN-002)", h1_style))
    story.append(Paragraph("During the final 10 minutes of the interview, take control of the narrative by asking 3 executive transaction questions, followed immediately by the <b>Commitment Lock-In Close</b>:", body_style))

    story.append(Paragraph("• <b>Strategic M&amp;A Trend Question:</b> <i>'As the No. 1 tech M&amp;A advisor globally, Houlihan Lokey sees incredible deal flow across mid-market software. In the current M&amp;A environment, where are you seeing the biggest bid-ask spread between founder ARR multiple expectations and financial sponsor LBO return hurdles?'</i>", bullet_style))
    story.append(Paragraph("• <b>Subsector Dynamics Question:</b> <i>'In software subsectors like Vertical SaaS vs. PropTech or Supply Chain, how heavily are buyers weighting Rule of 40 balance (FCF margin vs. pure top-line growth) compared to 12 months ago?'</i>", bullet_style))
    story.append(Paragraph("• <b>90-Day Performance Question:</b> <i>'If I join the team and we are sitting at my 90-day review, what specific deliverable or transaction contribution would make you say hiring me was a home run?'</i>", bullet_style))
    story.append(Paragraph("• <b>The Commitment Lock-In Close:</b><br/>"
                           "<i>'Based on our conversation today and the financial modeling frameworks in HL-TechMA-ValAI that we reviewed, is there anything that gives you pause about my ability to immediately hit the desk and execute for Houlihan Lokey’s Tech Group?'</i><br/>"
                           "<i>Why this works:</i> Triggers psychological consistency—the interviewer either states aloud why you are a strong fit, or surfaces any hidden hesitation while you still have time to address it.", bullet_style))

    story.append(Paragraph("6. WORD-FOR-WORD SALARY NEGOTIATION PROTOCOL (MTH-006)", h1_style))
    story.append(Paragraph("• <b>Phase 1: Receiving the Verbal Offer (The 48-Hour Professional Buffer):</b><br/>"
                           "<i>'Thank you so much, [Name]. I am thrilled to receive the offer to join Houlihan Lokey’s Technology Group. Because this is such an important career step, I want to review the full written offer package with my family over the next 48 hours. Can you send over the written details, and let’s connect on [Day] at [Time]?'</i>", bullet_style))
    story.append(Paragraph("• <b>Phase 2: The Base &amp; Signing Bonus Counter-Offer Script:</b><br/>"
                           "<i>'I reviewed the package and could not be more excited about joining the Tech Group. Given the senior modeling responsibilities, my 10+ years of financial analytics experience, and my ability to contribute day-one without training overhead, I was hoping we could align base salary at <b>$140,000</b> (or include a <b>$15,000</b> signing/relocation bonus). If we can bridge that gap, I am ready to sign the agreement today and commit 100%.'</i>", bullet_style))
    story.append(Paragraph("• <b>Phase 3: The 5 Non-Salary Levers to Sequence:</b><br/>"
                           "1. <b>Signing / Transition Bonus:</b> Easiest lever for HR to approve without altering fixed band structure.<br/>"
                           "2. <b>Accelerated 6-Month Comp Review:</b> Written agreement to review base/bonus after first major deal close.<br/>"
                           "3. <b>Level / Title Anchoring:</b> Confirm Senior Analyst Year 2/3 standing positioning for direct Associate promotion track.<br/>"
                           "4. <b>Continuing Education / Certification Stipend:</b> Firm sponsorship for Wall Street Prep / CFA / CPA materials.<br/>"
                           "5. <b>Start Date Buffer:</b> Securing 2–3 weeks between offer and start to ensure complete mental reset.", bullet_style))

    doc.build(story)
    print(f"[OK] Generated HireMe Playbook PDF at: {output_path}")


if __name__ == "__main__":
    p_resume = r"C:\Users\bhupe\Downloads\Bhupesh_Chandra_Dimri_Houlihan_Lokey_Resume.pdf"
    p_cover = r"C:\Users\bhupe\Downloads\Bhupesh_Chandra_Dimri_Houlihan_Lokey_Cover_Letter.pdf"
    p_hireme = r"C:\Users\bhupe\Downloads\Houlihan_Lokey_Tech_Senior_Analyst_HireMe_Playbook.pdf"

    generate_resume_pdf(p_resume)
    generate_cover_letter_pdf(p_cover)
    generate_hireme_playbook_pdf(p_hireme)
