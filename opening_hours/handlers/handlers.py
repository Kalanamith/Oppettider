__doc__ = """ Declaration of base handlers and sub handlers """

from typing import Any, Dict, List, Union

from aiohttp import web


class Handler:

    SUCCESS_CODE: int = 200
    ERROR_CODE: int = 400

    async def get(self, request):
        pass

    async def post(self, request):
        pass

    async def put(self, request):
        pass

    async def delete(self, request):
        pass

    @staticmethod
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


class OpeningHours(Handler):
    """
    Opening hours handler
    Accepts opening hours as a json array
    Returns json array in readable format
    """

    async def put(self, request):
        pass

    async def delete(self, request):
        pass

    async def get(self, request):
        pass

    async def post(self, request):
        pass
