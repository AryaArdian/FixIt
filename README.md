# FixIt – Don't Replace It. Fix It.

Alur: **Problem → Diagnosis → Safe Tutorial → Repair Service**.
Versi ini **tanpa database**: semua data ada di file Python. Diagnosis rule-based (bukan AI) di `services/diagnosis.py`.

**Teknologi:** Python, Flask, Tailwind CSS (CDN), JavaScript.

## Struktur
`app.py` (entry) · `routes/main.py` (halaman) · `services/catalog.py` (kategori & repair service) · `services/diagnosis.py` (logika diagnosis) · `templates/` · `static/`

## Menjalankan di Windows (PowerShell)
```powershell
cd FixIt
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env      # lalu isi SECRET_KEY
python app.py
```
Buka http://127.0.0.1:5000

## Mengubah data
Edit `services/catalog.py` (kategori & service) lalu simpan; server debug memuat ulang otomatis.

## Catatan
- Hasil diagnosis dibawa lewat URL (`/result/<item>?q=...`), jadi aman di-refresh dan bisa dibagikan. Tidak ada riwayat laporan.
- Foto hanya divalidasi dan dipreview di browser; tidak disimpan dan belum dianalisis.
- Tidak ada admin/CRUD/login. Jika nanti butuh database, ubah 3 fungsi di bagian bawah `catalog.py`.

## Push ke GitHub
```powershell
git add .
git commit -m "No-database mode"
git push
```
(Pertama kali: `git init`, `git branch -M main`, `git remote add origin https://github.com/USERNAME/FixIt.git`, lalu `git push -u origin main`.)

## Deploy ke Vercel
Import repo di vercel.com → tambahkan env `SECRET_KEY` → Deploy. `vercel.json` sudah disiapkan. Karena tidak menulis ke disk, tidak ada masalah penyimpanan di Vercel.
