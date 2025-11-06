import streamlit as st
import json
import os

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"  # change to your logo
WEBSITE_URL = "https://www.vanderhotel.com/food-drink"  # change to your site
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"  # change to your map link
PREFIX = "Ref:V12/"
COUNTER_FILE = "counter.json"
# ----------------

# initialize counter file if not exists
if not os.path.exists(COUNTER_FILE):
    with open(COUNTER_FILE, "w") as f:
        json.dump({"number": 100}, f)

# read + increment voucher number
with open(COUNTER_FILE, "r+") as f:
    data = json.load(f)
    number = data["number"]
    data["number"] += 1
    f.seek(0)
    json.dump(data, f)
    f.truncate()

voucher_number = f"{PREFIX}/{number}"

# --- UI ---
st.image(LOGO_URL, width=120)
st.markdown(f"### 🎟️ **Voucher: {voucher_number}**")
st.link_button("🌐 Visit Website", WEBSITE_URL)
st.link_button("📍 View Location", LOCATION_URL)

st.caption("Each scan generates a new voucher number automatically.")
