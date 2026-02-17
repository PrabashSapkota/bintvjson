import requests
import json
import os

# The source API
SOURCE_URL = "https://streamed.pk/api/matches/all-today/popular"
# Your local file path in the repo
DEST_FILE = "bintvjson/index.json"

def sync_api():
    try:
        # 1. Fetch data from Streamed API
        print(f"Fetching data from {SOURCE_URL}...")
        response = requests.get(SOURCE_URL, timeout=15)
        response.raise_for_status()
        data = response.json()

        # 2. Ensure the directory exists
        os.makedirs(os.path.dirname(DEST_FILE), exist_ok=True)

        # 3. Save it to your local bintvjson/index.json
        with open(DEST_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        
        print("Success: bintvjson/index.json has been updated.")

    except Exception as e:
        print(f"Error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    sync_api()
