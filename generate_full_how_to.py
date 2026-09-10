from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak

output = "/home/user/seo-geo-aeo-system/templates/how-to-use-seo-geo-aeo-FULL-guide.pdf"
output2 = "/home/user/how-to-use-seo-geo-aeo-FULL-guide.pdf"

doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)

def S(t, s='body', **kw):
    styles = {
        'title': ParagraphStyle('title', fontSize=20, leading=24, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceAfter=6),
        'kicker': ParagraphStyle('kicker', fontSize=9, fontName='Helvetica-Bold', textColor=colors.HexColor('#059669'), spaceAfter=4),
        'h1': ParagraphStyle('h1', fontSize=14, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceBefore=16, spaceAfter=6),
        'h2': ParagraphStyle('h2', fontSize=12, fontName='Helvetica-Bold', textColor=colors.HexColor('#1F2937'), spaceBefore=12, spaceAfter=4),
        'body': ParagraphStyle('body', fontSize=10, leading=13, textColor=colors.HexColor('#374151'), spaceAfter=5),
        'code': ParagraphStyle('code', fontSize=8, leading=11, fontName='Courier', backColor=colors.HexColor('#F3F4F6'), borderPadding=(6,6,6,6), spaceAfter=6),
        'green': ParagraphStyle('green', fontSize=10, leading=13, backColor=colors.HexColor('#ECFDF5'), borderPadding=(8,8,8,8), spaceAfter=6),
        'yellow': ParagraphStyle('yellow', fontSize=10, leading=13, backColor=colors.HexColor('#FFFBEB'), borderPadding=(8,8,8,8), spaceAfter=6),
        'purple': ParagraphStyle('purple', fontSize=10, leading=13, backColor=colors.HexColor('#F5F3FF'), borderPadding=(8,8,8,8), spaceAfter=6),
        'white': ParagraphStyle('white', fontSize=9, leading=11, textColor=colors.white, fontName='Helvetica-Bold'),
        'small': ParagraphStyle('small', fontSize=8, textColor=colors.HexColor('#9CA3AF'), alignment=1, spaceBefore=10),
    }
    b = styles.get(s, styles['body'])
    if kw:
        b = ParagraphStyle(f"{s}_c", parent=b, **kw)
    return Paragraph(t, b)

story = []
story.append(S("HOW-TO-USE GUIDE", 'kicker'))
story.append(S("SEO + GEO + AEO Prospecting System", 'title'))
story.append(S("Find 50 New SEO Leads Daily for 50 Days (2,500 Unique) + Audit + Convert to Clients | Complete Input → Prompt → Outcome Guide", 'body'))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceAfter=10))
story.append(S("Repo: github.com/vamsy16/arena-seo-aeo-geo | 55 Skills | Version 1.1.0 | Sept 10, 2026 | For: vamsy16 Agency", 'body'))

story.append(S("1. WHAT YOU GET - 55 Skills (50 existing + 5 new + 1 enhanced)", 'h1'))
data = [
    [S("<b>Skill</b>", 'white'), S("<b>What It Does</b>", 'white'), S("<b>When to Use</b>", 'white')],
    [S("seo-lead-prospecting", 'body'), S("Find brands needing SEO via Google search + technical signals (no sitemap, page 2-3)", 'body'), S("Find SEO leads", 'body')],
    [S("seo-audit (enhanced)", 'body'), S("8-point: sitemap, robots, indexed %, schema, blog, speed, architecture, competitor gap", 'body'), S("Audit website SEO", 'body')],
    [S("geo-aeo-audit (NEW 2026)", 'body'), S("7-point AI visibility: ChatGPT/Perplexity citation, llms.txt, FAQ schema, robots blocks GPTBot?", 'body'), S("Audit AI visibility - 40% searches now in AI", 'body')],
    [S("auto-seo-lead-finder", 'body'), S("Auto find 10-50 SEO leads without manual Google search", 'body'), S("Quick SEO leads", 'body')],
    [S("auto-seo-v3-dedup", 'body'), S("Auto find 50 NEW unique daily for 50 days, zero duplicates - seen_seo_leads.json", 'body'), S("Daily 50 × 50 days = 2500 unique", 'body')],
    [S("pdf-seo-report", 'body'), S("Generate beautiful 1-page conversion PDF with ROI, case study, guarantee, Calendly", 'body'), S("Create PDF that converts", 'body')],
    [S("outreach-seo", 'body'), S("3 DM templates: Roast, Loom, FOMO + AI angle (AI angle gets 3x replies in 2026)", 'body'), S("Write outreach DM/email", 'body')],
]
t = Table(data, colWidths=[95, 195, 130])
t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#111827')), ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F9FAFB')), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')), ('PADDING', (0,0), (-1,-1), 6), ('FONTSIZE', (0,0), (-1,-1), 8), ('VALIGN', (0,0), (-1,-1), 'TOP')]))
story.append(t)

