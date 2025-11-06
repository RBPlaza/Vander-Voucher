import streamlit as st

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"
WEBSITE_URL = "https://www.vanderhotel.com/food-drink"
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"
VOUCHER_CODE = "V12"
# ----------------

# --- PAGE STYLING ---
st.markdown(
    """
    <style>
    /* Center everything */
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh;
        background-color: #f8f8f8;
        font-family: 'Arial', sans-serif;
    }
    /* Card style */
    .voucher-card {
        background-color: #ffffff;
        padding: 30px 25px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        text-align: center;
        max-width: 400px;
        width: 90%;
    }
    .voucher-logo {
        width: 120px;
        margin-bottom: 20px;
    }
    .voucher-code {
        font-size: 1.8rem;
        font-weight: bold;
        margin: 20px 0;
        color: #333333;
    }
    .voucher-buttons a {
        display: inline-block;
        background-color: #0078D7;
        color: white;
        text-decoration: none;
        padding: 12px 20px;
        margin: 8px;
        border-radius: 12px;
        font-weight: bold;
    }
    .voucher-caption {
        font-size: 0.85rem;
        color: #666666;
        margin-top: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- VOUCHER CARD ---
st.markdown(
    f"""
    <div class="voucher-card">
        <img class="voucher-logo" src="{LOGO_URL}" alt="Logo">
        <div class="voucher-code">🎟️ Free Welcome drink Voucher code: {VOUCHER_CODE}</div>
        <div class="voucher-buttons">
            <a href="{WEBSITE_URL}" target="_blank">🌐 Visit Website</a>
            <a href="{LOCATION_URL}" target="_blank">📍 View Location</a>
        </div>
        <div class="voucher-caption">Show this voucher on your device</div>
    </div>
    """,
    unsafe_allow_html=True
)

