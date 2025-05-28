# streamlit_app.py
# ----------------------------------
# Streamlitを使用して、Google Places APIの入力条件をGUIで指定し、CSV形式で結果を出力するツール
# 入力: 地域名(市区町村)、業態(美容室など)、最小評価
# 出力: 店舗情報を中間表示してCSVとしてダウンロード
# ----------------------------------

import streamlit as st
import requests
import csv
import io
from urllib.parse import urlencode

API_KEY = "API_KEY"  # ここに自分のAPIキーを設定
PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"

def search_places(query, min_rating=0.0):
    all_results = []
    params = {
        "query": query,
        "key": API_KEY,
        "language": "ja"
    }
    while True:
        response = requests.get(PLACES_URL, params=params)
        data = response.json()
        for result in data.get("results", []):
            rating = result.get("rating", 0.0)
            if rating >= min_rating:
                place_id = result["place_id"]
                details = fetch_place_details(place_id)
                all_results.append({
                    "名前": result.get("name"),
                    "評価": rating,
                    "評価数": result.get("user_ratings_total", 0),
                    "電話番号": details.get("formatted_phone_number", ""),
                    "住所": result.get("formatted_address"),
                    "URL": details.get("url", "")
                })
        if "next_page_token" in data:
            import time
            time.sleep(2)
            params["pagetoken"] = data["next_page_token"]
        else:
            break
    return all_results

def fetch_place_details(place_id):
    params = {
        "place_id": place_id,
        "fields": "formatted_phone_number,url",
        "key": API_KEY,
        "language": "ja"
    }
    response = requests.get(DETAILS_URL, params=params)
    return response.json().get("result", {})

def convert_to_csv(data):
    output = io.StringIO()
    fieldnames = ["名前", "評価", "評価数", "電話番号", "住所", "URL"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)
    return output.getvalue()

# Streamlit UI
st.title("Google Maps 店舗情報探索")

city = st.text_input("場所指定 (例: 東京都新宿区)")
keyword = st.text_input("業態指定 (例: 美容室, 居酒屋)")
min_rating = st.slider("最小評価", 0.0, 5.0, 3.5, step=0.1)

if st.button("探索開始"):
    if city and keyword:
        query = f"{city} {keyword}"
        with st.spinner("探索中..."):
            results = search_places(query, min_rating=min_rating)
        if results:
            st.success(f"{len(results)} 件の結果")
            st.dataframe(results)
            csv_data = convert_to_csv(results)
            st.download_button("CSVダウンロード", data=csv_data, file_name="results.csv", mime="text/csv")
        else:
            st.warning("結果がありません")
    else:
        st.error("すべての項目を入力してください")
