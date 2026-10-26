from flask import Flask

from app.repositories.category_repository import CategoryRepository
from app.repositories.product_repository import ProductRepository
from app.services.category_service import CategoryService
from app.services.product_service import ProductService
from app.controllers.category_controller import CategoryController
from app.controllers.product_controller import ProductController
from app.routes.category_route import create_category_blueprint
from app.routes.product_route import create_product_blueprint
from app.utils.response_helper import fail_response


def create_app():
    app = Flask(__name__)

    # Menyiapkan resource categories dan products
    category_repository = CategoryRepository()
    product_repository = ProductRepository()

    category_service = CategoryService(
        category_repository,
        product_repository
    )
    product_service = ProductService(
        product_repository,
        category_repository
    )

    category_controller = CategoryController(category_service)
    product_controller = ProductController(product_service)

    # Mendaftarkan blueprint
    app.register_blueprint(
        create_category_blueprint(category_controller)
    )
    app.register_blueprint(
        create_product_blueprint(product_controller)
    )

    # Respons error bawaan Flask yang seragam
    @app.errorhandler(404)
    def not_found(error):
        return fail_response(
            "uri",
            "Resource tidak ditemukan",
            404
        )

    @app.errorhandler(405)
    def method_not_allowed(error):
        return fail_response(
            "method",
            "Method HTTP tidak diizinkan untuk resource ini",
            405
        )

    return app
