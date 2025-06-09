# 🔎 Google Index Status Checker

A simple and intuitive Streamlit web application that allows you to check whether multiple URLs are indexed on Google using the Serper API.

## 🚀 Features

- Paste and check multiple URLs at once
- Detects whether URLs are **Indexed**, **Not Indexed**, or returns an **Error**
- View results in a sortable, interactive table
- Get a summary of indexed vs. non-indexed URLs
- Export results to a downloadable CSV file

## 🧠 How It Works

This tool uses the [Serper API](https://serper.dev/) to perform a `site:` query for each URL. Based on the returned results, it determines if a URL is currently indexed on Google.

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Serper API](https://serper.dev/)

## 🖥️ Usage

1. **Install Dependencies**
   ```bash
   pip install streamlit pandas requests
