import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS







class BroadcastServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.factory.register(self)

    def onMessage(self, payload, isBinary):
        if not isBinary:
            # msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            msg = "{}".format(payload.decode('utf8'))
            self.factory.broadcast(msg)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)


class BroadcastServerFactory(WebSocketServerFactory):
    """
        Broadcast message to all clients
    """
    def __init__(self, url, debug = False, debugCodePaths = False):
        WebSocketServerFactory.__init__(self, url, debug=debug, debugCodePaths = debugCodePaths)
        self.clients = []
        self.tickcount = 0
        self.tick()

    def tick(self):
        self.tickcount += 1
        self.broadcast("tick %d from server" % self.tickcount)
        # reactor.callLater(1, self.tick)

    def register(self, client):
        if not client in self.clients:
            print("registered client: {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregisterd client: {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("{}".format(msg))
        for c in self.clients:
            c.sendMessage(msg.encode('utf8'))
            print("message sent to {}".format(c.peer))
