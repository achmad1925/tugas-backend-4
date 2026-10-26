from app.utils.exceptions import NotFoundError, ValidationError


class ProductService:
    def __init__(self, repository, category_repository):
        self.repository = repository
        self.category_repository = category_repository

    def get_all(self, min_price=None, category_id=None):
        if min_price is not None and min_price < 0:
            raise ValidationError(
                "min_price",
                "Harga minimum tidak boleh negatif"
            )

        if category_id is not None:
            self._ensure_category_exists(category_id)

        return self.repository.get_all(min_price, category_id)

    def get_by_id(self, product_id):
        product = self.repository.get_by_id(product_id)

        if product is None:
            raise NotFoundError(
                f"Produk dengan id {product_id} tidak ditemukan"
            )

        return product

    def create(self, data):
        name, price, category_id = self._validate(data)

        for product in self.repository.get_all():
            if product["name"].lower() == name.lower():
                raise ValidationError(
                    "name",
                    "Nama produk sudah digunakan"
                )

        return self.repository.create({
            "name": name,
            "price": price,
            "category_id": category_id
        })

    def update(self, product_id, data):
        product = self.get_by_id(product_id)

        merged_data = {**product, **data}
        name, price, category_id = self._validate(merged_data)

        for existing in self.repository.get_all():
            if (
                existing["id"] != product_id
                and existing["name"].lower() == name.lower()
            ):
                raise ValidationError(
                    "name",
                    "Nama produk sudah digunakan"
                )

        return self.repository.update(product_id, {
            "name": name,
            "price": price,
            "category_id": category_id
        })

    def delete(self, product_id):
        product = self.repository.delete(product_id)

        if product is None:
            raise NotFoundError(
                f"Produk dengan id {product_id} tidak ditemukan"
            )

        return product

    def _validate(self, data):
        name = data.get("name")

        if not isinstance(name, str) or not name.strip():
            raise ValidationError("name", "Nama produk wajib diisi")

        price = data.get("price")

        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValidationError("price", "Harga harus berupa angka")

        if price < 0:
            raise ValidationError("price", "Harga tidak boleh negatif")

        category_id = data.get("category_id")

        if (
            isinstance(category_id, bool)
            or not isinstance(category_id, int)
        ):
            raise ValidationError(
                "category_id",
                "Kategori produk wajib diisi dengan id kategori yang valid"
            )

        self._ensure_category_exists(category_id)

        return name.strip(), price, category_id

    def _ensure_category_exists(self, category_id):
        if self.category_repository.get_by_id(category_id) is None:
            raise NotFoundError(
                f"Kategori dengan id {category_id} tidak ditemukan",
                field="category_id"
            )
