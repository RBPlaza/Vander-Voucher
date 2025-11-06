import streamlit as st
import json
import os
import random
import string

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"
WEBSITE_URL = "https://www.vanderhotel.com/food‑drink"
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"
PDF_FILE = "static/ChefsPlatesWinter.pdf"  # PDF in repo
COUNTER_FILE = "counter.json"

BUTTON_COLOR = "#353230"
BUTTON_HOVER = "#1e1c1a"
TEXT_PRIMARY = "#333333"
TEXT_SECONDARY = "#777777"
CARD_BG = "#ffffff"
PAGE_BG = "#f4f5f6"
STATIC_PREFIX = "V12/"
# ----------------

# --- Initialize counter file ---
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        json.dump({"number": 100}, f)

# --- Read + increment counter ---
with open(COUNTER_FILE, "r+") as f:
    data = json.load(f)
    number = data["number"]
    data["number"] += 1
    f.seek(0)
    json.dump(data, f)
    f.truncate()

# --- Generate random 5-character suffix ---
suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

# --- Final voucher code ---
VOUCHER_CODE = f"{STATIC_PREFIX}{number}{suffix}"

# --- PAGE STYLING ---
st.markdown(
    f"""
    <style>
      body {{
        background-color: {PAGE_BG};
        font-family: 'Arial', sans-serif;
        margin: 0; padding: 0;
      }}
      .voucher-card {{
        background-color: {CARD_BG};
        padding: 35px 25px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        text-align: center;
        max-width: 420px;
        width: 90%;
        margin: 40px auto;
      }}
      .voucher-logo {{
        width: 130px;
        margin-bottom: 20px;
      }}
      .voucher-text {{
        font-size: 1.2rem;
        color: {TEXT_SECONDARY};
        margin-bottom: 8px;
      }}
      .voucher-code {{
        font-size: 2rem;
        font-weight: bold;
        color: {TEXT_PRIMARY};
        margin-bottom: 25px;
      }}
      .voucher-buttons {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
        margin-bottom: 12px;
      }}
      .voucher-buttons a {{
        display: inline-block;
        background-color: {BUTTON_COLOR};
        color: white;
        text-decoration: none;
        padding: 12px 26px;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: background-color 0.3s ease;
      }}
      .voucher-buttons a:hover {{
        background-color: {BUTTON_HOVER};
      }}
      .voucher-caption {{
        font-size: 0.85rem;
        color: {TEXT_SECONDARY};
        margin-top: 18px;
      }}
      @media only screen and (max-width: 480px) {{
        .voucher-card {{
          margin-top: 20px;
        }}
        .voucher-code {{
          font-size: 1.8rem;
        }}
        .voucher-buttons a {{
          padding: 10px 20px;
          font-size: 0.9rem;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- VOUCHER CARD ---
st.markdown(
    f"""
    <div class="voucher-card">
      <img class="voucher-logo" src="{LOGO_URL}" alt="Logo">
      <div class="voucher-text">Free welcome drink with voucher:</div>
      <div class="voucher-code">🎟️ {VOUCHER_CODE}</div>
      <div class="voucher-buttons">
        <a href="{WEBSITE_URL}" target="_blank">🌐 Visit Website</a>
        <a href="{LOCATION_URL}" target="_blank">📍 View Location</a>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- PDF Download / Open Button ---
with open(PDF_FILE, "rb") as pdf_file:
    st.download_button(
        label="📄 View Menu",
        data=pdf_file,
        file_name="ChefsPlatesWinter.pdf",
        mime="application/pdf"
    )

st.caption("Please show this voucher on your device")
