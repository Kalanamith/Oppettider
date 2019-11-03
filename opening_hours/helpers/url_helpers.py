import aiohttp_cors
from aiohttp import web
from aiohttp.web_app import Application

from opening_hours.config import API_VERSION_1, APP_NAME
from opening_hours.handlers.handlers import Ping, OpeningHours

APP_VERSION: str = f"{APP_NAME}/{API_VERSION_1}"


def add_routes(app: Application) -> None:
    """
    Register routes and cors
    :param app: aiohttp app
    """
    ping: Ping = Ping()
    opening_hours: OpeningHours = OpeningHours()

    app.add_routes(
        [
            # GET handlers
            web.get(f"/{APP_VERSION}/", ping.get),
            web.get(f"/{APP_VERSION}/opening_hours", opening_hours.get),
            # POST Handlers
            web.post(f"/{APP_VERSION}/opening_hours", opening_hours.post),
        ]
    )


def add_cors(app) -> None:
    """
    Register CORS
    :param app: aiohttp app
    """

    cors = aiohttp_cors.setup(
        app, defaults={"*": aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*")}
    )

    for route in list(app.router.routes()):
        cors.add(route)
