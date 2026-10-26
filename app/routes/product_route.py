from flask import Blueprint


def create_product_blueprint(controller):
    product_bp = Blueprint("products", __name__)

    product_bp.add_url_rule(
        "/api/v1/products",
        view_func=controller.get_all,
        methods=["GET"]
    )

    product_bp.add_url_rule(
        "/api/v1/products",
        view_func=controller.create,
        methods=["POST"]
    )

    product_bp.add_url_rule(
        "/api/v1/products/<int:product_id>",
        view_func=controller.get_by_id,
        methods=["GET"]
    )

    product_bp.add_url_rule(
        "/api/v1/products/<int:product_id>",
        view_func=controller.update,
        methods=["PUT"]
    )

    product_bp.add_url_rule(
        "/api/v1/products/<int:product_id>",
        view_func=controller.delete,
        methods=["DELETE"]
    )

    return product_bp
