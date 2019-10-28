import os

import click
from aiohttp import web

from opening_hours import main


@click.command("run", help="Runs the application")
def run():
    """
    Entry point for aiohttp application
    """
    app = main.create_app()
    web.run_app(app=app, port=5000)
    # web.run_app(app=app, port=os.environ["BACK_OFFICE_APP_PORT"])