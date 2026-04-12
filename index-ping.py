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

# --- 2. CONTENT GENERATOR (3,000 WORDS) ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Updated {today}</h2>"
    content += f"<p>MaxLend provides {keyword} through a secure, tribal-lending platform. Residents of {state} can access up to $2,000 with fast approval and no hard credit pull.</p>"
    
    sections = [
        f"Why {keyword} is the Preferred Choice in {state}",
        "Understanding Tribal Sovereignty and Your Loan",
        "The MaxLend Advantage: Fast, Secure, and Reliable",
        "How to Qualify for Instant Funding Today",
        "Repayment Terms and Financial Responsibility",
        "Common Questions About Online Installment Loans"
    ]
    
    for section in sections:
        content += f"<h3>{section}</h3><p>"
        content += f"When considering {keyword}, it is vital to understand how {section} affects your long-term goals. MaxLend ensures that {state} borrowers have the transparency they deserve. " * 25
        content += "</p>"
    return content

# --- 3. THE MASTER TEMPLATE ---
def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    today_iso = datetime.date.today().strftime("%Y-%m-%d")
    
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
        .cta-btn {{ display: inline-block; background: var(--secondary); color: white; padding: 18px 35px; font-size: 1.4rem; font-weight: bold; text-decoration: none; border-radius: 50px; margin: 20px 0; box-shadow: 0 4px 15px rgba(230,0,0,0.3); }}
        .container {{ max-width: 900px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        nav {{ background: #003366; padding: 10px; text-align: center; }}
        nav a {{ color: white; margin: 0 15px; text-decoration: none; font-size: 0.9rem; }}
        footer {{ background: #f1f1f1; padding: 40px 20px; font-size: 0.75rem; color: #444; border-top: 1px solid #ccc; }}
        .sticky-footer {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; text-align: center; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); }}
    </style>
    
    <script>
        let cookieFired = false;
        function fireAffiliate() {{
            if (!cookieFired) {{
                cookieFired = true;
                window.open("{AFFILIATE_URL}", "_blank");
            }}
        }}
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{ fireAffiliate(); }}
        }}, false);
    </script>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="blog.html">Loan Advice</a>
        <a href="contact.html">Contact</a>
        <a href="privacy.html">Legal</a>
    </nav>
    <header>
        <a href="{AFFILIATE_URL}"><img src="{LOGO_PATH}" class="logo" alt="MaxLend Owl"></a>
        <h1>{keyword}</h1>
        <p>Instant Decision • No FICO Impact • Tribal Lending Excellence</p>
        <a href="{AFFILIATE_URL}" class="cta-btn">APPLY AT MAXLEND</a>
    </header>
    <div class="container">{body}</div>
    <div class="sticky-footer">
        <a href="{AFFILIATE_URL}" class="cta-btn" style="font-size: 1rem; margin: 0; padding: 10px 25px;">GET YOUR CASH</a>
    </div>
    <footer>
        <div style="max-width: 900px; margin: auto;">
            <p><strong>Official Contact:</strong> 1-877-936-4336 | customerservice@maxlend.com | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
            <p><strong>Legal:</strong> MaxLend is an entity of the Mandan, Hidatsa, and Arikara Nation. APR varies by creditworthiness. This is an expensive form of borrowing for short-term needs.</p>
            <p style="text-align:center;">Last Updated: {today_long}</p>
        </div>
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

# Bing Ping
payload = {{"host": "brightlane.github.io", "key": INDEXNOW_KEY, "keyLocation": f"{BASE_URL}/{{INDEXNOW_KEY}}.txt", "urlList": urls}}
try:
    requests.post("https://www.bing.com/indexnow", json=payload, timeout=10)
    print("Bing Notified.")
except:
    print("Ping Failed.")
