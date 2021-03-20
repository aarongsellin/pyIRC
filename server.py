import socket, multiprocessing, requests

# Function for starting and initating the server
def Setup(port=6667):
	ServerObj = server(port)
	return ServerObj

# Client class on the sever side
class client:
	def __init__(self,ServerObj,conn,addr):
		self.ServerObj = ServerObj
		self.conn = conn
		self.addr = addr

	# Client thread
	def ClientThread(self):
		while True:
			try:
				data = self.conn.recv(1024)
			except:
				break

			if not data:
				break

			# Relay data to all connected users
			for client in self.ServerObj.clients:
				client.conn.send(data)

		# Remove client
		print("{} Disconnected".format(addr[0]))
		self.ServerObj.clients.remove(self)

# Server class
class server:
	def __init__(self,port):
		self.clients = []
		# Server adress
		self.port = port
		self.ip = requests.get("https://ipv4bot.whatismyipaddress.com").text
		# Setup server socket
		self.serverSock = self.setups.setupSocket()
		self.ListenerThread = None

	# Function for starting the listener thread
	def StartListener(self):
		try:
			self.ListenerThread = multiprocessing.Process(target=server.Listener,args=self).start()
			return True
		except:
			return False

	# Listener thread
	def Listener(self):
		# Start listening for client connections
		self.serverSock.listen(5)
		while True:
			# Accept client connections
			conn, addr = self.serverSock.accept()
			# Start a thread for the client
			ClientObj = client(conn,addr)
			multiprocessing.Process(target=ClientObj.ClientThread,args=ClientObj).start()
			self.clients.append(ClientObj)

	# Function for stopping the listener thread
	def StopListener(self):
		self.ListenerThread.shutdown()

	class setups:
		# Function for setting up the server socket
		def setupSocket(self):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(10)
			sock.bind(("",port))
			return sock