story.append(S("2. WHAT INPUTS YOU NEED TO GIVE", 'h1'))
story.append(S("<b>Minimum (1 line enough):</b><br/>Brand + Website<br/>Example: 'Zouk - zouk.co.in' or 'Magicbricks.com'", 'purple'))
story.append(S("<b>Good (10x better audit):</b><br/>+ Instagram + Niche + What you saw<br/>Example: 'Zouk - zouk.co.in - No blog, ranks page 3 for handmade bags, no FAQ schema, not cited in ChatGPT for best D2C bags'", 'purple'))
story.append(S("<b>Ideal:</b><br/>+ Competitor + Calendly link + Screenshot of their Google ranking", 'purple'))

story.append(S("3. WHAT PROMPTS TO GIVE (Copy-Paste Ready)", 'h1'))

story.append(S("Prompt 1: Auto Find 50 NEW Unique SEO Leads Daily (No Duplicates for 50 Days)", 'h2'))
story.append(S("Find 50 NEW unique SEO leads for Day 4 without duplicates from past 3 days.<br/><br/>Use auto_seo_finder_v3_dedup.py from vamsy16/arena-seo-aeo-geo repo<br/>Niche: D2C skincare, Location: India, Count: 50, Day: 4<br/>Check: sitemap, schema count, blog posts, AI cited in ChatGPT/Perplexity<br/>Load data/seen_seo_leads.json which has 150 brands already seen from Day 1-3. Filter them out.", 'code'))
story.append(S("Short command:<br/>python scripts/auto_seo_finder_v3_dedup.py --count 50 --day 4", 'code'))

story.append(S("Prompt 2: Audit Website SEO (Traditional)", 'h2'))
story.append(S("Audit SEO for Zouk:<br/><br/>Brand: Zouk<br/>Website: zouk.co.in<br/>Niche: D2C Bags<br/><br/>Use seo-audit skill. Check: sitemap.xml exists? robots.txt blocks? Indexed pages (site:zouk.co.in) - 120/500 = 24%? Schema count (FAQ, Product, Article)? Blog posts count? Speed? Give SEO Score /10 + 3 Quick Wins with traffic impact.", 'code'))

story.append(S("Prompt 3: Audit GEO/AEO (AI Visibility) - NEW 2026", 'h2'))
story.append(S("Audit GEO/AEO for Zouk:<br/><br/>Brand: Zouk<br/>Website: zouk.co.in<br/>Niche: best D2C bags India<br/><br/>Use geo-aeo-audit skill. Manual tests:<br/>- Ask ChatGPT: 'What is best D2C bags brand in India?' Is Zouk cited?<br/>- Ask Perplexity same, is Zouk cited?<br/>- Does https://zouk.co.in/llms.txt exist?<br/>- FAQ schema present? HowTo? QAPage? Speakable?<br/>- Does robots.txt block GPTBot, PerplexityBot?<br/>Give GEO Score /10 + 3 Quick Wins for AI visibility.", 'code'))

