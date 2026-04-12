import datetime
import random
import requests
import json
import os

# --- 1. CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/FastCashLoanOnline"
INDEXNOW_KEY = "817c039b282227a69abd9cfa9f9b87f2"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb"
LOGO_PATH = "images/Mr-owl-with-brown-eyes.jpg"

PAGES_TO_GENERATE = {
    "index.html": "Fast Cash Loans Online",
    "maxlendfastcash.html": "MaxLend Online Loans",
    "need-money-now.html": "Need Money Now Today",
    "instant-payday-loans.html": "Instant Payday Loans Online",
    "emergency-cash-advance.html": "Emergency Cash Advance",
    "bad-credit-loans-direct.html": "Bad Credit Loans Direct Lender",
    "same-day-deposit-loans.html": "Same Day Deposit Loans",
    "quick-money-apps.html": "Quick Money Lending Apps",
    "borrow-money-instantly.html": "Borrow Money Instantly",
    "small-personal-loans.html": "Small Personal Loans Fast",
    "privacy.html": "Privacy Policy & Legal Disclosures",
    "contact.html": "Contact MaxLend Support",
    "blog.html": "Financial Success Blog"
}

STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Florida", "Georgia", "Texas", "Ohio", "New York", "Illinois"]

# --- 2. CONTENT GENERATOR ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Updated {today}</h2>"
    sections = ["Why {keyword} is the Preferred Choice", "Understanding Tribal Sovereignty", "How to Qualify Today"]
    for section in sections:
        content += f"<h3>{section}</h3><p>" + (f"In {state}, {keyword} seekers choose MaxLend for speed. ") * 40 + "</p>"
    return content

# --- 3. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{ --primary: #004080; --secondary: #e60000; }}
        body {{ font-family: sans-serif; margin: 0; background: #f4f7f9; }}
        header {{ background: var(--primary); color: white; padding: 40px; text-align: center; }}
        .logo {{ height: 100px; border-radius: 50%; background: white; }}
        .cta-btn {{ background: var(--secondary); color: white; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; }}
        .container {{ max-width: 900px; margin: 20px auto; padding: 20px; background: white; }}
    </style>
    <script>
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
        }});
    </script>
</head>
<body>
    <header>
        <a href="{AFFILIATE_URL}"><img src="{LOGO_PATH}" class="logo"></a>
        <h1>{keyword}</h1>
        <a href="{AFFILIATE_URL}" class="cta-btn">APPLY NOW</a>
    </header>
    <div class="container">{body}</div>
    <footer style="text-align:center; padding:20px; font-size:0.8rem;">
        <p>Official MaxLend Affiliate | 1-877-936-4336 | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
        <p>Last Updated: {today_long}</p>
    </footer>
</body>
</html>"""

# --- 4. EXECUTION ---
urls = []
for file, key in PAGES_TO_GENERATE.items():
    state = random.choice(STATES)
    text = generate_3000_words(key, state)
    with open(file, "w", encoding="utf-8") as f:
        f.write(get_template(key, key, text))
    urls.append(f"{BASE_URL}/{file}")

# Sitemap
with open("sitemap.xml", "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u in urls:
        f.write(f'<url><loc>{u}</loc><lastmod>{datetime.date.today()}</lastmod></url>')
    f.write('</urlset>')

# Bing Ping (Fixed JSON structure)
payload = {
    "host": "brightlane.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
    "urlList": urls
}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing Notified.")
except Exception as e:
    print(f"Ping Failed: {e}")
