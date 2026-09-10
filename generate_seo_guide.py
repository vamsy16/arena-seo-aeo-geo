from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import os

output = "/home/user/seo-geo-aeo-system/templates/how-to-use-seo-geo-aeo-guide.pdf"
doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)

def S(t, s='body', **kw):
    styles = {
        'title': ParagraphStyle('title', fontSize=20, leading=24, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceAfter=6),
        'kicker': ParagraphStyle('kicker', fontSize=9, fontName='Helvetica-Bold', textColor=colors.HexColor('#059669'), spaceAfter=4),
        'h1': ParagraphStyle('h1', fontSize=14, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceBefore=16, spaceAfter=6),
        'h2': ParagraphStyle('h2', fontSize=12, fontName='Helvetica-Bold', textColor=colors.HexColor('#1F2937'), spaceBefore=12, spaceAfter=4),
        'body': ParagraphStyle('body', fontSize=10, leading=13, textColor=colors.HexColor('#374151'), spaceAfter=5),
        'code': ParagraphStyle('code', fontSize=9, leading=11, fontName='Courier', backColor=colors.HexColor('#F3F4F6'), borderPadding=(6,6,6,6), spaceAfter=6),
        'green': ParagraphStyle('green', fontSize=10, leading=13, backColor=colors.HexColor('#ECFDF5'), borderPadding=(8,8,8,8), spaceAfter=6),
        'small': ParagraphStyle('small', fontSize=8, textColor=colors.HexColor('#9CA3AF'), alignment=1, spaceBefore=10),
    }
    b = styles.get(s, styles['body'])
    if kw:
        b = ParagraphStyle(f"{s}_c", parent=b, **kw)
    return Paragraph(t, b)

story = []
story.append(S("HOW-TO-USE GUIDE", 'kicker'))
story.append(S("SEO + GEO + AEO Prospecting System", 'title'))
story.append(S("Find 50 New SEO Leads Daily for 50 Days (2,500 Unique) + Audit + Convert | Input → Prompt → Outcome", 'body'))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceAfter=10))

story.append(S("1. WHAT YOU GET - 6 Skills", 'h1'))
story.append(S("• seo-lead-prospecting: Find brands needing SEO via Google search + technical signals<br/>• seo-audit: 8-point technical + on-page + schema + speed audit<br/>• geo-aeo-audit: 7-point AI visibility - ChatGPT/Perplexity citation, llms.txt, FAQ schema<br/>• auto-seo-lead-finder: Auto find 10-50 leads without manual search<br/>• auto-seo-finder-v3-dedup: 50 days × 50 = 2500 unique zero duplicates<br/>• pdf-seo-report + outreach-seo: Beautiful PDF + 3 DM templates (Roast, Loom, FOMO + AI angle)", 'body'))

story.append(S("2. INPUTS NEEDED", 'h1'))
story.append(S("<b>Minimum:</b> Brand + Website (e.g., 'Zouk - zouk.co.in')<br/><b>Good:</b> + Niche + What you saw (e.g., 'No blog, ranks page 3, no FAQ schema, not cited in ChatGPT')<br/><b>Ideal:</b> + Competitor + Calendly", 'body'))

story.append(S("3. PROMPTS (Copy-Paste)", 'h1'))
story.append(S("Auto Find 50 NEW SEO Leads Daily:", 'h2'))
story.append(S("Find 50 NEW unique SEO leads for Day 1 without duplicates.<br/>Use auto_seo_finder_v3_dedup.py from seo-geo-aeo-system<br/>Niche: D2C skincare, Location: India, Count: 50, Day: 1<br/>Check: sitemap, schema count, blog posts, AI cited in ChatGPT/Perplexity<br/>Load data/seen_seo_leads.json", 'code'))

story.append(S("Audit SEO:", 'h2'))
story.append(S("Audit SEO for Zouk:<br/>Brand: Zouk, Website: zouk.co.in, Niche: D2C Bags<br/>Use seo-audit skill. Check sitemap.xml, robots.txt, indexed pages (site:zouk.co.in), schema (FAQ, Product), blog count, speed. Give SEO Score /10 + 3 Quick Wins.", 'code'))

story.append(S("Audit GEO/AEO (AI Visibility):", 'h2'))
story.append(S("Audit GEO/AEO for Zouk:<br/>Brand: Zouk, Website: zouk.co.in, Niche: best D2C bags India<br/>Use geo-aeo-audit skill. Check: Is Zouk cited in ChatGPT for 'best D2C bags India'? Perplexity? Does /llms.txt exist? FAQ schema? Robots blocks GPTBot? Give GEO Score /10 + 3 Wins.", 'code'))

story.append(S("4. OUTCOMES", 'h1'))
story.append(S("• 50 NEW unique SEO leads daily × 50 days = 2500 total, zero duplicates (seen_seo_leads.json)<br/>• 8-point SEO audit + 7-point GEO/AEO audit per lead<br/>• Beautiful 1-page conversion PDF with ROI, case study, Calendly CTA → 25-35% reply<br/>• 3 outreach templates: Roast, Loom, FOMO + AI angle (AI angle gets 3x replies in 2026)", 'body'))

story.append(S("5. WHY GEO/AEO HUGE IN 2026", 'h1'))
story.append(S("• 40% searches now in ChatGPT/Perplexity, not Google<br/>• Brand ranking #1 on Google but NOT cited in AI = losing 40% traffic<br/>• 95% agencies don't offer GEO/AEO = blue ocean, premium pricing<br/>• You can charge: 'We make you visible in ChatGPT in 14 days with llms.txt + FAQ schema'", 'green'))

story.append(S("Repo: seo-geo-aeo-system (local review, NOT pushed to GitHub yet) | 6 Skills | Version 1.0.0 | Sept 10, 2026", 'small'))

doc.build(story)
print(f"Generated {output}")
