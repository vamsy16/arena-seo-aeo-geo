# SEO + GEO + AEO Prospecting System

> **Find brands needing SEO/GEO/AEO + Audit + Convert to Clients**
> Similar to Performance Marketing system, but for SEO leads

**For:** vamsy16 | **Created:** Sept 10, 2026 | **Type:** Agent Skills | **Status:** Local review (NOT pushed to GitHub yet)

---

## What is SEO + GEO + AEO?

- **SEO:** Traditional - Rank on Google (sitemap, schema, blog, speed)
- **GEO:** Generative Engine Optimization - Be cited by ChatGPT, Perplexity, Gemini (NEW 2026, 40% searches now in AI)
- **AEO:** Answer Engine Optimization - Appear in featured snippets, People Also Ask, AI overviews

**Why HUGE in 2026:**
- 40% searches happen in ChatGPT/Perplexity, not Google
- Brand ranking #1 on Google but NOT cited in AI = losing 40% traffic
- 95% of agencies don't offer GEO/AEO = blue ocean, premium pricing

---

## 6 Skills (Same Structure as Performance Marketing)

| Skill | What It Does | When to Use |
|-------|--------------|-------------|
| `seo-lead-prospecting` | Find brands needing SEO via Google search + technical signals | Find SEO leads manually |
| `seo-audit` | 8-point technical + on-page + content + schema + speed audit | Audit website SEO |
| `geo-aeo-audit` | 7-point AI visibility audit: ChatGPT/Perplexity citation, llms.txt, FAQ schema | Audit AI visibility |
| `auto-seo-lead-finder` | Auto find 10-50 leads without manual Google/AI checks | Auto find SEO leads |
| `pdf-seo-report` | Generate beautiful conversion PDF with ROI | Create PDF that converts |
| `outreach-seo` | 3 DM templates: Roast, Loom, FOMO + AI angle | Write outreach |

**Plus V3 dedup system:** 50 days × 50 leads = 2500 unique, zero duplicates (same as performance marketing)

---

## How They Work Together

```
Find (seo-lead-prospecting / auto-seo-lead-finder)
  → Audit (seo-audit + geo-aeo-audit)
  → PDF (pdf-seo-report)
  → Outreach (outreach-seo)
```

---

## Inputs Needed

**Minimum:**
- Brand + Website (e.g., "Zouk - zouk.co.in")

**Good:**
- + Instagram, Niche, What you saw (e.g., "No blog, ranks page 3, no FAQ schema, not cited in ChatGPT")

**Ideal:**
- + Competitor, Ad Library link, Calendly

---

## Prompts (Copy-Paste)

### Auto Find 50 SEO Leads (No Duplicates for 50 Days)

```
Find 50 NEW unique SEO leads for Day 1 without duplicates.

Use auto-seo-lead-finder from seo-geo-aeo-system
Niche: D2C skincare, Location: India, Count: 50, Day: 1
Type: Both SEO + GEO/AEO

Check: sitemap, schema count, blog posts, AI cited in ChatGPT/Perplexity
```

### Audit Website SEO

```
Audit SEO for Zouk:

Brand: Zouk
Website: zouk.co.in
Niche: D2C Bags

Use seo-audit skill. Check sitemap.xml, robots.txt, indexed pages (site:zouk.co.in), schema (FAQ, Product), blog count, speed, internal linking. Give SEO Score /10 + 3 Quick Wins + ROI.
```

### Audit GEO/AEO (AI Visibility)

```
Audit GEO/AEO for Zouk:

Brand: Zouk
Website: zouk.co.in
Niche: best D2C bags India

Use geo-aeo-audit skill. Check:
- Is Zouk cited in ChatGPT when asking "best D2C bags India"?
- Is it cited in Perplexity?
- Does zouk.co.in/llms.txt exist?
- FAQ schema present?
- Robots.txt blocks GPTBot?
Give GEO Score /10 + 3 Quick Wins for AI visibility.
```

### Generate Conversion PDF + Outreach

```
Generate conversion PDF + outreach DM for Zouk SEO audit.

Brand: Zouk, SEO Score 8/10, GEO Score 9/10
Leaks: No sitemap (24% indexed), 3 blog posts, no FAQ schema, not cited in ChatGPT/Perplexity
Competitor: Mokobara ranks page 1 + cited in AI
Use pdf-seo-report + outreach-seo skills.
Make PDF client-facing with ROI, case study, Calendly CTA.
```

---

## Outcomes

1. **50 NEW unique SEO leads daily for 50 days** = 2500 total, zero duplicates (seen_leads.json)
2. **8-point SEO audit + 7-point GEO/AEO audit** per lead
3. **Beautiful 1-page conversion PDF** with money leak in rupees, ROI, case study, guarantee, Calendly
4. **3 outreach templates** (Roast, Loom, FOMO + AI angle) - AI angle gets 3x replies in 2026

---

## Sample Audit: Magicbricks.com SEO + GEO

**SEO Score: 5/10**
- Sitemap: Yes but heavy, 28 chunks
- Robots: OK
- Indexed: ~60% (heavy site)
- Schema: Product? No, FAQ? No, only basic
- Blog: Yes but not optimized for SEO
- Speed: Slow (heavy homepage)
- Programmatic opportunity: 1000 locality pages possible (/flats-in-whitefield etc.)

**GEO Score: 8/10 (Needs GEO)**
- ChatGPT: Ask "best property site India" → 99acres cited, Magicbricks sometimes, but not for "best site for Bangalore flats"
- llms.txt: No
- FAQ schema: No
- Robots blocks AI? No, but no optimization
- Opportunity: Add llms.txt + FAQ schema + comparison content

**Quick Wins:**
1. Add sitemap + FAQ schema → +40% indexed, +15% CTR
2. Programmatic SEO: 50 locality pages → +2000 visits/mo
3. Add llms.txt + AI FAQ page → Cited in ChatGPT in 14 days

---

## Installation (When Ready to Push to New Repo)

```bash
# Create new repo: seo-geo-aeo-prospecting
# Then:
npx skills add vamsy16/seo-geo-aeo-prospecting
```

For now, local review only - NOT pushed to arena-performance-marketing.

---

## Files

```
seo-geo-aeo-system/
├── skills/
│   ├── seo-lead-prospecting/
│   ├── seo-audit/
│   ├── geo-aeo-audit/
│   ├── auto-seo-lead-finder/
│   ├── pdf-seo-report/
│   └── outreach-seo/
├── templates/
├── scripts/
│   ├── auto_seo_finder.py
│   └── auto_seo_finder_v3_dedup.py
├── data/
│   └── seen_seo_leads.json
└── README.md
```

---

**Status:** Local review - NOT pushed to GitHub yet. Once approved, will push to new repo `vamsy16/seo-geo-aeo-prospecting`
