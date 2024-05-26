"""
Controller for SocketIO APIs
"""

import logging
from apps.socket_handler.dtos import SocketIoDto
from apps.core.utils import BaseResponseHandler
from flask_restx import Resource
from flask import render_template,render_template_string,make_response

api_ns = SocketIoDto.api_ns
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
        Render the home page of notification syste,
        """
        headers = {'Content-Type': 'text/html'}
        html_content = render_template('index.html')
        return make_response(html_content,200,headers)

@api_ns.route("/createchannel")
class CreateChannelController(Resource):
    """
    Controller to Create Channel
    """    
    def __init__(self,api)-> None:
        super().__init__(self,api)

    @api_ns.doc(validate=False)
    @api_ns.expect()
    @api_ns.response(
        SocketIoDto.api_success_response_code,
        SocketIoDto.create_channel_api_success_response_message,
        SocketIoDto.resp_create_channel_api,
    )
    @api_ns.response(
        SocketIoDto.api_fail_response_code,
        SocketIoDto.create_channel_api_fail_response_message,
        SocketIoDto.resp_create_channel_api,
    )
    def post(self):
        """
        API To Create a Channel
        """
        from apps.socket_handler.controllers.socketio_handler import serv_socketio_handler
        data = api_ns.payload
        channel_name=data.get("channel_name")
        # Emit the create_channel event
        serv_socketio_handler.create_channel({'channel_name': channel_name})
        return {'message': f'Channel {channel_name} creation event emitted'}, 200