import logging
from flask_socketio import SocketIO, emit
from socketio_def import socketio

class SocketIOHandler:
    def __init__(self, socketio):
        self.socketio = socketio
        self.active_channels = {}
        self.connected_users = {}
        self.register_events()

    def register_events(self):
        self.socketio.on_event('connect', self.handle_connect)
        # self.socketio.on_event('create_channel', self.create_channel)
        # self.socketio.on_event('subscribe_to_channel', self.subscribe_to_channel)
        # self.socketio.on_event('post_on_channel', self.post_on_channel)
        self.socketio.on_event('disconnect', self.handle_disconnect)
        

    def handle_connect(self):
        logging.info('Client connected')
        self.get_channels_list()        
    
    def create_channel(self,dct_data:dict):
        channel_name = dct_data.get("channel_name")
        message = f'Channel - {channel_name} Created'
        logging.info(message)
        self.active_channels[channel_name] = set()
        self.get_channels_list()

    def get_channels_list(self):
        lst_channels = list(self.active_channels.keys())
        self.socketio.emit('update_channels', lst_channels)

    def subscribe_to_channel(self,dct_data:dict):
        channel_name = dct_data.get("channel_name")
        user_id = dct_data.get("user_id")
        message = f'Subscribed to Channel - {channel_name}'
        self.active_channels[channel_name].add(user_id)
        logging.info(message)
        emit('response', {'message': message})

    def post_on_channel(self,dct_data:dict):
        message = f'Post added to Channel - {channel_name}'
        channel_name = dct_data.get("channel_name")
        user_id = dct_data.get("user_id")
        post_message = dct_data.get("post_message")        
        logging.info(message)
        emit('post_received_on_channel', {'user_id':user_id,'post_message':post_message},room=channel_name)

    def unsubscribe_to_channel(self,dct_data:dict):
        channel_name = dct_data.get("channel_name")
        user_id = dct_data.get("user_id")
        logging.info('Client connected')
        emit('response', {'message': 'Connected to server'})

    def handle_disconnect(self,dct_data:dict):        
        user_id = dct_data.get("user_id")
        for channel_name, members in self.active_channels.items():
            if user_id in members:
                members.remove(user_id)                
        logging.info('Client disconnected')


serv_socketio_handler = SocketIOHandler(socketio)