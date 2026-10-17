from flask import Flask, jsonify

from app.repositories.item_repository import ItemRepository
from app.services.item_service import ItemService
from app.controllers.item_controller import ItemController
from app.routes.item_route import create_item_blueprint


def create_app():
    app = Flask(__name__)

    # Menyiapkan resource items
    item_repository = ItemRepository()
    item_service = ItemService(item_repository)
    item_controller = ItemController(item_service)

    # Mendaftarkan blueprint items
    app.register_blueprint(
        create_item_blueprint(item_controller)
    )

    # Respons error 404 yang seragam
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "Resource tidak ditemukan"
        }), 404

    return app