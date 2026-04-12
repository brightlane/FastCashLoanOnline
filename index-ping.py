import datetime
import random

# 1. Configuration
TARGET_FILES = ["index.html", "maxlendfastcash.html"]
KEYWORDS = ["Need money now", "Fast cash loans", "Instant payday advance", "Emergency loans online"]
STATES = ["Texas", "Florida", "California", "Alabama", "Ohio"]

# 2. Generate the "Fresh" Content (Modular Strategy)
def generate_3000_words(keyword, state):
    today = datetime.date.today().strftime("%B %d, %2026")
    
    # In a real scenario, you could pull from an API or a local text database
    intro = f"<h3>Why {keyword} in {state} is trending on {today}</h3>"
    body = f"<p>If you are looking for {keyword}, you aren't alone. In {state}, thousands are...</p>"
    
    # Loop to build up the word count with your 10-page logic
    full_content = intro + body + (f"<p>More optimized text about {keyword}...</p>" * 50) 
    return full_content

# 3. Inject into HTML
for filename in TARGET_FILES:
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    keyword = random.choice(KEYWORDS)
    state = random.choice(STATES)
    new_content = generate_3000_words(keyword, state)

    # Replace the markers we set up in Step 1
    start_marker = ""
    end_marker = ""
    
    if start_marker in html and end_marker in html:
        before = html.split(start_marker)[0]
        after = html.split(end_marker)[1]
        updated_html = f"{before}{start_marker}\n{new_content}\n{end_marker}{after}"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(updated_html)
            print(f"Updated {filename} with keyword: {keyword}")