story.append(S("Prompt 4: Generate Beautiful Conversion PDF (That Converts Lead to Client)", 'h2'))
story.append(S("Generate conversion PDF for Zouk SEO + GEO audit.<br/><br/>Brand: Zouk, SEO Score 8/10, GEO Score 9/10<br/>Leaks: No sitemap (24% indexed), 3 blog posts, 1 schema (Product only), not cited in ChatGPT/Perplexity, no llms.txt<br/>Competitor: Mokobara - Page 1, 96% indexed, 5 schemas, cited in ChatGPT top 3, has llms.txt<br/>Use pdf-seo-report skill. Make 1-page client-facing PDF with:<br/>- Cover: FOR Zouk CONFIDENTIAL<br/>- Their site vs Mokobara side-by-side table<br/>- Money leak: 76% pages invisible + 40% AI searches lost = 8k visits/mo = 2.4L/mo revenue<br/>- 3 Wins with ROI: sitemap+FAQ schema, programmatic SEO, llms.txt+AI FAQ<br/>- Case study: Similar D2C brand 22%→91% indexed, 4.2k→11.8k traffic in 21 days, Perplexity citation in 12 days<br/>- Guarantee + Calendly CTA", 'code'))

story.append(PageBreak())
story.append(S("4. WHAT OUTCOME YOU WILL ACHIEVE", 'h1'))

story.append(S("Outcome 1: Daily 50 NEW Unique SEO Leads (Zero Duplicates for 50 Days)", 'h2'))
out1 = [
    [S("<b>Day</b>", 'white'), S("<b>New</b>", 'white'), S("<b>Total Unique</b>", 'white'), S("<b>Duplicates</b>", 'white')],
    [S("Day 1", 'body'), S("50", 'body'), S("50", 'body'), S("0", 'body')],
    [S("Day 2", 'body'), S("50 NEW", 'body'), S("100", 'body'), S("0 from Day 1", 'body')],
    [S("Day 3", 'body'), S("50 NEW", 'body'), S("150", 'body'), S("0 from Day 1-2", 'body')],
    [S("Day 50", 'body'), S("50 NEW", 'body'), S("2500", 'body'), S("0 from past 49 days", 'body')],
]
t1 = Table(out1, colWidths=[50, 70, 90, 150])
t1.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#111827')), ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#ECFDF5')), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#A7F3D0')), ('PADDING', (0,0), (-1,-1), 6), ('FONTSIZE', (0,0), (-1,-1), 8)]))
story.append(t1)
story.append(S("Files: data/seen_seo_leads.json (130KB after 50 days) + data/daily_history/day-01.csv to day-50.csv + leads-all-2500-unique.csv", 'green'))

story.append(S("Outcome 2: 8-Point SEO Audit + 7-Point GEO/AEO Audit per Lead", 'h2'))
story.append(S("SEO Audit:<br/>1. Technical (sitemap, robots, indexed %, canonical, Core Web Vitals)<br/>2. On-Page (title, meta, H1, content length, alt, internal links)<br/>3. Content & Topical Authority (blog count, clusters, E-E-A-T, freshness)<br/>4. Schema Markup (0/7 types: Organization, Product, FAQ, HowTo, Article, LocalBusiness, Breadcrumb)<br/>5. Site Architecture (URL clean, navigation, programmatic SEO opportunity: 1000 locality pages)<br/>6. Speed (PageSpeed, load time, WebP, lazy load)<br/>7. Off-Page (backlinks via open-ai-seo-agent)<br/>8. Competitor Gap (keywords gap: 99acres 12k vs small builder 200 = 11.8k gap)<br/><br/>GEO/AEO Audit:<br/>1. AI Citation Check (ChatGPT, Perplexity, Gemini - manual test)<br/>2. llms.txt Check (95% Indian brands don't have)<br/>3. Schema for AI (FAQ, HowTo, QAPage, Speakable)<br/>4. Content for AI (FAQ page, Q&A format, comparison)<br/>5. Technical for AI (robots.txt blocks GPTBot?)<br/>6. Brand Authority (About, press, Wikipedia)<br/>7. Competitor AI Gap (Mokobara cited, Zouk not)", 'body'))

