import sockjs.tornado
import json, unicodedata

class EchoSockjsConnection(sockjs.tornado.SockJSConnection):
  clients = set()

  def send_error(self, message, error_type=None):
    """
      Standard format for all errors
    """
    return self.send(json.dumps({
      'data_type': 'error' if not error_type else '%s_error'% error_type,
      'data': {
        'message': message
      }
    }))

  def send_message(self, message, data_type=None):
    """
      Standard format of all messages
    """
    return self.send(json.dumps({
      "data_type":  data_type,
      "data":       message
    }))

  def on_open(self, request):
    print "sockjs: open"
    self.send("Connection Opened")

  def on_message(self, data):
    print "%s" %(unicodedata.normalize("NFKD", data).encode("ascii", "ignore"))
    self.send(data)

  def on_close(self):
    print "sockjs: close"

def EchoSockjsRouter(prefix):
  return sockjs.tornado.SockJSRouter(EchoSockjsConnection, prefix).urls
  
