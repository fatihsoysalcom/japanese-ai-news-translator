# Japanese AI News Translator

This example demonstrates how to translate Japanese text into English using the Google Cloud Translate API. It simulates the core translation functionality described in the article, which uses an n8n workflow to automate this process for Japanese AI news. The script utilizes Python's standard library for making HTTP requests and parsing JSON responses.

## Language

`python`

## How to Run

1. Obtain a Google Cloud Translate API key and enable the Cloud Translation API in your Google Cloud project.
2. Set the API key as an environment variable: `export GOOGLE_TRANSLATE_API_KEY="YOUR_API_KEY"` (Linux/macOS) or `$env:GOOGLE_TRANSLATE_API_KEY="YOUR_API_KEY"` (PowerShell).
3. Run the script: `python main.py`

## Original Article

This example accompanies the Turkish article: [Japon Yapay Zeka Haberlerini Otomatik Çeviren n8n İş Akışı: Her Sabah $0.03'e Küresel Bilgiye Erişin](https://fatihsoysal.com/blog/japon-yapay-zeka-haberlerini-otomatik-ceviren-n8n-is-akisi-her-sabah-0-03e-kuresel-bilgiye-erisin/).

## License

MIT — see [LICENSE](LICENSE).
