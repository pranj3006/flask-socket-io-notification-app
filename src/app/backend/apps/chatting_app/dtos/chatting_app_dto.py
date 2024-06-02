"""
DTOs for ChattingApp
"""
from flask_restx import Namespace, fields

class ChattingAppDto:
    """
    ChattingApp DTO Definition
    """

    api_ns = Namespace("chatting_app",description="Chatting App APIs")
    resp_add_user_api = api_ns.model(
        "Add User",
        {
            "message": fields.String,
            "error_code": fields.Integer,
            "error_details": fields.String,
        }
    )
    
    api_success_response_code = 200
    add_user_api_success_response_message = "User Added"

    api_fail_response_code = 503
    add_user_api_fail_response_message = "Failed"
