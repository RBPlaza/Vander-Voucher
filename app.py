import streamlit as st

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"
WEBSITE_URL = "https://www.vanderhotel.com/food-drink"
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"
VOUCHER_CODE = "Ref:V12"

# --- PAGE STYLING ---
st.markdown(
    """
    <style>
    body {
        background-color: #f8f8f8;
        font-family: 'Arial', sans-serif;
    }
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }
    .voucher-card {
        background-color: #ffffff;
        padding: 35px 25px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 400px;
        width: 90%;
    }
    .voucher-logo {
        width: 130px;
        margin-bottom: 20px;
    }
    .voucher-text {
        font-size: 1.2rem;
        color: #555555;
        margin-bottom: 10px;
    }
    .voucher-code {
        font-size: 2rem;
        font-weight: bold;
        color: #333333;
        margin-bottom: 25px;
    }
    .voucher-buttons a {
        display: inline-block;
        background-color: #0078D7;
        color: white;
        text-decoration: none;
        padding: 14px 28px;
        margin: 8px 4px;
        border-radius: 12px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .voucher-buttons a:hover {
        background-color: #005ea3;
    }
    .voucher-caption {
        font-size: 0.85rem;
        color: #888888;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- VOUCHER CARD ---
st.markdown(
    f"""
    <div class='voucher-card'>
        <img class='voucher-logo' src='{LOGO_URL}' alt='Logo'>
        <div class='voucher-text'>Free welcome drink with voucher:</div>
        <div class='voucher-code'>🎟️ {VOUCHER_CODE}</div>
        <div class='voucher-buttons'>
            <a href='{WEBSITE_URL}' target='_blank'>🌐 Visit Website</a>
            <a href='{LOCATION_URL}' target='_blank'>📍 View Location</a>
        </div>
        <div class='voucher-caption'>Show this voucher on your device</div>
    </div>
    """,
    unsafe_allow_html=True
)
