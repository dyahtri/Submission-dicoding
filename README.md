# Bike Rental Dashboard

Dashboard ini bertujuan untuk melakukan visualisasi dan prediksi jumlah penyewaan sepeda berdasarkan data historis. Dibangun menggunakan Python, Streamlit, dan beberapa pustaka data science lainnya.

## Fitur

- **Home**: Berisi pengantar dan gambar ilustrasi terkait penyewaan sepeda.
- **Visualisasi**: Menampilkan grafik pengaruh kondisi cuaca terhadap jumlah penyewaan sepeda dan tren penyewaan sepeda berdasarkan tanggal.
- **Prediksi**: Melakukan prediksi jumlah penyewaan sepeda berdasarkan musim, hari libur, dan kondisi cuaca.

## Persyaratan

- Python 3.7 atau lebih tinggi
- Pastikan pustaka yang diperlukan sudah terinstall. Pustaka-pustaka tersebut dapat diinstall melalui `requirements.txt`.

## Instalasi

1. Clone repositori ini ke komputer Anda:
   ```bash
   git clone https://github.com/dyahtri/Submission-dicoding.git
   
2. Masuk ke direktori project:
   ```bash
   cd Submission-dicoding/dashboard
   ```
   
3. Install semua dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Aplikasi

1. Pastikan Anda berada di direktori `dashboard`.
2. Jalankan aplikasi Streamlit dengan perintah berikut:
   ```bash
   streamlit run dashboard.py
   ```
3. Buka browser Anda dan akses alamat lokal yang diberikan, biasanya [http://localhost:8501](http://localhost:8501).

## Struktur Proyek

- `dashboard.py`: Kode utama untuk aplikasi Streamlit.
- `hour.csv`: Dataset historis untuk penyewaan sepeda.
- `requirements.txt`: Daftar pustaka yang diperlukan untuk menjalankan aplikasi ini.

## Penggunaan

1. **Home**: Baca pengantar untuk memahami konteks dari dashboard ini.
2. **Visualisasi**: Gunakan fitur visualisasi untuk melihat hubungan antara kondisi cuaca dan tren penyewaan sepeda.
3. **Prediksi**: Masukkan variabel input untuk musim, hari libur, dan kondisi cuaca, lalu klik prediksi untuk melihat estimasi jumlah penyewaan sepeda.

## Catatan

Jika terdapat error terkait file `hour.csv` saat menjalankan aplikasi, pastikan file `hour.csv` berada di direktori yang sama dengan `dashboard.py`. Anda juga bisa memperbarui path pada `dashboard.py` agar sesuai dengan lokasi file `hour.csv`.


Instruksi ini harus membantu dalam menjalankan aplikasi dan melakukan pemeriksaan lebih lanjut.
