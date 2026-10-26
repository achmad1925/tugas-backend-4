from flask import request

from app.utils.exceptions import NotFoundError, ValidationError
from app.utils.response_helper import fail_response, success_response


class ProductController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        min_price_raw = request.args.get("min_price")
        min_price = request.args.get("min_price", type=float)

        if min_price_raw is not None and min_price is None:
            return fail_response(
                "min_price",
                "Harga minimum harus berupa angka"
            )

        category_id_raw = request.args.get("category_id")
        category_id = request.args.get("category_id", type=int)

        if category_id_raw is not None and category_id is None:
            return fail_response(
                "category_id",
                "Id kategori harus berupa angka"
            )

        try:
            products = self.service.get_all(min_price, category_id)
            return success_response(
                products,
                "Data produk berhasil diambil"
            )
        except ValidationError as error:
            return fail_response(error.field, error.reason)
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)

    def get_by_id(self, product_id):
        try:
            product = self.service.get_by_id(product_id)
            return success_response(
                product,
                "Produk berhasil ditemukan"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)

    def create(self):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return fail_response("body", "Body harus berupa objek JSON")

        try:
            product = self.service.create(data)
            return success_response(
                product,
                "Produk berhasil ditambahkan",
                201
            )
        except ValidationError as error:
            return fail_response(error.field, error.reason)
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)

    def update(self, product_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return fail_response("body", "Body harus berupa objek JSON")

        try:
            product = self.service.update(product_id, data)
            return success_response(
                product,
                "Produk berhasil diperbarui"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)
        except ValidationError as error:
            return fail_response(error.field, error.reason)

    def delete(self, product_id):
        try:
            product = self.service.delete(product_id)
            return success_response(
                product,
                "Produk berhasil dihapus"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)
