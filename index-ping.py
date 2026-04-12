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

# --- 2. THE 3,000 WORD CONTENT ENGINE ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Updated {today}</h2>"
    
    # Financial Compliance & Education Blocks
    sections = [
        f"Why {keyword} is Trending in {state}",
        "Understanding Tribal Sovereignty and Consumer Protection",
        "How to Qualify with Alternative Credit Data",
        "The Importance of Short-Term Financial Planning",
        "MaxLend vs. Traditional Storefront Lenders",
        "Repayment Strategies for Installment Loans"
    ]
    
    for section in sections:
        content += f"<h3>{section}</h3><p>"
        content += f"In the current economic climate of {state}, {keyword} has become a vital tool for many families. MaxLend provides a transparent platform where transparency meets speed. " * 30 
        content += "</p>"
    
    return content

# --- 3. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MaxLend Official Affiliate</title>
    <style>
        :root {{ --primary: #004080; --secondary: #e60000; }}
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #f4f7f9; color: #333; line-height: 1.6; }}
        header {{ background: var(--primary); color: white; padding: 40px 20px; text-align: center; border-bottom: 5px solid var(--secondary); }}
        .logo {{ height: 100px; border-radius: 50%; border: 3px solid white; background: white; }}
        .cta-btn {{ display: inline-block; background: var(--secondary); color: white; padding: 18px 35px; font-size: 1.4rem; font-weight: bold; text-decoration: none; border-radius: 50px; margin: 20px 0; }}
        .container {{ max-width: 900px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        nav {{ background: #003366; padding: 10px; text-align: center; }}
        nav a {{ color: white; margin: 0 15px; text-decoration: none; font-size: 0.9rem; }}
        footer {{ background: #f1f1f1; padding: 40px 20px; font-size: 0.75rem; color: #444; border-top: 1px solid #ccc; }}
    </style>
    <script>
        // Exit Intent Strategy
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ window.open("{AFFILIATE_URL}", "_blank"); }}
        }}, false);
    </script>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="blog.html">Advice</a>
        <a href="contact.html">Contact</a>
        <a href="privacy.html">Legal</a>
    </nav>
    <header>
        <a href="{AFFILIATE_URL}"><img src="{LOGO_PATH}" class="logo" alt="MaxLend"></a>
        <h1>{keyword}</h1>
        <p>Instant Decision • No FICO Impact • Tribal Excellence</p>
        <a href="{AFFILIATE_URL}" class="cta-btn">APPLY NOW</a>
    </header>
    <div class="container">{body}</div>
    <footer>
        <div style="max-width: 900px; margin: auto;">
            <p><strong>Official Info:</strong> 1-877-936-4336 | customerservice@maxlend.com | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
            <p>MaxLend is an entity of the MHA Nation. APR and terms apply. This is an expensive form of borrowing.</p>
            <p style="text-align:center;">Last Updated: {today_long}</p>
        </div>
    </footer>
</body>
</html>"""

# --- 4. EXECUTION ---
generated_urls = []
for filename, keyword in PAGES_TO_GENERATE.items():
    state = random.choice(STATES)
    body_text = generate_3000_words(keyword, state)
    full_html = get_template(keyword, keyword, body_text)
    
    # This "w" mode creates the file if it's missing, no reading required.
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    generated_urls.append(f"{BASE_URL}/{filename}")
    print(f"Generated {filename}")

# Build Sitemap
sitemap_content = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
for url in generated_urls:
    sitemap_content += f'<url><loc>{url}</loc><lastmod>{datetime.date.today()}</lastmod></url>'
sitemap_content += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

# IndexNow Ping
payload = {
    "host": "brightlane.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
    "urlList": generated_urls
}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing IndexNow notification sent.")
except Exception as e:
    print(f"Ping failed: {e}")
