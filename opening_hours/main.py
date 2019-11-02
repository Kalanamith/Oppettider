from aiohttp import web
from aiohttp.abc import Application

from opening_hours.helpers.url_helpers import add_routes, add_cors


def create_app() -> Application:
    """
    Constructs the aiohttp application
    :return:
    """
    app = web.Application()

    # Add routes
    add_routes(app)

    # Add cors
    add_cors(app)

    return app
