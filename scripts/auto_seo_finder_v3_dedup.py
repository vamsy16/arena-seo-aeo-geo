"""
Auto SEO Finder V3 - 50-Day Dedup for SEO/GEO/AEO
Same logic as performance marketing V3, but for SEO signals

Usage:
  python auto_seo_finder_v3_dedup.py --count 50 --day 1
  python auto_seo_finder_v3_dedup.py --count 50 --day 2 (excludes Day 1)
  ...
  python auto_seo_finder_v3_dedup.py --count 50 --day 50 (2500 unique, zero duplicates)
"""

import csv, json, random
from datetime import datetime
from pathlib import Path

SEEN_FILE = Path(__file__).parent.parent / "data" / "seen_seo_leads.json"
HISTORY_DIR = Path(__file__).parent.parent / "data" / "daily_history"
SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
HISTORY_DIR.mkdir(parents=True, exist_ok=True)

# 3000 mock SEO brands for 50-day demo
MOCK_DB = [
    {"brand": f"SEO_Brand_{i:04d}", "website": f"seobrand{i:04d}.com", "niche": random.choice(["D2C", "Real Estate", "Clinic", "Coach"]), "google_rank": f"Page {random.randint(2,3)}", "indexed": f"{random.randint(20,60)}%", "sitemap": random.choice(["No", "Yes but blocked"]), "schema_count": random.randint(0,2), "blog_posts": random.randint(0,15), "ai_cited_chatgpt": "No", "ai_cited_perplexity": "No", "seo_score": random.randint(6,10), "geo_score": random.randint(7,10), "leak": random.choice(["No sitemap", "No FAQ schema", "Not cited in AI", "Thin blog"])}
    for i in range(1, 3000)
]

REAL = [
    {"brand": "Zouk", "website": "zouk.co.in", "niche": "D2C Bags", "google_rank": "Page 3", "indexed": "24%", "sitemap": "No", "schema_count": 1, "blog_posts": 3, "ai_cited_chatgpt": "No", "ai_cited_perplexity": "No", "seo_score": 8, "geo_score": 9, "leak": "No sitemap, 24% indexed, no FAQ, not cited"},
    {"brand": "Propsoch", "website": "propsoch.club", "niche": "Real Estate", "google_rank": "Page 3", "indexed": "26%", "sitemap": "No", "schema_count": 0, "blog_posts": 5, "ai_cited_chatgpt": "No", "ai_cited_perplexity": "No", "seo_score": 9, "geo_score": 10, "leak": "No sitemap, 0 schema, zero AI citations"},
]
MOCK_DB = REAL + MOCK_DB

def load_seen():
    if SEEN_FILE.exists():
        with open(SEEN_FILE) as f:
            return json.load(f)
    return {"brands": {}, "total_found": 0, "daily_log": []}

def save_seen(d):
    with open(SEEN_FILE, 'w') as f:
        json.dump(d, f, indent=2)

def find_new_seo_leads(count=50, day=1, niche="ALL"):
    seen = load_seen()
    seen_brands = set(seen["brands"].keys())
    print(f"📅 Day {day} | Target: {count} NEW SEO leads | Already seen: {len(seen_brands)}")
    available = [l for l in MOCK_DB if l['brand'] not in seen_brands]
    if niche != "ALL":
        available = [l for l in available if niche.lower() in l['niche'].lower()]
    random.shuffle(available)
    new_leads = available[:count]
    for lead in new_leads:
        lead['found_at'] = datetime.now().isoformat()
        lead['day_found'] = day
        seen["brands"][lead['brand']] = {"first_seen": lead['found_at'], "day": day, "website": lead['website']}
    seen["total_found"] += len(new_leads)
    seen["daily_log"].append({"day": day, "date": datetime.now().strftime("%Y-%m-%d"), "count": len(new_leads), "total_so_far": seen["total_found"], "brands": [l['brand'] for l in new_leads]})
    save_seen(seen)
    csv_path = HISTORY_DIR / f"seo-day-{day:02d}-{count}-leads.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=new_leads[0].keys())
        writer.writeheader()
        writer.writerows(new_leads)
    print(f"✅ Day {day}: {len(new_leads)} NEW SEO leads (0 duplicates from {len(seen_brands)}) | Total: {seen['total_found']} | Saved: {csv_path}")
    return new_leads

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=50)
    parser.add_argument("--day", type=int, default=1)
    parser.add_argument("--niche", default="ALL")
    parser.add_argument("--stats", action="store_true")
    parser.add_argument("--reset", action="store_true")
    args = parser.parse_args()
    if args.stats:
        seen = load_seen()
        print(f"Total unique: {seen['total_found']} | Days: {len(seen['daily_log'])}")
    elif args.reset:
        if SEEN_FILE.exists():
            SEEN_FILE.unlink()
        print("Reset done")
    else:
        find_new_seo_leads(args.count, args.day, args.niche)
