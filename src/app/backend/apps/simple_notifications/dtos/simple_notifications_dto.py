"""
DTOs for SimpleNotifications
"""
from flask_restx import Namespace, fields

class SimpleNotificationsDto:
    """
    SimpleNotifications DTO Definition
    """

    api_ns = Namespace("simple_notifications",description="Simple Notifications APIs")
    resp_create_channel_api = api_ns.model(
        "Send NotificationAPI",
        {
            "message": fields.String,
            "error_code": fields.Integer,
            "error_details": fields.String,
        }
    )

    
    api_success_response_code = 200
    send_notification_api_success_response_message = "Notification Sent"

    api_fail_response_code = 503
    send_notification_api_fail_response_message = "Failed"
