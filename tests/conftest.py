import pytest
from aiohttp import web

from opening_hours.helpers.url_helpers import add_routes, add_cors


@pytest.fixture
def oh_client(loop, aiohttp_client):
    """
    Creates a test app for the project
    """
    app = web.Application()

    add_routes(app)
    add_cors(app)

    return loop.run_until_complete(aiohttp_client(app))
