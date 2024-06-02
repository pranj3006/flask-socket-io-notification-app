"""
Controller for Chattting App APIs
"""
from flask import request
from apps.chatting_app.dtos import ChattingAppDto
from apps.core.utils import BaseResponseHandler
from flask_restx import Resource
from flask import render_template,make_response
from apps.chatting_app.socket_handler import serv_socketio_handler

api_ns = ChattingAppDto.api_ns
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
        Render the home page of Chatting App example,
        """        
        headers = {'Content-Type': 'text/html'}
        html_content = render_template('chatting_app_templates/index.html')
        print(html_content)
        return make_response(html_content,200,headers)

@api_ns.route("/add_user")
class AddUserController(Resource):
    """
    Controller to Add User
    """    
    def __init__(self,api)-> None:
        super().__init__(self,api)

    @api_ns.doc(validate=False)
    @api_ns.expect()
    @api_ns.response(
        ChattingAppDto.api_success_response_code,
        ChattingAppDto.add_user_api_success_response_message,
        ChattingAppDto.resp_add_user_api,
    )
    @api_ns.response(
        ChattingAppDto.api_fail_response_code,
        ChattingAppDto.add_user_api_fail_response_message,
        ChattingAppDto.resp_add_user_api,
    )
    def post(self):
        """
        API To Add User
        """
        
        data = request.get_json()
        serv_socketio_handler.add_user(data)        
        return {'message': 'User Added'}, 200
    
    