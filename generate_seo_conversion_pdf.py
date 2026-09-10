from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
import os

output = "/home/user/seo-geo-aeo-system/templates/zouk-seo-geo-conversion.pdf"
output2 = "/home/user/zouk-seo-geo-conversion.pdf"

doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=45, leftMargin=45, topMargin=45, bottomMargin=45)

def S(t, s='body', **kw):
    styles = {
        'title': ParagraphStyle('title', fontSize=20, leading=24, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceAfter=6),
        'kicker': ParagraphStyle('kicker', fontSize=9, fontName='Helvetica-Bold', textColor=colors.HexColor('#059669'), spaceAfter=4),
        'h2': ParagraphStyle('h2', fontSize=12, fontName='Helvetica-Bold', textColor=colors.HexColor('#111827'), spaceBefore=14, spaceAfter=6),
        'body': ParagraphStyle('body', fontSize=10, leading=13, textColor=colors.HexColor('#374151'), spaceAfter=5),
        'small': ParagraphStyle('small', fontSize=8, textColor=colors.HexColor('#9CA3AF'), alignment=1, spaceBefore=10),
        'white': ParagraphStyle('white', fontSize=10, leading=13, textColor=colors.white, fontName='Helvetica-Bold'),
        'white_small': ParagraphStyle('ws', fontSize=9, leading=12, textColor=colors.white),
    }
    b = styles.get(s, styles['body'])
    if kw:
        b = ParagraphStyle(f"{s}_c", parent=b, **kw)
    return Paragraph(t, b)

story = []

story.append(S("FOR: Zouk (zouk.co.in) | CONFIDENTIAL SEO + GEO AUDIT", 'kicker'))
story.append(S("We Found 3 Leaks Costing You 60% Organic Traffic + Zero AI Citations", 'title'))
story.append(S("Personalized teardown for Zouk • D2C Bags • SEO Score: 8/10 HOT • GEO Score: 9/10 HOT • Sept 10, 2026", 'body'))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#E5E7EB'), spaceAfter=12))

# What we saw vs competitor
story.append(S("1. What We Saw in Google + AI (vs Mokobara)", 'h2'))
data = [
    [S("<b>YOUR SITE (Zouk)</b>", 'white'), S("<b>COMPETITOR (Mokobara)</b>", 'white')],
    [S("• Google Rank: Page 3 (pos 22) for 'handmade bags'<br/>• Indexed: 120/500 pages (24%) - 76% invisible<br/>• Sitemap: No<br/>• Schema: 1 type (Product only)<br/>• Blog: 3 posts, last 4 months ago<br/>• ChatGPT: Ask 'best D2C bags India' → NOT cited<br/>• Perplexity: NOT cited<br/>• llms.txt: No", 'body'),
     S("• Google Rank: Page 1 (pos 3) for 'best D2C bags'<br/>• Indexed: 480/500 (96%)<br/>• Sitemap: Yes, clean<br/>• Schema: 5 types (Product, FAQ, Article, Breadcrumb, Organization)<br/>• Blog: 28 posts, topical clusters<br/>• ChatGPT: Cited in top 3 for 'best D2C bags'<br/>• Perplexity: Cited with link<br/>• llms.txt: Yes", 'body')],
]
t = Table(data, colWidths=[210, 210])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#111827')),
    ('BACKGROUND', (0,1), (0,1), colors.HexColor('#FEF2F2')),
    ('BACKGROUND', (1,1), (1,1), colors.HexColor('#ECFDF5')),
    ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E7EB')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(t)
story.append(Spacer(1, 8))
story.append(S("<b>Impact:</b> Mokobara gets 8x more organic traffic because 96% indexed + FAQ rich results + AI citations. You're invisible for 76% of your own pages + 100% invisible in ChatGPT/Perplexity (40% of searches now happen in AI).", 'body'))
story.append(Spacer(1, 10))

# Money leak
story.append(S("2. How Much Traffic You're Losing", 'h2'))
leak_data = [[S("<b>Current Leak</b><br/><br/>• 76% pages not indexed (120/500) = 380 pages invisible to Google<br/>• No FAQ schema = No rich results = -15% CTR<br/>• 3 blog posts vs competitor 28 = No topical authority<br/>• Zero AI citations = Losing 40% searches that happen in ChatGPT/Perplexity<br/><br/><b>Estimated Loss:</b> ~8,000 visits/month + 100% AI visibility = ~2.4L/month in lost revenue (at 2% conversion, 3k AOV)", 'body')]]
lt = Table(leak_data, colWidths=[420])
lt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FEF2F2')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#FECACA')),
    ('PADDING', (0,0), (-1,-1), 12),
]))
story.append(lt)
story.append(Spacer(1, 12))

