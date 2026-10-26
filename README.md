# REST API Kategori & Produk - Layered Architecture

## Deskripsi
Proyek ini merupakan REST API Kategori dan Produk
menggunakan Flask dengan arsitektur berlapis.
Resource `products` berelasi dengan `categories`
melalui field `category_id` (satu kategori memiliki
banyak produk).

## Teknologi
- Python
- Flask
- REST API
- JSON

## Struktur Arsitektur

- **Route:** Mendefinisikan endpoint menggunakan Blueprint.
- **Controller:** Menangani request dan response HTTP.
- **Service:** Menjalankan validasi dan aturan bisnis.
- **Repository:** Mengelola data pada list Python.
- **Utils:** `response_helper.py` (respons seragam)
  dan `exceptions.py` (ValidationError, NotFoundError).
- **Application Factory:** Membuat aplikasi dan
  mendaftarkan Blueprint.

## Format Response

Semua endpoint menggunakan `response_helper.py`.

Respons sukses (`success_response`):

```json
{
  "success": true,
  "message": "Data produk berhasil diambil",
  "data": []
}
```

Respons gagal (`fail_response`) selalu memuat
`field` (nama field yang menyebabkan kesalahan)
dan `message` (alasan kesalahan):

```json
{
  "success": false,
  "error": "Bad Request",
  "field": "price",
  "message": "Harga tidak boleh negatif"
}
```

## Tabel Spesifikasi API

### Resource Categories

| Method | URI | Input | Respons Sukses | Respons Gagal |
|--------|-----|-------|----------------|---------------|
| GET | `/api/v1/categories` | Tidak ada | `200` `{"success":true,"message":"Data kategori berhasil diambil","data":[{"id":1,"name":"Makanan"}]}` | `404` `{"success":false,"error":"Not Found","field":"uri","message":"Resource tidak ditemukan"}` |
| GET | `/api/v1/categories/<id>` | Path `id` (int) | `200` `{"success":true,"message":"Kategori berhasil ditemukan","data":{"id":1,"name":"Makanan"}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Kategori dengan id 99 tidak ditemukan"}` |
| POST | `/api/v1/categories` | Body JSON: `name` (string, wajib, unik) | `201` `{"success":true,"message":"Kategori berhasil ditambahkan","data":{"id":4,"name":"Alat Tulis"}}` | `400` `{"success":false,"error":"Bad Request","field":"name","message":"Nama kategori wajib diisi"}`; `400` `field":"name","message":"Nama kategori sudah digunakan"`; `400` `field":"body","message":"Body harus berupa objek JSON"` |
| PUT | `/api/v1/categories/<id>` | Path `id` (int); Body JSON: `name` (string, wajib, unik) | `200` `{"success":true,"message":"Kategori berhasil diperbarui","data":{"id":1,"name":"Makanan Ringan"}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Kategori dengan id 99 tidak ditemukan"}`; `400` `field":"name","message":"Nama kategori wajib diisi"`; `400` `field":"body","message":"Body harus berupa objek JSON"` |
| DELETE | `/api/v1/categories/<id>` | Path `id` (int) | `200` `{"success":true,"message":"Kategori berhasil dihapus","data":{"id":4,"name":"Alat Tulis"}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Kategori dengan id 99 tidak ditemukan"}`; `400` `field":"id","message":"Kategori tidak dapat dihapus karena masih memiliki produk"` |

### Resource Products

| Method | URI | Input | Respons Sukses | Respons Gagal |
|--------|-----|-------|----------------|---------------|
| GET | `/api/v1/products` | Query opsional: `min_price` (number), `category_id` (int, harus exist) | `200` `{"success":true,"message":"Data produk berhasil diambil","data":[{"id":1,"name":"Keripik Pisang","price":15000,"category_id":1}]}` | `400` `{"success":false,"error":"Bad Request","field":"min_price","message":"Harga minimum harus berupa angka"}`; `400` `field":"min_price","message":"Harga minimum tidak boleh negatif"`; `404` `field":"category_id","message":"Kategori dengan id 99 tidak ditemukan"` |
| GET | `/api/v1/products/<id>` | Path `id` (int) | `200` `{"success":true,"message":"Produk berhasil ditemukan","data":{"id":1,"name":"Keripik Pisang","price":15000,"category_id":1}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Produk dengan id 99 tidak ditemukan"}` |
| POST | `/api/v1/products` | Body JSON: `name` (string, wajib, unik), `price` (number >= 0, wajib), `category_id` (int, wajib, harus exist) | `201` `{"success":true,"message":"Produk berhasil ditambahkan","data":{"id":4,"name":"Teh Manis","price":8000,"category_id":2}}` | `400` `{"success":false,"error":"Bad Request","field":"name","message":"Nama produk wajib diisi"}`; `400` `field":"price","message":"Harga harus berupa angka"`; `400` `field":"price","message":"Harga tidak boleh negatif"`; `404` `field":"category_id","message":"Kategori dengan id 99 tidak ditemukan"`; `400` `field":"name","message":"Nama produk sudah digunakan"`; `400` `field":"body","message":"Body harus berupa objek JSON"` |
| PUT | `/api/v1/products/<id>` | Path `id` (int); Body JSON: `name`, `price`, `category_id` (ikut divalidasi jika dikirim) | `200` `{"success":true,"message":"Produk berhasil diperbarui","data":{"id":1,"name":"Keripik Pisang Premium","price":18000,"category_id":1}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Produk dengan id 99 tidak ditemukan"}`; `400` `field":"price","message":"Harga tidak boleh negatif"`; `404` `field":"category_id","message":"Kategori dengan id 99 tidak ditemukan"`; `400` `field":"body","message":"Body harus berupa objek JSON"` |
| DELETE | `/api/v1/products/<id>` | Path `id` (int) | `200` `{"success":true,"message":"Produk berhasil dihapus","data":{"id":1,"name":"Keripik Pisang","price":15000,"category_id":1}}` | `404` `{"success":false,"error":"Not Found","field":"id","message":"Produk dengan id 99 tidak ditemukan"}` |

## Business Rules

1. Nama kategori wajib diisi dan harus unik
   (tidak membedakan huruf besar/kecil).
2. Nama produk wajib diisi dan harus unik
   (tidak membedakan huruf besar/kecil).
3. Harga produk wajib berupa angka dan
   tidak boleh negatif.
4. `category_id` pada produk wajib merujuk ke
   kategori yang ada (resource berelasi).
5. Kategori yang masih memiliki produk tidak
   boleh dihapus.
6. Kategori/produk yang tidak ditemukan
   menghasilkan HTTP 404.
7. Body request harus berupa objek JSON.

## Cara Menjalankan

1. Instal Flask dengan `pip install flask`.
2. Jalankan `python run.py`.
3. Akses `http://127.0.0.1:5000/api/v1/categories`
   dan `http://127.0.0.1:5000/api/v1/products`.

## Catatan
Penyimpanan data masih menggunakan list Python.
Data tidak tersimpan secara permanen setelah aplikasi
dimulai ulang.
