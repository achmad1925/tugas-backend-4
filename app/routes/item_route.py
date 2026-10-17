from flask import Blueprint


def create_item_blueprint(controller):
    item_bp = Blueprint("items", __name__)

    item_bp.add_url_rule(
        "/api/v1/items",
        view_func=controller.get_all,
        methods=["GET"]
    )

    item_bp.add_url_rule(
        "/api/v1/items",
        view_func=controller.create,
        methods=["POST"]
    )

    item_bp.add_url_rule(
        "/api/v1/items/<int:item_id>",
        view_func=controller.get_by_id,
        methods=["GET"]
    )

    item_bp.add_url_rule(
        "/api/v1/items/<int:item_id>",
        view_func=controller.update,
        methods=["PUT"]
    )

    item_bp.add_url_rule(
        "/api/v1/items/<int:item_id>",
        view_func=controller.delete,
        methods=["DELETE"]
    )

    return item_bp
