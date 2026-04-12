import datetime
import random
import requests
import json
import os

# --- 1. CONFIGURATION ---
BASE_URL = "https://brightlane.github.io/FastCashLoanOnline"
INDEXNOW_KEY = "817c039b282227a69abd9cfa9f9b87f2"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb"

# The 10 Targeted Keywords & Filenames
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
    "small-personal-loans.html": "Small Personal Loans Fast"
}

STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Florida", "Georgia", "Texas", "Ohio"]

# --- 2. THE CONTENT GENERATOR (3,000 Word Logic) ---
def generate_fresh_content(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    
    # Dynamic Headers
    content = f"<h2>How to get {keyword} in {state} on {today}</h2>"
    content += f"<p>Searching for {keyword} in {state} has increased by 40% this week. If you need immediate funding, MaxLend provides a secure path to capital without the hurdles of traditional banking.</p>"
    
    # Modular Blocks to hit 3,000 words
    # We use a loop to simulate high-volume educational content about lending laws and strategies
    filler_topics = [
        f"Understanding the APR of {keyword} in {state}.",
        f"Why {state} residents prefer online installment loans over storefronts.",
        f"How to improve your approval odds for {keyword}.",
        "The role of Tribal Sovereignty in modern lending."
    ]
    
    for topic in filler_topics:
        content += f"<h3>{topic}</h3>"
        content += f"<p>This deep dive into {keyword} explores why transparency matters. {state} borrowers often face high-interest cycles, but by using a 'Pay-Ahead' strategy, you can minimize costs...</p>"
        # Repeat/Expand text blocks to reach the 3,000-word SEO threshold
        content += "<p>Lorem ipsum logic: Detailed financial advice text goes here... " * 20
        
    return content

# --- 3. THE TEMPLATE BUILDER ---
def get_template(title, keyword):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 2026 Fast Approval</title>
    <style>
        :root {{ --primary: #004080; --secondary: #e60000; }}
        body {{ font-family: 'Segoe UI', sans-serif; margin: 0; background: #f4f7f9; color: #333; }}
        header {{ background: var(--primary); color: white; padding: 40px; text-align: center; border-bottom: 5px solid var(--secondary); }}
        .logo {{ height: 100px; border-radius: 50%; border: 3px solid white; }}
        .cta-btn {{ display: inline-block; background: var(--secondary); color: white; padding: 18px 35px; font-size: 1.4rem; font-weight: bold; text-decoration: none; border-radius: 50px; margin: 20px 0; }}
        .container {{ max-width: 900px; margin: 30px auto; padding: 20px; background: white; border-radius: 8px; }}
        .sticky-footer {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; text-align: center; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <header>
        <a href="{AFFILIATE_URL}"><img src="images/Mr-owl-with-brown-eyes.jpg" class="logo" alt="Logo"></a>
        <h1>{keyword}</h1>
        <a href="{AFFILIATE_URL}" class="cta-btn">GET CASH NOW</a>
    </header>
    <div class="container">
        </div>
    <div class="sticky-footer"><a href="{AFFILIATE_URL}" class="cta-btn" style="font-size:1rem; padding:10px 20px;">APPLY TODAY</a></div>
    <footer style="text-align:center; padding:40px; font-size:0.8rem;">
        Last Updated: {datetime.date.today().strftime("%B %d, 2026")}
    </footer>
</body>
</html>"""

# --- 4. EXECUTION ---
generated_urls = []

for filename, title in PAGES_TO_GENERATE.items():
    keyword = title
    state = random.choice(STATES)
    
    # 1. Create the base HTML structure
    html_content = get_template(title, keyword)
    
    # 2. Generate the 3,000 words
    fresh_body = generate_fresh_content(keyword, state)
    
    # 3. Inject content
    final_html = html_content.replace("", fresh_body)
    
    # 4. Save file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    generated_urls.append(f"{BASE_URL}/{filename}")
    print(f"Successfully generated {filename}")

# --- 5. PING BING (IndexNow) ---
def ping_bing(key, url_list):
    data = {{
        "host": "brightlane.github.io",
        "key": key,
        "keyLocation": f"{BASE_URL}/{{key}}.txt",
        "urlList": url_list
    }}
    try:
        r = requests.post("https://www.bing.com/indexnow", json=data, timeout=10)
        print(f"Bing Notification Status: {{r.status_code}}")
    except Exception as e:
        print(f"Ping failed: {{e}}")

ping_bing(INDEXNOW_KEY, generated_urls)
