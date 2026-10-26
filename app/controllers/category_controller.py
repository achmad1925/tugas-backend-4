from flask import request

from app.utils.exceptions import NotFoundError, ValidationError
from app.utils.response_helper import fail_response, success_response


class CategoryController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        try:
            categories = self.service.get_all()
            return success_response(
                categories,
                "Data kategori berhasil diambil"
            )
        except ValidationError as error:
            return fail_response(error.field, error.reason)

    def get_by_id(self, category_id):
        try:
            category = self.service.get_by_id(category_id)
            return success_response(
                category,
                "Kategori berhasil ditemukan"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)

    def create(self):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return fail_response("body", "Body harus berupa objek JSON")

        try:
            category = self.service.create(data)
            return success_response(
                category,
                "Kategori berhasil ditambahkan",
                201
            )
        except ValidationError as error:
            return fail_response(error.field, error.reason)

    def update(self, category_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return fail_response("body", "Body harus berupa objek JSON")

        try:
            category = self.service.update(category_id, data)
            return success_response(
                category,
                "Kategori berhasil diperbarui"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)
        except ValidationError as error:
            return fail_response(error.field, error.reason)

    def delete(self, category_id):
        try:
            category = self.service.delete(category_id)
            return success_response(
                category,
                "Kategori berhasil dihapus"
            )
        except NotFoundError as error:
            return fail_response(error.field, error.reason, 404)
        except ValidationError as error:
            return fail_response(error.field, error.reason)
