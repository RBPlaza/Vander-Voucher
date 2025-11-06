import streamlit as st

st.set_page_config(page_title="Voucher", page_icon="🎟️", layout="centered")

# --- SETTINGS ---
LOGO_URL = "https://kabinet01.net/wp-content/uploads/2020/02/VANDER-logo.png"
WEBSITE_URL = "https://www.vanderhotel.com/food‑drink"
LOCATION_URL = "https://maps.app.goo.gl/Hb5fZGGMMBcbaGzDA"
VOUCHER_CODE = "Ref:V12"
ACCENT_BLUE = "#0066cc"   # brand‑style blue (adjust if needed)
BUTTON_HOVER = "#0055a3"
TEXT_PRIMARY = "#333333"
TEXT_SECONDARY = "#777777"
CARD_BG = "#ffffff"
PAGE_BG = "#f4f5f6"
# ----------------

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
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        text-align: center;
        max-width: 420px;
        width: 90%;
        margin: 60px auto;
      }}
      .voucher-logo {{
        width: 140px;
        margin-bottom: 25px;
      }}
      .voucher-text {{
        font-size: 1.2rem;
        color: {TEXT_SECONDARY};
        margin-bottom: 8px;
      }}
      .voucher-code {{
        font-size: 2.2rem;
        font-weight: bold;
        color: {TEXT_PRIMARY};
        margin-bottom: 30px;
      }}
      .voucher‑buttons a {{
        display: inline-block;
        background-color: {ACCENT_BLUE};
        color: white;
        text-decoration: none;
        padding: 16px 32px;
        margin: 10px 6px;
        border-radius: 14px;
        font-weight: 600;
        transition: background-color 0.3s ease;
      }}
      .voucher‑buttons a:hover {{
        background-color: {BUTTON_HOVER};
      }}
      .voucher-caption {{
        font-size: 0.9rem;
        color: {TEXT_SECONDARY};
        margin-top: 22px;
      }}
      @media only screen and (max-width: 480px) {{
        .voucher-code {{
          font-size: 1.8rem;
        }}
        .voucher‑buttons a {{
          padding: 14px 24px;
          margin: 8px 4px;
        }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="voucher-card">
      <img class="voucher-logo" src="{LOGO_URL}" alt="Logo">
      <div class="voucher-text">Free welcome drink with voucher:</div>
      <div class="voucher-code">🎟️ {VOUCHER_CODE}</div>
      <div class="voucher‑buttons">
        <a href="{WEBSITE_URL}" target="_blank">🌐 Visit Website</a>
        <a href="{LOCATION_URL}" target="_blank">📍 View Location</a>
      </div>
      <div class="voucher-caption">Please show this voucher on your device</div>
    </div>
    """,
    unsafe_allow_html=True,
)
