import sys

from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS



class BroadcastClientProtocol(WebSocketClientProtocol):

    def sendHello(self):
        self.sendMessage("Hello from Python!".encode('utf8'))

    def onOpen(self):
        self.sendHello()

    def onMessage(self, payload, isBinary):
        if not isBinary:
            print("Text message received: {}".format(payload.decode('utf8')))
