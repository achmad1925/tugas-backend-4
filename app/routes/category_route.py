from flask import Blueprint


def create_category_blueprint(controller):
    category_bp = Blueprint("categories", __name__)

    category_bp.add_url_rule(
        "/api/v1/categories",
        view_func=controller.get_all,
        methods=["GET"]
    )

    category_bp.add_url_rule(
        "/api/v1/categories",
        view_func=controller.create,
        methods=["POST"]
    )

    category_bp.add_url_rule(
        "/api/v1/categories/<int:category_id>",
        view_func=controller.get_by_id,
        methods=["GET"]
    )

    category_bp.add_url_rule(
        "/api/v1/categories/<int:category_id>",
        view_func=controller.update,
        methods=["PUT"]
    )

    category_bp.add_url_rule(
        "/api/v1/categories/<int:category_id>",
        view_func=controller.delete,
        methods=["DELETE"]
    )

    return category_bp
