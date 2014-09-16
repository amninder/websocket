import sys
from twisted.web.wsgi import WSGIResource
from twisted.internet import reactor, protocol
from twisted.web.server import Site
from twisted.python import log
from twisted.web.static import File
from twisted.application import service
from twisted.application.internet import TCPServer


from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS
from broadcast.broadcast import BroadcastServerProtocol, BroadcastServerFactory


initialized = True
fixtures = ()



if len(sys.argv) > 1 and sys.argv[1] == 'debug':
    log.startLogging(sys.stdout)
    debug = True
else:
    debug = False
ServerFactory = BroadcastServerFactory
factory = ServerFactory("ws://localhost:5000",
                            debug = debug,
                            debugCodePaths = debug)
factory.protocol = BroadcastServerProtocol
factory.setProtocolOptions(allowHixie76 = True)
listenWS(factory)

webdir = File(".")
web = Site(webdir)

if __name__ == "__main__":
    reactor.listenTCP(8000, web)
    reactor.run()
else:
    application = service.Application("charserver")
    TCPServer(8000, web).setServiceParent(application)
