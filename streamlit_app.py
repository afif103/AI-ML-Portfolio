import streamlit as st
import requests

# === CONFIG ===
API_URL = "https://house-price-api-mcdo.onrender.com/predict"
st.set_page_config(page_title="AI House Price", page_icon="house", layout="centered")

# === HEADER ===
st.title("AI House Price Predictor")
st.markdown("**Real XGBoost model trained on 10,000+ homes**")
st.markdown("Enter details → Get **instant AI valuation**")

# === INPUT SLIDERS ===
col1, col2 = st.columns(2)
with col1:
    bedrooms = st.slider("Bedrooms", 1, 10, 3)
    sqft_living = st.slider("Living Area (sqft)", 500, 10000, 2000, step=100)
with col2:
    sqft_lot = st.slider("Lot Size (sqft)", 1000, 50000, 8000, step=500)
    bathrooms = st.slider("Bathrooms", 1, 8, 2)

# === PREDICTION ===
if st.button("Predict Price", type="primary", use_container_width=True):
    payload = {
        "features": [bedrooms, sqft_living, sqft_lot, 1500, bathrooms]
    }
    with st.spinner("Running AI model..."):
        try:
            response = requests.post(API_URL, json=payload, timeout=15)
            if response.status_code == 200:
                price = response.json()['price']
                st.success(f"### Predicted Price: **${price:,.0f}**")
                st.balloons()
                st.caption(f"Based on {bedrooms} bed, {sqft_living} sqft living, {bathrooms} bath")
            else:
                st.error("API returned an error. Try again.")
        except requests.exceptions.RequestException:
            st.error("Connection failed. Your API is live — retry in 10 seconds.")
else:
    st.info("Adjust sliders and click **Predict Price**")

# === FOOTER ===
st.markdown("---")
st.markdown(
    "Built by **Afif** | "
    "[GitHub](https://github.com/afif103/AI-ML-Portfolio) | "
    "[API](https://house-price-api-mcdo.onrender.com)"
)