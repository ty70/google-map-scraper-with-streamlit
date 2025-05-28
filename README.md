# Google Maps Scraper with Streamlit UI

Google Mapsの店舗情報を、指定条件（市町村名・業態・評価）に基づいて自動取得し、CSVとして出力できるStreamlitアプリケーションです。Google Places APIを利用しています。

---

## ✨ 機能

* 市町村（例："新宿区"）の指定
* 業態（例："ネイルサロン"）の入力
* 評価の下限（例："4.0"）の設定
* 結果をCSVファイルとしてダウンロード可能

---

## 🚀 実行手順

### 1. 必要なライブラリのインストール

```bash
pip install streamlit requests
```

### 2. Google Places APIキーの登録

* [Google Cloud Console](https://console.cloud.google.com/) にログイン
* Places API を有効化
* 認証情報(API Key) を発行

取得したAPI Keyを```streamlit_app.py```中のAPI_KEYの中に記述してください

```streamlit_app.py
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

API_KEY = "ここに貼り付けてください"  # ここに自分のAPIキーを設定
PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
```

### 3. Streamlit アプリの実行

```bash
streamlit run streamlit_app.py
```

---

## 入力

場所、業態、評価をそれぞれ入力し
探索開始ボタンを押す。

---

## 📦 出力

検索した結果
\*\*件の結果
店名、評価、レビュー数、電話番号、住所、Google Maps URL の表が
表れます。
CSVダウンロードのボタンを押すと
上記の表がダウンロードされます。

---

## 🔧 構成

```
.
├── streamlit_app.py
├── output/
│   └── results.csv
└── README.md
```

---

## 注意

* 有料なAPI利用となる場合があるので、発行したAPI Keyの使用量には注意してください
* 問題などあればIssueまで

---

## 🙏 ライセンス

[MIT License](./LICENSE).
