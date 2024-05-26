from apps.socket_handler.controllers import api_ns
from flask import Blueprint
from flask_restx import Api

socketio_bp = Blueprint("socketio",__name__, template_folder='../templates')


socketio_api = Api(socketio_bp,
                      title = "SocketIO",
                      description="SocketIO API Documentation",
                      doc="/swagger/")

socketio_api.add_namespace(api_ns)

    