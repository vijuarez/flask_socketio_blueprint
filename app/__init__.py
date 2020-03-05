from gevent import monkey
monkey.patch_all()

from flask import Flask

from .config import config_all, get_socketio

SCKT= get_socketio()


def create_app(debug=False) -> Flask:
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug

    config_all(app, debug)

    from .blueprints import people
    app.register_blueprint(people.PP)
    SCKT.on_event('new_friend', people.new_friend, namespace="/people")

    SCKT.init_app(app)


    return app
