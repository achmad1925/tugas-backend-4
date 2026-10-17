class ItemService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self, min_price=None, category=None):
        if min_price is not None and min_price < 0:
            raise ValueError("Harga minimum tidak boleh negatif")

        return self.repository.get_all(min_price, category)

    def get_by_id(self, item_id):
        item = self.repository.get_by_id(item_id)

        if item is None:
            raise LookupError("Barang tidak ditemukan")

        return item

    def create(self, data):
        self._validate(data)

        for item in self.repository.get_all():
            if item["name"].lower() == data["name"].strip().lower():
                raise ValueError("Nama barang sudah digunakan")

        cleaned_data = {
            "name": data["name"].strip(),
            "price": data["price"],
            "category": data["category"].strip()
        }

        return self.repository.create(cleaned_data)

    def update(self, item_id, data):
        item = self.repository.get_by_id(item_id)

        if item is None:
            raise LookupError("Barang tidak ditemukan")

        merged_data = {**item, **data}
        self._validate(merged_data)

        for existing in self.repository.get_all():
            if (
                existing["id"] != item_id
                and existing["name"].lower()
                == merged_data["name"].strip().lower()
            ):
                raise ValueError("Nama barang sudah digunakan")

        cleaned_data = {
            "name": merged_data["name"].strip(),
            "price": merged_data["price"],
            "category": merged_data["category"].strip()
        }

        return self.repository.update(item_id, cleaned_data)

    def delete(self, item_id):
        item = self.repository.delete(item_id)

        if item is None:
            raise LookupError("Barang tidak ditemukan")

        return item

    def _validate(self, data):
        if not isinstance(data.get("name"), str) or not data["name"].strip():
            raise ValueError("Nama barang wajib diisi")

        if not isinstance(data.get("category"), str) or not data["category"].strip():
            raise ValueError("Kategori barang wajib diisi")

        price = data.get("price")

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Harga harus berupa angka")

        if price < 0:
            raise ValueError("Harga tidak boleh negatif")
