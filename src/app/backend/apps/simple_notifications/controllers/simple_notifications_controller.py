"""
Controller for Simple Notification APIs
"""
from flask import request
from apps.simple_notifications.dtos import SimpleNotificationsDto
from apps.core.utils import BaseResponseHandler
from flask_restx import Resource
from flask import render_template,make_response
from apps.simple_notifications.socket_handler import serv_socketio_handler

api_ns = SimpleNotificationsDto.api_ns
responseHandler = BaseResponseHandler()

@api_ns.route("/home")
class HomeController(Resource):
    """
    Controller to Render Home Page
    """    
    def __init__(self,api)-> None:
        super().__init__(self,api)
    
    def get(self):
        """
        Render the home page of simple notification example,
        """        
        headers = {'Content-Type': 'text/html'}
        html_content = render_template('simple_notifications_templates/index.html')
        return make_response(html_content,200,headers)

@api_ns.route("/send_notification")
class SendNotificationController(Resource):
    """
    Controller to Send Notification
    """    
    def __init__(self,api)-> None:
        super().__init__(self,api)

    @api_ns.doc(validate=False)
    @api_ns.expect()
    @api_ns.response(
        SimpleNotificationsDto.api_success_response_code,
        SimpleNotificationsDto.send_notification_api_success_response_message,
        SimpleNotificationsDto.resp_create_channel_api,
    )
    @api_ns.response(
        SimpleNotificationsDto.api_fail_response_code,
        SimpleNotificationsDto.send_notification_api_fail_response_message,
        SimpleNotificationsDto.resp_create_channel_api,
    )
    def post(self):
        """
        API To Send a Notification to all user connected to system channel
        """
        
        data = request.get_json()        
        serv_socketio_handler.send_notification(data)        
        return {'message': 'Message Sent'}, 200
    
    