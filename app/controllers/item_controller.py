from flask import jsonify, request


class ItemController:
    def __init__(self, service):
        self.service = service

    def get_all(self):
        try:
            min_price = request.args.get("min_price", type=float)
            category = request.args.get("category")

            items = self.service.get_all(min_price, category)
            return jsonify(items), 200
        except ValueError as error:
            return jsonify({
                "error": "Bad Request",
                "message": str(error)
            }), 400

    def get_by_id(self, item_id):
        try:
            return jsonify(self.service.get_by_id(item_id)), 200
        except LookupError as error:
            return jsonify({
                "error": "Not Found",
                "message": str(error)
            }), 404

    def create(self):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "error": "Bad Request",
                "message": "Body harus berupa objek JSON"
            }), 400

        try:
            item = self.service.create(data)
            return jsonify(item), 201
        except ValueError as error:
            return jsonify({
                "error": "Bad Request",
                "message": str(error)
            }), 400

    def update(self, item_id):
        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({
                "error": "Bad Request",
                "message": "Body harus berupa objek JSON"
            }), 400

        try:
            item = self.service.update(item_id, data)
            return jsonify({
                "message": "Barang berhasil diperbarui",
                "data": item
            }), 200
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

    def delete(self, item_id):
        try:
            item = self.service.delete(item_id)
            return jsonify({
                "message": "Barang berhasil dihapus",
                "data": item
            }), 200
        except LookupError as error:
            return jsonify({
                "error": "Not Found",
                "message": str(error)
            }), 404
