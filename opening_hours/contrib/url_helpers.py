import aiohttp_cors
from aiohttp import web
from aiohttp.web_app import Application

from opening_hours.config import API_VERSION_1
from opening_hours.handlers.handlers import Ping, OpeningHours


def add_routes(app: Application) -> None:
    """
    Register routes and cors
    :param app: aiohttp app
    """
    ping: Ping = Ping()
    opening_hours: OpeningHours = OpeningHours()

    app.add_routes(
        [
            web.get(f"/{API_VERSION_1}/", ping.get),
            web.get(f"/{API_VERSION_1}/opening_hours", opening_hours.get),
            web.get(f"/{API_VERSION_1}/opening_hours", opening_hours.post),
        ]
    )


def add_cors(app) -> None:
    """
    Register CORS
    :param app: aiohttp app
    """

    cors = aiohttp_cors.setup(
        app, defaults={
            "*": aiohttp_cors.ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*"
            )
        }
    )

    for route in list(app.router.routes()):
        cors.add(route)
