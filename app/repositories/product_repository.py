class ProductRepository:
    def __init__(self):
        self.products = [
            {
                "id": 1,
                "name": "Keripik Pisang",
                "price": 15000,
                "category_id": 1
            },
            {
                "id": 2,
                "name": "Kopi Bubuk",
                "price": 25000,
                "category_id": 2
            },
            {
                "id": 3,
                "name": "Gelas Bambu",
                "price": 30000,
                "category_id": 3
            }
        ]

        self.next_id = 4

    def get_all(self, min_price=None, category_id=None):
        result = self.products.copy()

        if min_price is not None:
            result = [
                product for product in result
                if product["price"] >= min_price
            ]

        if category_id is not None:
            result = [
                product for product in result
                if product["category_id"] == category_id
            ]

        return result

    def get_by_id(self, product_id):
        return next(
            (product for product in self.products
             if product["id"] == product_id),
            None
        )

    def create(self, data):
        product = {
            "id": self.next_id,
            "name": data["name"],
            "price": data["price"],
            "category_id": data["category_id"]
        }

        self.products.append(product)
        self.next_id += 1

        return product

    def update(self, product_id, data):
        product = self.get_by_id(product_id)

        if product is None:
            return None

        product.update(data)
        return product

    def delete(self, product_id):
        product = self.get_by_id(product_id)

        if product is None:
            return None

        self.products.remove(product)
        return product
