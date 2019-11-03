from opening_hours.handlers.util.decorators import view_validator

__doc__ = """ Declaration of base handlers and sub handlers """

from typing import Any, Dict, List, Union

from aiohttp import web

SUCCESS_CODE: int = 200
ERROR_CODE: int = 400


class Handler:
    """
    Base Generic Handler with common status codes.
    """
    async def get(self, request):
        pass

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass

    async def json_response(
            self,
            results: Dict[
                "str", Union[bool, int, str, List[Any]]
            ],
            status: int = SUCCESS_CODE
    ):
        """
        Prepares a JSON response for give data
        :param results:
        :param status:
        :return:
        """
        return web.json_response(data=results, status=status)


class Ping(Handler):
    """
    Keep alive check handler
    """
    async def get(self, request):
        """
        End point to return pong for client for a ping
        :param request:
        :return: Dict[str: str]:
        """
        return await self.json_response(
            results={"ping": "pong"}, status=SUCCESS_CODE
        )


class OpeningHours(Handler):
    """
    Opening hours handler
    Accepts opening hours as a json array
    Returns json array in readable format
    """

    async def put(self, request_args):
        pass

    async def delete(self, request_args):
        pass

    async def get(self, request):
        return await self.json_response(
            results={"opening_hours": "GET to be implemented."}, status=SUCCESS_CODE
        )

    @view_validator(schema_name="opening_hours_get_schema")
    async def post(self, request_args):

        data = request_args

        for key in data:
            p = data[key]

        return await self.json_response(
            results={"opening_hours": "pong"}, status=SUCCESS_CODE
        )

