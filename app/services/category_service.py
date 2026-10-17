class CategoryService:
    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, category_id):
        category = self.repository.get_by_id(category_id)
        if category is None:
            raise LookupError("Kategori tidak ditemukan")
        return category

    def create(self, data):
        name = data.get("name")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Nama kategori wajib diisi")

        for category in self.repository.get_all():
            if category["name"].lower() == name.strip().lower():
                raise ValueError("Nama kategori sudah digunakan")

        return self.repository.create({"name": name.strip()})

    def update(self, category_id, data):
        self.get_by_id(category_id)

        name = data.get("name")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Nama kategori wajib diisi")

        for category in self.repository.get_all():
            if (
                category["id"] != category_id
                and category["name"].lower() == name.strip().lower()
            ):
                raise ValueError("Nama kategori sudah digunakan")

        return self.repository.update(
            category_id, {"name": name.strip()}
        )

    def delete(self, category_id):
        self.get_by_id(category_id)
        self.repository.delete(category_id)