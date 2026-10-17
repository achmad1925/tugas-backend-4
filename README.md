# REST API Barang - Layered Architecture

## Deskripsi
Proyek ini merupakan refactoring REST API Barang
menggunakan Flask dengan arsitektur berlapis.

## Teknologi
- Python
- Flask
- REST API
- JSON

## Struktur Arsitektur

- **Route:** Mendefinisikan endpoint menggunakan Blueprint.
- **Controller:** Menangani request dan response HTTP.
- **Service:** Menjalankan validasi dan aturan bisnis.
- **Repository:** Mengelola data barang.
- **Application Factory:** Membuat aplikasi dan
  mendaftarkan Blueprint.

## Diagram Alur Layer

mermaid
flowchart TD
    A[Client] --> B[Blueprint Route]
    B --> C[Controller]
    C --> D[Service Layer]
    D --> E{Validasi Business Rule}
    E -->|Valid| F[Repository]
    E -->|Tidak Valid| G[Response Error 400]
    F --> H[(Penyimpanan Data)]
    H --> F
    F --> D
    D --> C
    C --> B
    B --> A

## Business Rules

1. Nama barang wajib diisi.
2. Nama barang harus unik.
3. Harga harus berupa angka dan tidak boleh negatif.
4. Barang yang tidak ditemukan menghasilkan HTTP 404.
5. Body request harus berupa objek JSON.

## Endpoint API

| Method | Endpoint | Fungsi |
|--------|----------|--------|
| GET | /api/v1/items | Menampilkan semua barang |
| GET | /api/v1/items?min_price=20000 | Filter harga |
| GET | /api/v1/items?category=Makanan | Filter kategori |
| GET | /api/v1/items/<id> | Mencari barang berdasarkan ID |
| POST | /api/v1/items | Menambah barang |
| PUT | /api/v1/items/<id> | Memperbarui barang |
| DELETE | /api/v1/items/<id> | Menghapus barang |

## Cara Menjalankan

1. Instal Flask dengan `pip install flask`.
2. Jalankan `python run.py`.
3. Akses `http://127.0.0.1:5000/api/v1/items`.

## Catatan
Penyimpanan data masih menggunakan list Python.
Data tidak tersimpan secara permanen setelah aplikasi
dimulai ulang.