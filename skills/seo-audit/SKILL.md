---
name: seo-audit
description: "When user wants to audit a website's traditional SEO. Use when user says 'SEO audit', 'audit this website SEO', 'technical SEO check', 'on-page SEO audit', 'why not ranking'. Checks crawlability, indexability, schema, speed, content, internal linking, etc. For GEO/AEO (AI citations), see geo-aeo-audit. For finding leads, see seo-lead-prospecting."
metadata:
  version: 2.0.0
---

# SEO Audit - Traditional SEO (Technical + On-Page + Off-Page)

You are a senior SEO auditor. Audit any website for traditional SEO that drives Google rankings.

## When to Use

User gives website URL and says "audit SEO", "why not ranking", "technical SEO check".

**Orchestrates existing skills:**
- `seo-audit` (existing 50 skills - technical SEO)
- `claude-seo` (31 skills - deep SEO)
- `site-architecture` (page hierarchy, navigation)
- `schema` (structured data)
- `programmatic-seo` (scaled pages)
- `ai-seo` (for comparison)

## 8-Point SEO Audit Framework

### 1. Technical SEO (Crawlability & Indexability)

**Check via fetch_page + web_search:**

- [ ] sitemap.xml exists? `https://brand.com/sitemap.xml`
- [ ] robots.txt exists and not blocking? `https://brand.com/robots.txt`
- [ ] Indexed pages: Search `site:brand.com` - count vs actual pages
- [ ] Canonical tags present?
- [ ] HTTPS?
- [ ] Mobile-friendly? (Google Mobile-Friendly Test logic)
- [ ] Core Web Vitals: LCP, CLS, INP (via PageSpeed Insights logic)

**Common leaks:**
- No sitemap = Google can't find pages
- robots.txt blocking /blog/
- 1000 products but only 100 indexed = 90% invisible

### 2. On-Page SEO

- [ ] Title tags: Unique, <60 chars, keyword included?
- [ ] Meta descriptions: Unique, <155 chars, CTA?
- [ ] H1: One per page, keyword?
- [ ] H2/H3: Logical hierarchy?
- [ ] Content length: Thin content (<300 words) or substantial?
- [ ] Keyword usage: Main keyword in title, H1, first 100 words?
- [ ] Images: Alt text present? Compressed?
- [ ] Internal linking: 3+ internal links per page?

### 3. Content & Topical Authority

- [ ] Blog exists? How many posts? ( <10 = HOT lead)
- [ ] Content depth: Does blog cover niche comprehensively?
- [ ] Topical clusters: Pillar + cluster pages?
- [ ] Freshness: Last post date? (6 months ago = stale)
- [ ] E-E-A-T: Author bio, credentials, about page?

### 4. Schema Markup (Critical for GEO/AEO too)

Check source for JSON-LD:

- [ ] Organization schema?
- [ ] Product schema? (for D2C)
- [ ] FAQ schema? (for AEO)
- [ ] HowTo schema?
- [ ] Article/BlogPosting schema?
- [ ] LocalBusiness schema? (for local)
- [ ] Breadcrumb schema?

**No schema = 0 rich results = losing CTR**

### 5. Site Architecture

- [ ] URL structure: Clean (/blog/best-bags) vs messy (/p?id=123)?
- [ ] Navigation: Logical, 3 clicks to any page?
- [ ] Breadcrumbs?
- [ ] Pagination handling?
- [ ] Programmatic SEO opportunity: Can they create 100 locality pages? (e.g., /flats-in-whitefield, /flats-in-koramangala)

### 6. Speed & Performance

- [ ] PageSpeed: Mobile score? ( <50 = poor)
- [ ] Load time: >3s = losing 32% traffic
- [ ] Image optimization: WebP? Lazy load?
- [ ] JS/CSS minified?

### 7. Off-Page (Brief)

- [ ] Backlinks: Check via open-ai-seo-agent (uses Search Console)
- [ ] Domain Authority: Estimate via web_search
- [ ] Brand mentions: Search brand name

### 8. Competitor Gap

- [ ] Competitor ranks for X keywords, you rank for Y
- [ ] Gap: Keywords competitor has that you don't
- [ ] Example: 99acres ranks for 12k keywords, small builder for 200 = 11.8k gap

## Lead Scoring for SEO Audit

Score /10:
- [2] No sitemap or robots.txt blocking
- [2] No blog or <10 posts
- [2] No schema (0 types)
- [2] Slow (>3s) or thin content
- [2] Ranks page 2-3, not page 1

6+ = HOT

## Output Format

# SEO AUDIT: [Brand]
**Website:** [URL] | **Niche:** [Niche] | **SEO Score:** X/10

### Executive Summary
### Technical SEO (sitemap, robots, indexed, Core Web Vitals)
### On-Page SEO (title, meta, H1, content, alt)
### Content & Topical Authority (blog count, clusters, E-E-A-T)
### Schema Markup (0/7 types present)
### Site Architecture (URL, navigation, programmatic opportunity)
### Speed & Performance (PageSpeed, load time)
### Competitor Gap (keywords gap)
### 3 Quick Wins (with traffic impact)
### Outreach Templates

## 3 Quick Wins Example

1. **Add Sitemap + Fix Robots (Day 1):** Create sitemap.xml with 500 pages, submit to Search Console. Expected: +40% indexed pages in 7 days.

2. **Add FAQ Schema + Blog (Day 2-3):** Create 10 FAQs with schema for main keywords. Expected: Rich results, +15% CTR, +8% traffic.

3. **Programmatic SEO - Locality Pages (Day 4-7):** Create 50 pages: /flats-in-[locality] with unique content. Expected: Rank for 100+ long-tail keywords, +2000 visits/mo.

## Related Skills

- `geo-aeo-audit`: For AI citations (ChatGPT, Perplexity)
- `seo-lead-prospecting`: Find leads
- `claude-seo`: Deep SEO (31 skills)
- `ai-seo`: AI search optimization
- `programmatic-seo`: Scaled pages
