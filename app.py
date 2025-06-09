import streamlit as st
import requests
import json
import pandas as pd
from io import StringIO

# Page config
st.set_page_config(page_title="Google Index Checker", layout="centered")

# App Title
st.title("🔎 Google Index Status Checker")
st.write("Enter multiple URLs (one per line) to check if they are indexed on Google.")

# API Configuration
api_url = "https://google.serper.dev/search"
api_key = "2aef12cfe6a222430e48abca83c63f2b36a4970b"
headers = {
    'X-API-KEY': api_key,
    'Content-Type': 'application/json'
}

# Text area for URL input
url_input = st.text_area("Paste your URLs below:", height=200, placeholder="https://example.com\nhttps://example.com/page")

# Button to trigger index checking
if st.button("Check Index Status"):
    urls = [url.strip() for url in url_input.strip().split('\n') if url.strip()]
    
    if not urls:
        st.warning("Please enter at least one URL.")
    else:
        results = []

        with st.spinner("Checking index status..."):
            for url in urls:
                payload = json.dumps({"q": f"site:{url}"})
                try:
                    response = requests.post(api_url, headers=headers, data=payload)
                    if response.status_code == 200:
                        organic = response.json().get('organic', [])
                        status = "Indexed" if len(organic) > 0 else "Not Indexed"
                    else:
                        status = f"Error {response.status_code}"
                except Exception as e:
                    status = "Error"

                results.append({"URL": url, "Index": status})

        # Convert results to DataFrame
        df = pd.DataFrame(results)

        # Show results
        st.subheader("Result Summary")
        st.dataframe(df)

        # Show counts
        indexed_count = df[df["Index"] == "Indexed"].shape[0]
        not_indexed_count = df[df["Index"] == "Not Indexed"].shape[0]
        error_count = df[df["Index"].str.contains("Error")].shape[0]

        st.markdown(f"✅ Indexed: **{indexed_count}**")
        st.markdown(f"❌ Not Indexed: **{not_indexed_count}**")
        st.markdown(f"⚠️ Errors: **{error_count}**")

        # Download CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="index_status_results.csv",
            mime="text/csv"
        )
