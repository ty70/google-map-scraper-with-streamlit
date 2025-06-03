# Google Maps Scraper with Streamlit UI

This is a web application that automatically collects store information from Google Maps based on specified conditions (municipality, business type, rating) and outputs the results as a CSV file. It utilizes the Google Places API.

---

## ✨ Features

* Specify a municipality (e.g., "Shinjuku, Tokyo")
* Input a business type (e.g., "hair salon")
* Set a minimum rating (e.g., "4.0")
* Download the result as a CSV file

---

## 🚀 How to Run

### 1. Install Required Libraries

```bash
pip install streamlit requests
```

### 2. Register Your Google Places API Key

* Log in to [Google Cloud Console](https://console.cloud.google.com/)
* Enable the Places API
* Generate API credentials (API Key)

Paste the obtained API Key into the `API_KEY` field in `streamlit_app.py`

```python
# streamlit_app.py
# ----------------------------------
# A tool that uses Streamlit to input parameters for the Google Places API via a GUI and outputs results in CSV format
# Input: Region name (municipality), business type (e.g., hair salon), minimum rating
# Output: Display intermediate store info and allow CSV download
# ----------------------------------

import streamlit as st
import requests
import csv
import io
from urllib.parse import urlencode

API_KEY = "Paste your API key here"  # Set your API key here
PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
```

### 3. Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

---

## Input

Enter location, business type, and rating, then press the "Start Search" button.

---

## 📦 Output

The results of the search will be displayed in a table showing:

* Store name
* Rating
* Number of reviews
* Phone number
* Address
* Google Maps URL

Clicking the CSV download button will export the above table as a CSV file.

---

## 🔧 Project Structure

```
.
├── streamlit_app.py
├── output/
│   └── results.csv
├── README_ja.md
└── README.md      # this file
```

---

## Notes

* Using the API may incur charges, so please monitor your API Key usage.
* For issues or bugs, feel free to open an issue.

---

## 🙏 License

[MIT License](./LICENSE).
