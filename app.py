import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model_rf.pkl')

st.set_page_config(page_title="Prediksi Penjualan Shopee", layout="wide")
st.title("📱 Prediksi Penjualan Produk Shopee")

st.markdown("Masukkan informasi produk untuk memprediksi berapa unit akan terjual.")

# Form input fitur
with st.form("form_prediksi"):
    harga = st.number_input("Harga Produk (Rp)", min_value=0, value=1500000)
    rating = st.slider("Rating Produk (0.0 - 5.0)", 0.0, 5.0, 4.5, step=0.1)
    lokasi = st.selectbox("Lokasi Penjual", ['DKI Jakarta', 'Jawa Barat', 'Jawa Tengah', 'DI Yogyakarta', 'Banten'])
    
    submitted = st.form_submit_button("Prediksi")

# Prediksi
if submitted:
    # Encoding lokasi manual (harus sesuai preprocessing model)
    lokasi_encoded = {
        'DKI Jakarta': 0,
        'Jawa Barat': 1,
        'Jawa Tengah': 2,
        'DI Yogyakarta': 3,
        'Banten': 4
    }

    data_input = pd.DataFrame({
        'price': [harga],
        'rating': [rating],
        'address': [lokasi_encoded.get(lokasi, 0)]
    })

    prediksi = model.predict(data_input)[0]
    st.success(f"📦 Estimasi produk terjual: **{int(prediksi):,} unit**")