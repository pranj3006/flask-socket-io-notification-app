from apps.simple_notifications.controllers import api_ns
from flask import Blueprint
from flask_restx import Api

module_bp = Blueprint("simple_notifications",__name__, template_folder='../templates')


module_api = Api(module_bp,
                title = "Simple Notifications",
                description="Simple Notifications API Documentation",
                doc="/swagger/")

module_api.add_namespace(api_ns)
