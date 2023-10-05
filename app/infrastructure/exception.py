# custom_exceptions.py
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = []
    for error in exc.errors():
        if error["type"] == "value_error.email":
            error_messages.append({"status_code": 422, "detail": "Invalid email address"})
        else:
            error_messages.append({"status_code": 422, "detail": error["msg"]})
    print(error_messages[0])
    return JSONResponse(
        status_code=422,
        content=error_messages[0],
    )