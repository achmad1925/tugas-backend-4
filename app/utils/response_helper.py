from flask import jsonify


ERROR_LABELS = {
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    409: "Conflict",
    500: "Internal Server Error"
}


def success_response(data=None, message="Berhasil", status_code=200):
    body = {
        "success": True,
        "message": message
    }

    if data is not None:
        body["data"] = data

    return jsonify(body), status_code


def fail_response(field, reason, status_code=400, error=None):
    body = {
        "success": False,
        "error": error or ERROR_LABELS.get(status_code, "Error"),
        "field": field,
        "message": reason
    }

    return jsonify(body), status_code
