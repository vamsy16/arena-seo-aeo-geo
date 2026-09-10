---
name: auto-seo-lead-finder
description: "When user wants to automatically find brands needing SEO/GEO/AEO without manual Google search or AI checks. Use when user says 'auto find SEO leads', 'scrape SEO leads', 'give me SEO leads automatically', 'find brands with bad SEO'. Automates finding via firecrawl, sitemap checks, schema checks, AI citation checks. For manual methods, see seo-lead-prospecting."
metadata:
  version: 1.0.0
---

# Auto SEO Lead Finder - Automated SEO/GEO/AEO Lead Discovery

Automatically find brands needing SEO/GEO/AEO WITHOUT manual Google search or ChatGPT checks.

## Problem with Manual

Traditional SEO prospecting requires:
- Manual Google search for each keyword
- Check site:brand.com, sitemap, robots.txt one by one
- Ask ChatGPT/Perplexity for each brand if cited
- Time consuming (30 mins for 10 leads)

## Automated Solution

### Method 1: Firecrawl + Technical Checks (Automated)

Use `firecrawl` skill (JS rendering):

Workflow:
1. User gives niche + location: "D2C skincare India" or "Real estate Bangalore"
2. Generate 20 keywords (e.g., "best skincare", "skincare brand India")
3. Use firecrawl to scrape Google search results for each keyword
4. For each result (brand), check:
   - sitemap.xml exists?
   - robots.txt blocks?
   - Schema markup present? (FAQ, Product, etc.)
   - Blog count?
   - PageSpeed?
5. Score 0-10, filter HOT (6+)

### Method 2: AI Visibility Check (Automated GEO/AEO)

Use `ai-seo` skill + API calls to Perplexity/ChatGPT:

1. For each niche query, ask Perplexity API: "What is best [niche] in [location]?"
2. Check if brand cited in answer
3. If NOT cited = HOT GEO lead

### Method 3: Sitemap + Schema Bulk Check

Use `firecrawl` to bulk check 100 websites:
- No sitemap = HOT
- No FAQ schema = HOT for GEO/AEO
- No blog = HOT

### Output Format (Automated)

```csv
Brand,Website,Niche,Google Rank,Indexed Pages,Sitemap,Schema Count,Blog Posts,AI Cited (ChatGPT),AI Cited (Perplexity),SEO Score,GEO Score,Why Hot,Contact
Zouk,zouk.co.in,D2C Bags,Page 3 (pos 22),120/500 (24%),No,1 (Product only),3,No,No,8,9,No sitemap, only 24% indexed, no FAQ schema, not cited in AI,contact@zouk.co.in
Dr Batra's,drbatras.com,Clinic,Page 2 (pos 12),80/200 (40%),Yes but blocked /blog/,2,12,No,No,7,8,Robots blocks blog, no FAQ schema, not in Perplexity for 'best skin clinic Bangalore',contact@drbatras.com
```

### What You Need From User

- Niche: D2C / Real Estate / Clinic / Coach / SaaS
- Location: India / Bangalore / Pan-India
- Count: How many leads? (10, 50, 100)
- Type: SEO only / GEO/AEO only / Both

Example:
- "Auto find 20 D2C brands needing SEO in India"
- "Find 15 real estate builders in Bangalore not cited in ChatGPT"

### Deduplication (50-Day Support)

Uses same V3 dedup system as performance marketing:
- `data/seen_seo_leads.json` remembers past brands
- Daily 50 NEW unique, zero duplicates for 50 days
- 50 days × 50 = 2500 unique SEO leads possible

### Limitations

- Google search scraping needs SerpAPI or firecrawl (JS-heavy)
- AI citation check needs Perplexity API or manual ChatGPT test
- For demo, uses mock DB with 3000 brands

### Related Skills

- `seo-lead-prospecting`: Manual methods
- `seo-audit`: Audit found lead
- `geo-aeo-audit`: AI visibility audit
- `firecrawl`: JS scraping
- `claude-seo`: Deep SEO
