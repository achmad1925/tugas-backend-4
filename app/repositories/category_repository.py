class CategoryRepository:
    def __init__(self):
        self.categories = []
        self.next_id = 1

    def get_all(self):
        return self.categories

    def get_by_id(self, category_id):
        for category in self.categories:
            if category["id"] == category_id:
                return category
        return None

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

        category["name"] = data["name"]
        return category

    def delete(self, category_id):
        category = self.get_by_id(category_id)
        if category is None:
            return False

        self.categories.remove(category)
        return True