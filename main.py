import os
import json
import urllib.request
import urllib.parse

# --- Configuration ---
# Get your Google Cloud Translate API key from environment variables.
# For instructions on how to obtain an API key and enable the Cloud Translation API,
# refer to Google Cloud documentation: https://cloud.google.com/translate/docs/setup
GOOGLE_TRANSLATE_API_KEY = os.getenv("GOOGLE_TRANSLATE_API_KEY")

if not GOOGLE_TRANSLATE_API_KEY:
    raise ValueError(
        "GOOGLE_TRANSLATE_API_KEY environment variable not set. "
        "Please obtain an API key from Google Cloud and set it."
    )

# Google Cloud Translate API endpoint (v2 for simplicity)
API_ENDPOINT = "https://translation.googleapis.com/language/translate/v2"

# --- Simulate fetching Japanese AI news ---
# In a real n8n workflow, this Japanese text would be fetched automatically
# from an RSS feed or another news source, as described in the article.
japanese_ai_news_snippet = (
    "日本のAI研究者、新たな強化学習アルゴリズムを発表。これは、"
    "ロボットがより複雑なタスクを自律的に学習する能力を大幅に向上させると期待されています。"
)

print("Original Japanese Text:")
print(japanese_ai_news_snippet)
print("-" * 30)

# --- Translate the text using Google Cloud Translate API ---
def translate_text(text, target_language="en", source_language="ja"):
    """
    Translates text using the Google Cloud Translate API (v2).
    Requires GOOGLE_TRANSLATE_API_KEY environment variable to be set.
    """
    params = {
        "q": text,
        "target": target_language,
        "source": source_language,
        "format": "text" # Optional: specify input format
    }
    
    # Construct the URL with the API key as a query parameter
    url = f"{API_ENDPOINT}?key={GOOGLE_TRANSLATE_API_KEY}"

    # Encode the parameters as JSON for the request body
    data = json.dumps(params).encode("utf-8")

    # Create the request object with appropriate headers
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json"
        },
        method="POST"
    )

    try:
        # Send the request and get the response
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode("utf-8")
            result = json.loads(response_data)
            
            # Extract the translated text from the API response
            if "data" in result and "translations" in result["data"]:
                return result["data"]["translations"][0]["translatedText"]
            else:
                print(f"Error: Unexpected API response structure: {result}")
                return None
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(f"Response body: {e.read().decode('utf-8')}")
        return None
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Raw response: {response_data}") # Print raw response for debugging
        return None

translated_text = translate_text(japanese_ai_news_snippet)

if translated_text:
    print("Translated English Text:")
    print(translated_text)
else:
    print("Translation failed.")
