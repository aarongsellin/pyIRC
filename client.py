import socket

class client:
    def __init__(self):
        self.clientSocket = self.setups.SocketSetup()
        self.alias = ""

    # Function for connecting to a server
    def connect(self,alias,host,port):
        try:
            self.clienSocket.connect((host,port))
            self.alias = alias
            return True
        except:
            return False

    # Function for getting data from the server
    def get(self):
        return str(self.clientSocket.recv(1024),"ASCII")

    # Function for sending data to the server, aka relaying the data to all other users
    def send(self,data):
        try:
            self.clientSocket.send(bytes(self.alias + ": " + data,"ASCII"))
            return 1
        except:
            return 0

    # Function for closing the connection to the server
    def close(self):
        try:
            self.clientSocket.close()
            self.clientSocket = self.setups.SocketSetup()
            return 1
        except:
            return 0

    class setups:
        # Function for setting up a socket
        def SocketSetup(self):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            return sock
