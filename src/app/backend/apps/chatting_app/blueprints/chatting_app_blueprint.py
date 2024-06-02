from apps.chatting_app.controllers import api_ns
from flask import Blueprint
from flask_restx import Api

chatting_app_bp = Blueprint("chatting_app",__name__, template_folder='../templates/')


chatting_app_api = Api(chatting_app_bp,
                title = "Chatting App",
                description="Chatting App API Documentation",
                doc="/swagger/")

chatting_app_api.add_namespace(api_ns)
