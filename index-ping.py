import datetime
import random
import requests
import json
import os

# --- 1. CONFIGURATION ---
# Replace with your actual GitHub Pages URL and LinkConnector URL
BASE_URL = "https://brightlane.github.io/FastCashLoanOnline"
INDEXNOW_KEY = "817c039b282227a69abd9cfa9f9b87f2"
AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949096598005765&atid=MaxlendWeb"
LOGO_PATH = "images/Mr-owl-with-brown-eyes.jpg"

# The 13-page engine (10 landing pages + Legal/Blog)
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
    "blog.html": "Financial Success Daily Blog"
}

STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Florida", "Georgia", "Texas", "Ohio", "New York", "Illinois", "Michigan"]

# --- 2. THE 3,000 WORD CONTENT ENGINE ---
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, 2026")
    content = f"<h2>{keyword} for {state} Residents - Verified {today}</h2>"
    
    # Building blocks for high-word-count SEO
    sections = [
        f"Why {keyword} is the Top Search in {state} Today",
        "The Benefits of Tribal Installment Lending",
        "Understanding Alternative Credit Data (No FICO Impact)",
        "Same Day Funding: How the MaxLend Process Works",
        "Managing Short-Term Financial Obligations Responsibly",
        "Regulatory Compliance and Your Rights as a Borrower"
    ]
    
    for section in sections:
        content += f"<h3>{section}</h3><p>"
        # Loops are used to build the "educational" density crawlers love
        content += f"In the state of {state}, finding reliable {keyword} options requires a partner that values speed and transparency. MaxLend stands out by providing a path to capital that bypasses traditional banking friction. " * 25
        content += "</p>"
    
    return content

# --- 3. THE MASTER HTML TEMPLATE ---
def get_template(title, keyword, body):
    today_long = datetime.date.today().strftime("%B %d, 2026")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MaxLend Official Portal</title>
    <style>
        :root {{ --primary: #004080; --secondary: #e60000; }}
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #f4f7f9; color: #333; line-height: 1.6; }}
        nav {{ background: #003366; padding: 10px; text-align: center; }}
        nav a {{ color: white; margin: 0 15px; text-decoration: none; font-size: 0.9rem; font-weight: bold; }}
        header {{ background: var(--primary); color: white; padding: 40px 20px; text-align: center; border-bottom: 5px solid var(--secondary); }}
        .logo {{ height: 100px; border-radius: 50%; border: 3px solid white; background: white; }}
        .cta-btn {{ display: inline-block; background: var(--secondary); color: white; padding: 18px 35px; font-size: 1.4rem; font-weight: bold; text-decoration: none; border-radius: 50px; margin: 20px 0; box-shadow: 0 4px 15px rgba(230,0,0,0.3); transition: transform 0.2s; }}
        .cta-btn:hover {{ transform: scale(1.05); }}
        .container {{ max-width: 900px; margin: 30px auto; padding: 30px; background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
        footer {{ background: #f1f1f1; padding: 40px 20px; font-size: 0.75rem; color: #444; border-top: 1px solid #ccc; line-height: 1.4; }}
        .legal-box {{ max-width: 900px; margin: auto; }}
        .sticky-footer {{ position: fixed; bottom: 0; width: 100%; background: white; padding: 10px; text-align: center; box-shadow: 0 -2px 10px rgba(0,0,0,0.1); z-index: 1000; }}
    </style>
    
    <script>
        document.addEventListener("mouseleave", function(e) {{
            if (e.clientY < 0) {{
                // Drop the affiliate cookie by opening the link in a background tab
                window.open("{AFFILIATE_URL}", "_blank");
            }}
        }}, false);
    </script>
</head>
<body>
    <nav>
        <a href="index.html">Home</a>
        <a href="blog.html">Loan Blog</a>
        <a href="contact.html">Contact Us</a>
        <a href="privacy.html">Privacy & Legal</a>
    </nav>
    <header>
        <a href="{AFFILIATE_URL}"><img src="{LOGO_PATH}" class="logo" alt="MaxLend Logo"></a>
        <h1>{keyword}</h1>
        <p>Instant Decisioning • Sovereign Lending • Funds by 5:00 PM</p>
        <a href="{AFFILIATE_URL}" class="cta-btn">APPLY AT MAXLEND</a>
    </header>
    <div class="container">
        {body}
    </div>
    <div class="sticky-footer">
        <a href="{AFFILIATE_URL}" class="cta-btn" style="font-size: 1rem; margin: 0; padding: 10px 25px;">GET STARTED TODAY</a>
    </div>
    <footer>
        <div class="legal-box">
            <p><strong>Official Contact:</strong> 1-877-936-4336 | customerservice@maxlend.com | 145 Tribal Business Council Rd, Mandaree, ND 58757</p>
            <p><strong>Tribal Disclosure:</strong> MaxLend is an entity of the Mandan, Hidatsa, and Arikara Nation, a federally recognized sovereign American Indian Tribe. Loans are governed by Tribal law. This is an expensive form of borrowing for short-term financial needs.</p>
            <p style="text-align:center; margin-top:20px;">Site Updated: {today_long} | &copy; 2026 Fast Cash Online</p>
        </div>
    </footer>
    <br><br><br> </body>
</html>"""

# --- 4. EXECUTION AND SITEMAP GENERATION ---
generated_urls = []

print("Starting generation...")
for filename, keyword in PAGES_TO_GENERATE.items():
    state = random.choice(STATES)
    body_content = generate_3000_words(keyword, state)
    final_html = get_template(keyword, keyword, body_content)
    
    # Use encoding="utf-8" to prevent crashes on Linux runners
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    generated_urls.append(f"{BASE_URL}/{filename}")
    print(f"Generated: {filename}")

# Generate sitemap.xml
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in generated_urls:
    sitemap_xml += f'  <url>\n    <loc>{url}</loc>\n    <lastmod>{datetime.date.today()}</lastmod>\n    <changefreq>daily</changefreq>\n  </url>\n'
sitemap_xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print("Sitemap generated.")

# --- 5. BING INDEXNOW PING ---
# Ensure keyLocation matches exactly where your .txt key file is hosted
payload = {
    "host": "brightlane.github.io",
    "key": INDEXNOW_KEY,
    "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
    "urlList": generated_urls
}

headers = {"Content-Type": "application/json; charset=utf-8"}

try:
    response = requests.post("https://www.bing.com/indexnow", data=json.dumps(payload), headers=headers, timeout=15)
    print(f"Bing Ping Response: {response.status_code}")
except Exception as e:
    print(f"Bing Ping Failed: {e}")
