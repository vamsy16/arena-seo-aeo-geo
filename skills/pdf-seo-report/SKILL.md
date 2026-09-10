---
name: pdf-seo-report
description: "When user wants to generate beautiful attractive PDF SEO/GEO/AEO audit report to send to leads. Use when user says 'generate SEO PDF', 'create SEO audit PDF', 'beautiful SEO report', 'PDF to send to SEO lead'. Converts seo-audit or geo-aeo-audit into branded visual PDF with scores, leaks, quick wins, ROI, with Smart Pursuit branding. For audit itself, see seo-audit or geo-aeo-audit."
metadata:
  version: 1.2.0
---

# PDF SEO Report Generator - Beautiful Audit PDFs for SEO/GEO/AEO Outreach (Smart Pursuit Branded)

Generate beautiful PDFs that convert SEO/GEO/AEO leads to clients.

**Agency Branding (ALWAYS include in NEW PDFs generated after audit):**
- Agency Name: Smart Pursuit
- Contact: 7095024220
- Email: smartpursuit3@gmail.com
- Do NOT update existing PDFs (sample-seo-audit-magicbricks.md, zouk-seo-geo-conversion.pdf old version) - keep them as is. Only NEW lead PDFs after audit should have Smart Pursuit branding.

## Structure (1-2 pages, conversion-focused)

1. **Cover:** FOR: [BRAND] | CONFIDENTIAL SEO + GEO AUDIT | Prepared by Smart Pursuit
2. **Executive Summary (Purple)**
3. **SEO Audit Table + GEO/AEO Table (ChatGPT/Perplexity cited?)**
4. **3 Quick Wins with ROI (Green boxes)**
5. **Case Study**
6. **How We Work + Guarantee**
7. **CTA Box (Dark) with Smart Pursuit Contact:**
   ```
   📞 Call/WhatsApp: 7095024220
   📧 Email: smartpursuit3@gmail.com
   — Smart Pursuit Team - SEO + GEO + AEO
   ```
8. **Footer:** Prepared by Smart Pursuit • 📞 7095024220 • 📧 smartpursuit3@gmail.com

## Templates

- Existing PDFs (DO NOT UPDATE): Keep old versions as is
- NEW template for future leads: smart-pursuit-seo-geo-TEMPLATE.pdf (has [BRAND NAME] placeholder + Smart Pursuit contact) - USE THIS as base for all NEW lead PDFs after audit

## How to Generate

Use reportlab. See generate_branded_pdfs.py. Always include Smart Pursuit contact in CTA and footer for NEW PDFs.

## Workflow

1. Run seo-audit + geo-aeo-audit for brand
2. Run pdf-seo-report → generates [brand]-seo-geo-audit.pdf with Smart Pursuit branding
3. Run outreach-seo → DM says "I made quick audit PDF for you..."

## Related Skills

- `seo-audit`, `geo-aeo-audit`, `outreach-seo`
