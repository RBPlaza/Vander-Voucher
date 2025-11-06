import streamlit as st

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"
WEBSITE_URL = "https://www.vanderhotel.com/food-drink"
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"
VOUCHER_CODE = "Ref:V12"
# ----------------

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
        color: #55555
