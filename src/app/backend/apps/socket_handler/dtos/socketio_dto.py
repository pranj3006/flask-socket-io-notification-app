"""
DTOs for SocketIo
"""
from flask_restx import Namespace, fields

class SocketIoDto:
    """
    SocketIo DTO Definition
    """

    api_ns = Namespace("socketio",description="SocketIo APIs")
    resp_create_channel_api = api_ns.model(
        "Create Channe API",
        {
            "status": fields.Integer,
            "message": fields.String,
            "data": fields.String,
            "error_code": fields.Integer,
            "error_details": fields.String,
        }
    )

    
    api_success_response_code = 200
    create_channel_api_success_response_message = "Channel Created"

    api_fail_response_code = 503
    create_channel_api_fail_response_message = "Failed"
