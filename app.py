import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model & fitur
model = joblib.load('model_rf.pkl')
feature_names = np.load('model_features.npy', allow_pickle=True)

st.title("📱 Prediksi Penjualan Produk Shopee")

st.markdown("Masukkan data produk untuk prediksi:")

# Form input
with st.form("form_prediksi"):
    price = st.number_input("Harga Produk (Rp)", min_value=0, value=1500000)
    rating = st.slider("Rating Produk", 0.0, 5.0, 4.5, step=0.1)
    address = st.selectbox("Lokasi Penjual", sorted([
        'Bandung', 'Bekasi', 'Binjai', 'Bogor', 'Depok', 'Dumai',
        'Jakarta Barat', 'Jakarta Pusat', 'Jakarta Selatan', 'Jakarta Utara',
        'Kab. Bandung Barat', 'Kab. Bekasi', 'Kab. Bogor', 'Kab. Cirebon',
        'Kab. Jember', 'Kab. Pasuruan', 'Kab. Sleman', 'Kab. Tangerang',
        'Malang', 'Palembang', 'Surabaya', 'Tangerang',
        'Tasikmalaya', 'Tegal'
    ]))

    submitted = st.form_submit_button("Prediksi")

if submitted:
    # Inisialisasi data input kosong
    input_dict = {feature: 0 for feature in feature_names}
    input_dict['price'] = price
    input_dict['rating'] = rating

    # Ubah alamat ke format one-hot
    address_col = f'address_{address}'
    if address_col in input_dict:
        input_dict[address_col] = 1
    else:
        st.warning(f"Alamat '{address}' tidak ditemukan dalam model. Menggunakan default.")

    # Buat DataFrame dengan urutan kolom sesuai model
    input_df = pd.DataFrame([input_dict], columns=feature_names)

    # Prediksi
    prediksi = model.predict(input_df)[0]
    st.success(f"📦 Estimasi produk terjual: **{int(prediksi):,} unit**")
