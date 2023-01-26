from pygcc.application import Application
from teapot_wars.teaport_wars_app import TeapotWarsApp


def main():
    app = Application(TeapotWarsApp())
    app.run()
