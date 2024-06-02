import logging
from socketio_def import socketio

class SocketIOHandler:
    def __init__(self, socketio):
        self.socketio = socketio
        self.connected_users = []
        self.register_events()

    def register_events(self):
        self.socketio.on_event('connect', self.handle_connect)
        self.socketio.on_event('disconnect', self.handle_disconnect)

    def handle_connect(self):
        logging.info('Client connected')

    def add_user(self,dct_data:dict):
        username = dct_data.get("username")        
        self.connected_users.append(username)
        logging.info('Username Added')
        self.socketio.emit('connected_users_list', self.connected_users)
    
    def handle_disconnect(self):
        logging.info('Client disconnected')


serv_socketio_handler = SocketIOHandler(socketio)