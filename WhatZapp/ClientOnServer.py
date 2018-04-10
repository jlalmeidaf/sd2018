class ClientOnServer(object):
	"""docstring for ClientOnServer"""
	def __init__(self, client):
		super(ClientOnServer, self).__init__()
		self.client = client
		self.msg = []
	def recv_msg(self,remetente, msg):
		self.msg.append([remetente, msg])
		