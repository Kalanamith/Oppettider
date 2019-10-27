import functools
from json import JSONDecodeError

from aiohttp import web
from cerberus import DocumentError, Validator

from opening_hours.handlers.util.validator_schema import ValidationSchema


def view_validator(schema_name: str):
    """
    Validates post parameters
    :param schema_name:
    """

    def wrapper(function):
        @functools.wraps(function)
        async def wrapped(handler, request):
            request_args = {}

            if request.method == "POST" or request.method == "PUT":

                try:
                    request_args = await request.json()
                except JSONDecodeError as e:
                    return web.json_response(data={"Error": "JSON error"}, status=400)

            elif request.method == "DELETE":
                request_args = {"id": request.match_info["id"]}

            elif request.method == "GET":
                request_args = dict(request.query)

            schema = ValidationSchema.get_schema(schema_name)

            try:
                validator_schema = Validator(schema())
                if not validator_schema.validate(request_args):

                    error_message: str = ""
                    for key, value in validator_schema.errors.items():
                        error_message += f"{key} : {value}  Error"

                    return web.json_response(data={"Error": "Field validation failure"}, status=400)

            except DocumentError as e:
                return web.json_response(data={"Error": "Invalid JSON"}, status=400)

            return await function(handler, request_args)

        return wrapped

    return wrapper
