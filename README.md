# Finance Tracker

Aplikasi pencatat keuangan pribadi sederhana berbasis web, dibuat dengan Python, Flask, dan SQLite. Mencatat pemasukan dan pengeluaran, menampilkan ringkasan saldo, serta mendukung tambah, edit, dan hapus transaksi — semuanya berjalan lokal di browser.

## Fitur

- Tambah transaksi (pemasukan/pengeluaran) dengan kategori dan deskripsi
- Edit dan hapus transaksi
- Ringkasan otomatis: total pemasukan, pengeluaran, dan saldo
- Validasi input di sisi server (jumlah harus angka positif, field wajib diisi)
- Data tersimpan secara lokal di SQLite, tidak ada data yang dikirim ke server lain

## Tech Stack

- **Python** — bahasa utama
- **Flask** — web framework
- **SQLite** — database lokal
- **Jinja2** — template engine untuk HTML dinamis

## Cara Menjalankan

1. Clone repository ini:
```bash
   git clone <url-repo-kamu>
   cd finance-tracker
```

2. Buat dan aktifkan virtual environment:
```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
```

3. Install dependencies:
```bash
   pip install -r requirements.txt
```

4. Jalankan aplikasi:
```bash
   python app.py
```

5. Buka browser ke `http://127.0.0.1:5000`

## Struktur Project
finance-tracker/
├── app.py # Routing dan logika Flask
├── database.py # Semua operasi database (CRUD)
├── static/
│ └── style.css # Styling halaman
├── templates/
│ ├── index.html # Halaman utama (daftar transaksi + form tambah)
│ └── edit.html # Halaman edit transaksi
└── requirements.txt

## Pembelajaran dari Project Ini

Project ini dibuat sebagai latihan memahami alur kerja aplikasi web full-stack sederhana: dari database (SQLite), logika server (Flask), hingga tampilan (HTML + Jinja2), termasuk penanganan input tidak valid dan debugging alur request/response.