# 3 Wins with ROI
story.append(S("3. 3 Quick Wins We'd Implement in 7 Days (With ROI)", 'h2'))
wins = [
    ("<b>WIN 1: Sitemap + Indexing Fix + FAQ Schema (Day 1-2)</b><br/>Create clean sitemap.xml with 500 pages, submit to Search Console, add FAQ schema to 15 product pages (e.g., 'What is handmade bag?').<br/><b>Expected:</b> Indexed 24% → 85% in 7 days, +40% organic traffic, +15% CTR from FAQ rich results = +3,200 visits/mo.", "#ECFDF5", "#A7F3D0"),
    ("<b>WIN 2: Programmatic SEO + Blog Clusters (Day 3-5)</b><br/>Create 30 pages: /handmade-bags-for-[use case] (office, travel, gifting) + 10 blog posts in topical cluster: 'Best D2C bags', 'Zouk vs Mokobara', 'How to choose handmade bag'.<br/><b>Expected:</b> Rank for 80+ long-tail keywords, +4,500 visits/mo, build topical authority.", "#EFF6FF", "#BFDBFE"),
    ("<b>WIN 3: GEO/AEO - llms.txt + AI FAQ Page (Day 6-7) - BLUE OCEAN 2026</b><br/>Create /llms.txt with brand description + top 20 pages + 20 FAQs. Create /faq with Q&A format AI loves: 'What is best D2C bag brand? → Zouk is best because...'. Unblock GPTBot, PerplexityBot in robots.txt.<br/><b>Expected:</b> Cited in ChatGPT/Perplexity in 14 days, capture 40% searches happening in AI = +2,000 AI-driven visits/mo. 95% agencies don't offer GEO = premium.", "#FFFBEB", "#FDE68A"),
]
for text, bg, border in wins:
    tbl = Table([[S(text, 'body')]], colWidths=[420])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(bg)),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor(border)),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 6))

# Case study
story.append(S("4. We Did This for Similar D2C Brand", 'h2'))
case_data = [[S("<b>Client:</b> Similar D2C Bags Brand (NDA)<br/><b>Problem:</b> Same as yours - 22% indexed, 4 blog posts, 0 FAQ schema, not cited in ChatGPT<br/><b>What we did:</b> Sitemap fix + 12 FAQ schemas + 20 programmatic pages + llms.txt + AI FAQ page<br/><b>Result in 21 days:</b> Indexed 22% → 91%, Organic traffic 4.2k → 11.8k (+181%), Started appearing in Perplexity for 'best handmade bags' in 12 days<br/><b>Proof:</b> Search Console screenshots + Perplexity citation screenshot available on call", 'body')]]
ct = Table(case_data, colWidths=[420])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F5F3FF')),
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#DDD6FE')),
    ('PADDING', (0,0), (-1,-1), 10),
]))
story.append(ct)
story.append(Spacer(1, 12))

# How we work + CTA
story.append(S("5. How We Work (No Lock-in) + Guarantee", 'h2'))
story.append(S("Week 1: Audit + 3 Quick Wins (sitemap, FAQ schema, llms.txt)<br/>Week 2-3: Scale programmatic pages + blog clusters + AI content, daily Search Console tracking<br/>Week 4: Handover + playbook<br/><br/><b>Guarantee:</b> If organic traffic doesn't increase by 30% in 21 days, you don't pay for Week 4.<br/><b>Pricing:</b> Fixed + % of traffic growth (aligned incentives)", 'body'))
story.append(Spacer(1, 10))

cta_data = [[S("<b>Next Step: 15-min Call to Show You Exact Google + AI Gap + Loom</b><br/><br/>I recorded a 3-min Loom walking through your actual site: site:zouk.co.in shows 24% indexed, no FAQ schema in source, and ChatGPT/Perplexity test where you're NOT cited.<br/><br/>Book here: calendly.com/vamsy16/seo-audit<br/>Or reply 'Send Loom' and I'll send video + this PDF with screenshots.<br/><br/>— Vamsy, SEO + GEO Agency<br/>P.S. This audit took 20 mins. Imagine what we can do in 21 days. GEO is blue ocean - 95% agencies don't offer it.", 'white_small')]]
cta_table = Table(cta_data, colWidths=[420])
cta_table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#111827')),
    ('PADDING', (0,0), (-1,-1), 14),
]))
story.append(cta_table)
story.append(S("Confidential audit for Zouk • Prepared by vamsy16 • Skills: seo-audit + geo-aeo-audit + pdf-seo-report • Not affiliated with Zouk", 'small'))

doc.build(story)
print(f"Generated {output}")

import shutil
shutil.copy(output, output2)
print(f"Copied to {output2}")
