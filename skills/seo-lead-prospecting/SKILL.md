---
name: seo-lead-prospecting
description: "When user wants to FIND brands that need SEO, GEO, AEO services. Use when user says 'find SEO leads', 'find brands needing SEO', 'SEO prospecting', 'find websites with bad SEO', 'GEO leads', 'AEO leads'. Finds brands with weak organic traffic, not ranking, not cited by AI. For auditing found lead, see seo-audit. For GEO/AEO audit, see geo-aeo-audit."
metadata:
  version: 1.0.0
---

# SEO Lead Prospecting - Find Brands Needing SEO/GEO/AEO

Find brands that NEED SEO, GEO (Generative Engine Optimization), AEO (Answer Engine Optimization) - not brands already ranking.

## Golden Rule
Find websites with traffic but weak SEO, or good product but zero AI citations.

## 4 Methods to Find SEO Leads

### METHOD 1: Google Search + SEO Signals (Best for Traditional SEO)

**Search for:**
- `site:brand.com` - Check indexed pages vs actual pages
- `"brand" + "blog"` - Do they have blog? If no blog = HOT SEO lead
- Search keyword + location: `best skin clinic Bangalore` - Who ranks page 2-3? They need SEO
- `intitle:"best" + niche` - Find listicles where brand NOT mentioned

**Qualify GOOD SEO lead:**
- Website exists but blog has <10 posts
- Ranks page 2-3 for main keyword (e.g., "2BHK in Whitefield" - Magicbricks ranks #1, but small builder ranks #15 = needs SEO)
- No schema markup (check source)
- Slow site (>3s)
- No internal linking

**Tools:**
- `seo-audit` skill (technical audit)
- `claude-seo` (31 skills - deep SEO)
- `open-ai-seo-agent` (free Ahrefs/Semrush alternative using Search Console)
- `programmatic-seo` (scaled pages)

### METHOD 2: AI Visibility Check (Best for GEO/AEO Leads) - NEW 2026

**GEO = Generative Engine Optimization (Optimize for ChatGPT, Perplexity, Gemini)**
**AEO = Answer Engine Optimization (Optimize for AI answers, featured snippets)**

**How to find GEO/AEO leads:**

1. Ask ChatGPT/Perplexity: "What is best [niche] in [location]?" 
   - Example: "What is best skin clinic in Bangalore?"
   - If brand NOT cited in AI answer = GEO lead (needs AI optimization)

2. Check if brand has:
   - No FAQ schema
   - No HowTo schema
   - No Speakable schema
   - No llms.txt file (new standard for AI)
   - No AI citation optimization

**Qualify HOT GEO/AEO lead:**
- Good Google ranking but ZERO mention in ChatGPT/Perplexity
- No FAQ page
- No structured data for AI
- No blog optimized for AI citations

**Tools:**
- `ai-seo` skill (optimize for AI search, get cited by LLMs)
- `claude-seo` → semantic clustering, E-E-A-T

### METHOD 3: Competitor Gap (Best for All)

Use `competitor-x-ray` + `funnel-spy`:
1. Find competitor who ranks #1
2. Check what keywords they rank for that lead doesn't
3. Example: 99acres ranks for 12k keywords, Magicbricks for 10k, small builder for 200 = gap = opportunity

### METHOD 4: Technical SEO Signals (Automated)

Use `firecrawl` to check:
- No sitemap.xml
- No robots.txt
- No schema markup
- No meta descriptions
- Images without alt text
- No internal linking

If 3+ missing = HOT SEO lead.

## Lead Scoring for SEO (0-10)

- [2] No blog or <10 posts
- [2] Ranks page 2-3 for main keyword (not page 1)
- [2] No schema markup (FAQ, HowTo, Product)
- [2] Slow site (>3s) or no sitemap
- [2] Zero AI citations (not mentioned in ChatGPT/Perplexity for niche query)

6+ = HOT SEO/GEO/AEO lead

## What to Give for Audit

`Brand - Website - What you saw`

Example:
1. `Zouk - zouk.co.in - No blog, ranks page 3 for 'handmade bags', no FAQ schema, not cited in ChatGPT for 'best D2C bags'`
2. `Dr Batra's - drbatras.com - Has blog but no schema, slow 4.2s, not in Perplexity answer for 'best skin clinic Bangalore'`
3. `Adarsh Group - adarshdevelopers.com - Ranks page 2 for 'flats in Whitefield', no programmatic SEO for locality pages`

## Daily Workflow (60 mins)

- 0-20 min: Find 10 leads via Google search + AI visibility check
- 20-30 min: Put in CSV
- 30-45 min: Run seo-audit + geo-aeo-audit for top 3
- 45-60 min: Send personalized Loom + PDF

## Related Skills

- `seo-audit`: Technical + on-page audit
- `geo-aeo-audit`: AI citation audit
- `auto-seo-lead-finder`: Automate finding
- `claude-seo`: Deep SEO (31 skills)
- `ai-seo`: Optimize for AI search
