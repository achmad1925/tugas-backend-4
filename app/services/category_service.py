from app.utils.exceptions import NotFoundError, ValidationError


class CategoryService:
    def __init__(self, repository, product_repository):
        self.repository = repository
        self.product_repository = product_repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, category_id):
        category = self.repository.get_by_id(category_id)

        if category is None:
            raise NotFoundError(
                f"Kategori dengan id {category_id} tidak ditemukan"
            )

        return category

    def create(self, data):
        name = self._validate_name(data)

        for category in self.repository.get_all():
            if category["name"].lower() == name.lower():
                raise ValidationError(
                    "name",
                    "Nama kategori sudah digunakan"
                )

        return self.repository.create({"name": name})

    def update(self, category_id, data):
        category = self.get_by_id(category_id)

        merged_data = {**category, **data}
        name = self._validate_name(merged_data)

        for existing in self.repository.get_all():
            if (
                existing["id"] != category_id
                and existing["name"].lower() == name.lower()
            ):
                raise ValidationError(
                    "name",
                    "Nama kategori sudah digunakan"
                )

        return self.repository.update(category_id, {"name": name})

    def delete(self, category_id):
        self.get_by_id(category_id)

        products = self.product_repository.get_all(
            category_id=category_id
        )

        if products:
            raise ValidationError(
                "id",
                "Kategori tidak dapat dihapus karena masih memiliki produk"
            )

        return self.repository.delete(category_id)

    def _validate_name(self, data):
        name = data.get("name")

        if not isinstance(name, str) or not name.strip():
            raise ValidationError("name", "Nama kategori wajib diisi")

        return name.strip()