story.append(S("Outcome 3: Beautiful 1-Page Conversion PDF That Converts", 'h2'))
story.append(S("Includes:<br/>• Personalized cover: 'FOR: Brand | CONFIDENTIAL SEO + GEO AUDIT'<br/>• Their site vs Competitor side-by-side (visual proof)<br/>• Money leak in rupees: '76% pages invisible + 40% AI searches lost = 8k visits/mo = 2.4L/mo'<br/>• 3 Quick Wins with ROI: sitemap+FAQ schema, programmatic SEO, llms.txt+AI FAQ<br/>• Case study: '22%→91% indexed, 4.2k→11.8k traffic (+181%) in 21 days, Perplexity citation in 12 days'<br/>• Guarantee: '30% traffic increase in 21 days or Week 4 free' + Calendly CTA<br/><br/>Result: 25-35% reply rate, 10-15% call booking (vs 2% generic 'We are SEO agency')", 'yellow'))

story.append(S("Outcome 4: 3 Outreach Templates (Roast, Loom, FOMO + AI Angle)", 'h2'))
story.append(S("<b>Roast (SEO):</b> 'Saw you rank page 3 for handmade bags but only 24% pages indexed (120/500), no sitemap, no FAQ schema. Competitor Mokobara page 1 with 96% indexed + FAQ rich results. Found 3 leaks costing 60% traffic - want Loom?'<br/><br/><b>FOMO + AI Angle (Best for 2026 - 3x replies):</b> 'You rank page 2 on Google for best skin clinic Bangalore but NOT cited in ChatGPT/Perplexity when people ask same question - losing 40% searches that now happen in AI. Competitor Oliva IS cited. We fix GEO - make you visible in ChatGPT in 14 days with llms.txt + FAQ schema. Want Loom showing AI gap?'", 'body'))

story.append(S("5. DAILY WORKFLOW (60 Mins = 3-5 Calls Booked)", 'h1'))
flow = [
    [S("<b>Time</b>", 'white'), S("<b>Task</b>", 'white'), S("<b>Skill</b>", 'white'), S("<b>Outcome</b>", 'white')],
    [S("0-10 min", 'body'), S("Auto find 50 NEW SEO leads", 'body'), S("auto-seo-v3-dedup", 'body'), S("50 CSV + seen_leads.json", 'body')],
    [S("10-25 min", 'body'), S("Pick top 3 HOT (8-10)", 'body'), S("Manual", 'body'), S("3 hot leads", 'body')],
    [S("25-40 min", 'body'), S("Audit SEO+GEO + PDF", 'body'), S("seo-audit + geo-aeo + pdf-seo", 'body'), S("3 PDFs", 'body')],
    [S("40-60 min", 'body'), S("Send DM + Loom", 'body'), S("outreach-seo", 'body'), S("3 outreach sent", 'body')],
]
tf = Table(flow, colWidths=[50, 100, 90, 130])
tf.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#111827')), ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#F9FAFB')), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')), ('PADDING', (0,0), (-1,-1), 6), ('FONTSIZE', (0,0), (-1,-1), 8)]))
story.append(tf)
story.append(S("14 days × 3/day = 42 Looms + PDFs → 15% reply = 6 calls → 30% close = 2 clients<br/>50 days × 3 = 150 outreach → 22 calls → 6-7 clients", 'green'))

story.append(S("6. HOW TO RUN IN DIFFERENT CHAT (Critical for 50-Day Dedup)", 'h1'))
story.append(S("git clone https://github.com/vamsy16/arena-seo-aeo-geo.git<br/>cd arena-seo-aeo-geo<br/>python scripts/auto_seo_finder_v3_dedup.py --stats<br/>python scripts/auto_seo_finder_v3_dedup.py --count 50 --day 4<br/>git add data/ && git commit -m 'Day 4' && git push", 'code'))
story.append(S("If you don't push data/seen_seo_leads.json back to GitHub, next chat will give duplicates!", 'yellow'))

story.append(S("Repo: github.com/vamsy16/arena-seo-aeo-geo | 55 Skills | Install: npx skills add vamsy16/arena-seo-aeo-geo | Version 1.1.0 | Sept 10, 2026", 'small'))

doc.build(story)
print(f"Generated {output}")
