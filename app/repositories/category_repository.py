class CategoryRepository:
    def __init__(self):
        self.categories = [
            {
                "id": 1,
                "name": "Makanan"
            },
            {
                "id": 2,
                "name": "Minuman"
            },
            {
                "id": 3,
                "name": "Kerajinan"
            }
        ]

        self.next_id = 4

    def get_all(self):
        return self.categories.copy()

    def get_by_id(self, category_id):
        return next(
            (category for category in self.categories
             if category["id"] == category_id),
            None
        )

    def create(self, data):
        category = {
            "id": self.next_id,
            "name": data["name"]
        }

        self.categories.append(category)
        self.next_id += 1

        return category

    def update(self, category_id, data):
        category = self.get_by_id(category_id)

        if category is None:
            return None

        category.update(data)
        return category

    def delete(self, category_id):
        category = self.get_by_id(category_id)

        if category is None:
            return None

        self.categories.remove(category)
        return category
