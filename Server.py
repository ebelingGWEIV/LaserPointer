import socket               # Import socket module

class TCPServer:   
   def __init__(self, ip, port):
      self._Socket = socket.socket()
      self._ServerIP = ip
      self._Port = port
      self._Socket.bind((self._ServerIP, port))

   def Listen(self):
      self._Socket.listen(50)                 # Now wait for _Client connection.
      while True:
         self._Client, self.TCPAddress = self._Socket.accept()
         print('Connection from', self.TCPAddress)
         msg = "Hello from camera server"
         self.Send(msg)
      self._Socket.close

   def Send(self, msg):
      sendable = msg.encode()
      self._Client.send(sendable)

   def __del__ (self):
      self._Socket.close()

if __name__ == "__main__":
   myServer = TCPServer(socket._LOCALHOST, 5034)
   myServer.Listen()
   input("Press Enter to continnue...")
   pass
