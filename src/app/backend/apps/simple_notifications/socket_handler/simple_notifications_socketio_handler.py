import logging
from socketio_def import socketio

class SocketIOHandler:
    def __init__(self, socketio):
        self.socketio = socketio
        self.register_events()

    def register_events(self):
        self.socketio.on_event('connect', self.handle_connect)
        self.socketio.on_event('disconnect', self.handle_disconnect)

    def handle_connect(self):
        logging.info('Client connected')        

    def send_notification(self,dct_data:dict):
        message_text = dct_data.get("message")
        logging.info('Message Sent to All Connected Users')
        self.socketio.emit('system_notifications', {"message":message_text})
    
    def handle_disconnect(self):        
        logging.info('Client disconnected')


serv_socketio_handler = SocketIOHandler(socketio)