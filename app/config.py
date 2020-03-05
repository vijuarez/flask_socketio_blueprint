from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO
import os

load_dotenv('.env')


def get_socketio() -> SocketIO:
    # Returns an unitialized SocketIO client
    return SocketIO(message_queue=os.environ.get('REDIS_URL'), async_mode='gevent', engineio_logger=True)


def config_all(app: Flask, debug=False):
    # Add configuration and keys to the app
    app.config['REDIS_URL'] = os.environ.get('REDIS_URL')