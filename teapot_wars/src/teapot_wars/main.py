import logging

from pygcc.application import Application
from teapot_wars.teaport_wars_app import TeapotWarsApp

logging.basicConfig(level=logging.DEBUG)


def main():
    app = Application(TeapotWarsApp())
    app.run()
