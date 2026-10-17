from flask import jsonify, request


class CategoryController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        return jsonify(self.service.get_all()), 200

    def get_by_id(self, category_id):
        try:
            return jsonify(self.service.get_by_id(category_id)), 200
        except LookupError as error:
            return jsonify({
                "error": "Not Found",
                "message": str(error)
            }), 404

    def create(self):
        data = request.get_json(silent=True) or {}

        try:
            category = self.service.create(data)
            return jsonify(category), 201
        except ValueError as error:
            return jsonify({
                "error": "Bad Request",
                "message": str(error)
            }), 400

    def update(self, category_id):
        data = request.get_json(silent=True) or {}

        try:
            category = self.service.update(category_id, data)
            return jsonify(category), 200
        except LookupError as error:
            return jsonify({
                "error": "Not Found",
                "message": str(error)
            }), 404
        except ValueError as error:
            return jsonify({
                "error": "Bad Request",
                "message": str(error)
            }), 400

    def delete(self, category_id):
        try:
            self.service.delete(category_id)
            return jsonify({
                "message": "Kategori berhasil dihapus"
            }), 200
        except LookupError as error:
            return jsonify({
                "error": "Not Found",
                "message": str(error)
            }), 404