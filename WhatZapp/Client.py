import rpyc
class Client(object):
	"""docstring for Client"""
	def __init__(self, nome):
		super(Client, self).__init__()
		self.nome = nome
		conn = rpyc.connect("localhost", 18861)
		self.servidor = conn.root
		self.servidor.add(self.nome)

		
	def enviar_msg(self,dest_name,msg):
		print self.nome + " " + msg
		# client.recv_msg(msg)
		self.servidor.enviar_mensagem(self.nome,dest_name,msg)

	def get_msgs_from_servidor(self):
		msg = self.servidor.recv_msg(self.nome)
		self.recv_msg(msg)

	def recv_msg(self,msg):
		for eachMsg in msg:
			print self.nome + " - " + eachMsg[0] +" : " + eachMsg[1]
		