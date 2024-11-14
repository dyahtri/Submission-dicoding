import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('dashboard/hour.csv')

# Pastikan kolom 'dteday' ada sebagai kolom tanggal dalam data
data['dteday'] = pd.to_datetime(data['dteday'], errors='coerce')
data = data.dropna(subset=['dteday'])  # Hapus baris dengan tanggal yang tidak valid

# Konversi kolom yang seharusnya numerik
data['season'] = pd.to_numeric(data['season'], errors='coerce')
data['holiday'] = pd.to_numeric(data['holiday'], errors='coerce')
data['weathersit'] = pd.to_numeric(data['weathersit'], errors='coerce')
data['cnt'] = pd.to_numeric(data['cnt'], errors='coerce')

# Hapus baris dengan nilai NaN yang mungkin masih tersisa
data = data.dropna()

# Sidebar untuk filter
st.sidebar.title("Filter Data")
start_date = st.sidebar.date_input("Start Date", value=data['dteday'].min())
end_date = st.sidebar.date_input("End Date", value=data['dteday'].max())
filtered_data = data[(data['dteday'] >= pd.to_datetime(start_date)) & (data['dteday'] <= pd.to_datetime(end_date))]

# Menu pilihan
menu = st.sidebar.selectbox("Menu", ["Home", "Visualisasi", "Prediksi"])

# Bagian Home
if menu == "Home":
    st.title("Selamat Datang di Dashboard Penyewaan Sepeda")
    
    # Menampilkan gambar ilustrasi
    st.image("https://i.pinimg.com/736x/49/a1/f7/49a1f744d33146df192e65bf244c9474.jpg", caption="Ilustrasi Penyewaan Sepeda", use_column_width=True)
    st.write("Dashboard ini menyediakan visualisasi dan prediksi jumlah penyewaan sepeda berdasarkan data historis.")
    st.write("Pilih menu 'Visualisasi' untuk melihat grafik tren penyewaan sepeda atau 'Prediksi' untuk memprediksi jumlah penyewaan di masa depan.")

# Bagian Visualisasi
elif menu == "Visualisasi":
    st.title("Dashboard Penyewaan Sepeda")

    # Scatter Plot Pengaruh Kondisi Cuaca terhadap Penyewaan
    st.subheader("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=filtered_data, x='weathersit', y='cnt', color='blue')
    plt.xlabel("Kondisi Cuaca (weathersit)")
    plt.ylabel("Jumlah Penyewaan Sepeda (cnt)")
    plt.xticks([1, 2, 3, 4], ['Clear/Few clouds', 'Mist/Cloudy', 'Light Snow/Light Rain', 'Heavy Rain/Ice'])
    plt.title("Pengaruh Kondisi Cuaca terhadap Jumlah Penyewaan Sepeda")
    st.pyplot(plt)

    # Uji Korelasi
    correlation = filtered_data[['weathersit', 'cnt']].corr().iloc[0, 1]
    st.write(f"Korelasi antara kondisi cuaca dan jumlah penyewaan sepeda: {correlation:.2f}")

    # Line Chart untuk Tren Musiman Harian
    st.subheader("Tren Penyewaan Sepeda Berdasarkan Tanggal")
    daily_counts = filtered_data.groupby(['dteday'])['cnt'].sum().reset_index()
    daily_counts['dteday'] = pd.to_datetime(daily_counts['dteday'])
    daily_counts = daily_counts.set_index('dteday')

    plt.figure(figsize=(10, 6))
    plt.plot(daily_counts.index, daily_counts['cnt'], color='green', linewidth=2)
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Penyewaan Sepeda (cnt)")
    plt.title("Tren Penyewaan Sepeda Harian")
    st.pyplot(plt)

    # Visualisasi Tren Musiman berdasarkan Bulan
    st.subheader("Tren Penyewaan Sepeda Berdasarkan Musim dan Bulan")
    
    # Menambahkan kolom 'bulan' dan 'musim'
    filtered_data['bulan'] = filtered_data['dteday'].dt.month
    seasonal_monthly_counts = filtered_data.groupby(['season', 'bulan'])['cnt'].mean().reset_index()

    # Mapping musim ke nama
    seasonal_monthly_counts['season'] = seasonal_monthly_counts['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    
    # Visualisasi Tren Penyewaan Sepeda per Bulan dan Musim
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=seasonal_monthly_counts, x='bulan', y='cnt', hue='season', marker='o', palette='Set2')
    plt.xlabel("Bulan")
    plt.ylabel("Rata-rata Jumlah Penyewaan Sepeda")
    plt.title("Tren Penyewaan Sepeda Berdasarkan Bulan dan Musim")
    plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    st.pyplot(plt)

# Bagian Prediksi
elif menu == "Prediksi":
    st.title("Prediksi Jumlah Penyewaan Sepeda")

    # Input untuk prediksi
    season = st.selectbox("Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)", options=[1, 2, 3, 4])
    holiday = st.selectbox("Hari Libur (0: Tidak, 1: Ya)", options=[0, 1])
    weathersit = st.selectbox("Kondisi Cuaca (1: Clear, 2: Mist/Cloudy, 3: Light Snow/Rain, 4: Heavy Rain/Ice)", options=[1, 2, 3, 4])

    # Menyiapkan data untuk model
    y = data['cnt']
    X = pd.get_dummies(data[['season', 'holiday', 'weathersit']], drop_first=True)

    # Skala data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Membuat model regresi linear
    linear_model = LinearRegression().fit(X_scaled, y)

    # Data input untuk prediksi
    input_data = pd.DataFrame({
        'season': [season],
        'holiday': [holiday],
        'weathersit': [weathersit]
    })

    # Konversi input_data ke dalam bentuk dummy variables dan sesuaikan kolomnya
    input_data = pd.get_dummies(input_data, drop_first=True)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    # Skala data input
    input_data_scaled = scaler.transform(input_data)

    # Prediksi
    prediction = linear_model.predict(input_data_scaled)[0]
    st.write(f"Perkiraan jumlah penyewaan sepeda: {int(prediction)} unit")
