# 🤖 Gemini 1.5 Chatbot (Streamlit)

A minimal chatbot interface built with **Streamlit** using **Google's Gemini 1.5 Flash/Pro** model via `google-generativeai`.

## 🚀 Features

* Uses Gemini 1.5 (Flash or Pro)
* Streamlit-based web chat UI
* **Remembers chat history in session**
* Loads API key securely from `config.json`

## 🧱 Requirements

* Python 3.9 to 3.11
* `streamlit`
* `google-generativeai`
* `Pillow`

## 🔧 Setup

1. **Clone the repo**

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a ****`config.json`**** file** in the root:

   ```json
   {
     "GEMINI_API_KEY": "your-api-key-here"
   }
   ```

## ▶️ Run the App

```bash
streamlit run src/main.py
```

## 📆 Project Structure

```
project/
├── src/
│   └── main.py
├── config.json
├── requirements.txt
 I── notebook.ipynb
└── README.md
```

## 📀 Notes

* Works with Gemini 1.5 Flash or Pro.
* Ensure your API key has access via Google AI Studio or Console.


LMAO!
google.api_core.exceptions.ResourceExhausted: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations { quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests" quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier" quota_dimensions { key: "model" value: "gemini-1.5-flash" } quota_dimensions { key: "location" value: "global" } quota_value: 50 } , links { description: "Learn more about Gemini API quotas" url: "https://ai.google.dev/gemini-api/docs/rate-limits" } , retry_delay { seconds: 7 } ]
