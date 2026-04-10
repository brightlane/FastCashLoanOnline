import requests
from oauth2client.service_account import ServiceAccountCredentials

# 1. Setup credentials (requires your service_account.json)
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
JSON_KEY_FILE = "service_account.json" 

def push_to_google(url):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, SCOPES)
    access_token = credentials.get_access_token().access_token
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    data = {
        "url": url,
        "type": "URL_UPDATED"
    }
    
    response = requests.post(ENDPOINT, json=data, headers=headers)
    print(f"Status for {url}: {response.status_code} - {response.text}")

# Your main Power Page URL
push_to_google("https://your-portal-url.com/payday-loans")
