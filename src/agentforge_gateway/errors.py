from __future__ import annotations


class GatewayError(Exception):
    status_code = 500
    error_type = "internal_error"

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def to_response(self) -> dict[str, object]:
        return {
            "error": {
                "message": self.message,
                "type": self.error_type,
            }
        }


class BadRequestError(GatewayError):
    status_code = 400
    error_type = "bad_request"


class ModelNotFoundError(GatewayError):
    status_code = 404
    error_type = "model_not_found"

