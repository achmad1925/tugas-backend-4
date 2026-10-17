class ItemRepository:
    def __init__(self):
        self.items = [
            {
                "id": 1,
                "name": "Keripik Pisang",
                "price": 15000,
                "category": "Makanan"
            },
            {
                "id": 2,
                "name": "Kopi Bubuk",
                "price": 25000,
                "category": "Minuman"
            },
            {
                "id": 3,
                "name": "Gelas Bambu",
                "price": 30000,
                "category": "Kerajinan"
            }
        ]

        self.next_id = 4

    def get_all(self, min_price=None, category=None):
        result = self.items.copy()

        if min_price is not None:
            result = [
                item for item in result
                if item["price"] >= min_price
            ]

        if category:
            result = [
                item for item in result
                if item["category"].lower() == category.lower()
            ]

        return result

    def get_by_id(self, item_id):
        return next(
            (item for item in self.items
             if item["id"] == item_id),
            None
        )

    def create(self, data):
        item = {
            "id": self.next_id,
            "name": data["name"],
            "price": data["price"],
            "category": data["category"]
        }

        self.items.append(item)
        self.next_id += 1

        return item

    def update(self, item_id, data):
        item = self.get_by_id(item_id)

        if item is None:
            return None

        item.update(data)
        return item

    def delete(self, item_id):
        item = self.get_by_id(item_id)

        if item is None:
            return None

        self.items.remove(item)
        return item
