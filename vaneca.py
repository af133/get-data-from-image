import streamlit as st
import pandas as pd
import os
import easyocr
import re
@st.cache_resource
def get_reader():
    return easyocr.Reader(['id', 'en'])

reader = get_reader()

def proses_gambar(img_path):
    try:
        # Mengambil teks dalam bentuk list
        results = reader.readtext(img_path, detail=0)
        pola_nomor = r'\d{2}C-\d{6}-[A-Z]'
        
        data_transaksi = []
        
        # Iterasi mencari nomor transaksi
        for i, text in enumerate(results):
            if re.search(pola_nomor, text):
                nomor = text
                
                if i + 8 < len(results):
                    data_transaksi.append({
                        'Nomor': nomor,
                        'Jam': results[i+2],
                        'Total_Transaksi': results[i+4],
                        'Kode_Barang': results[i+5],
                        'Nama_Barang': results[i+6],
                        'Jumlah': results[i+8],
                        'Harga': results[i+9]
                    })
        return data_transaksi
    except Exception:
        return []

st.set_page_config(page_title="Dataset Builder Transaksi", layout="wide")
st.title("Tool Ekstraksi & Sorting Data Transaksi")

folder_path = st.text_input("Masukkan path folder gambar:", r"C:\Projek Pribadi\screenshots\0Screenshots")

if st.button("Mulai Proses & Sort"):
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        
        if not files:
            st.error("Tidak ditemukan file gambar!")
        else:
            semua_data = []
            for file in files:
                hasil = proses_gambar(os.path.join(folder_path, file))
                semua_data.extend(hasil)
            
            if semua_data:
                df = pd.DataFrame(semua_data)
                df = df.drop_duplicates()
                df = df.sort_values(by='Nomor', ascending=True)
                st.success(f"Berhasil mengekstraksi dan mengurutkan {len(df)} baris data!")
                st.dataframe(df)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button("Download CSV Dataset", csv, "dataset_transaksi_final.csv", "text/csv")
            else:
                st.warning("Data tidak terbaca, periksa apakah screenshot sudah jelas.")
    else:
        st.error("Folder tidak ditemukan!")