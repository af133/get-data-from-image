
```markdown
# Transaction Data Extractor (OCR)

Tool berbasis Streamlit untuk mengekstraksi data dari screenshot aplikasi kasir secara otomatis menggunakan AI (EasyOCR) dan menyimpannya ke format CSV yang terstruktur.

## Fitur Utama
- **Ekstraksi Otomatis**: Mengambil data transaksi dari kumpulan gambar di folder.
- **Auto-Cleaning**: Menghapus duplikat data secara otomatis.
- **Auto-Sorting**: Mengurutkan data berdasarkan Nomor Transaksi.
- **Downloadable**: Langsung unduh hasil ekstraksi dalam format CSV siap training.

## Cara Instalasi

1. **Clone repositori ini:**
   ```bash
   git clone [https://github.com/af133/get-data-from-image.git](https://github.com/af133/get-data-from-image.git)
   cd get-data-from-image

```

2. **Buat Virtual Environment (Sangat disarankan):**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

```


3. **Install dependencies:**
Pastikan Anda sudah memiliki file `requirements.txt` di folder yang sama, lalu jalankan:
```bash
pip install -r requirement.txt

```



## Cara Menjalankan

1. Jalankan aplikasi Streamlit:
```bash
streamlit run vaneca.py

```


2. Aplikasi akan terbuka secara otomatis di browser Anda (biasanya di `http://localhost:8501`).
3. Masukkan **path folder** yang berisi screenshot Anda di kolom input yang tersedia.
4. Klik tombol **"Mulai Proses & Sort"**.

## Struktur Data

Data akan diproses menjadi kolom:

* `Nomor` | `Jam` | `Total_Transaksi` | `Kode_Barang` | `Nama_Barang` | `Jumlah` | `Harga`

---

*Catatan: Saat pertama kali dijalankan, EasyOCR akan mengunduh model AI (sekitar 500MB). Proses ini hanya terjadi satu kali.*

```

---

### Jangan lupa pastikan folder proyek Anda memiliki isi berikut:
1.  **`vaneca.py`** (file kode utama Anda).
2.  **`requirements.txt`** (isinya: `streamlit`, `pandas`, `easyocr`, `pillow`, `torch`).
3.  **`README.md`** (isi yang di atas).


```