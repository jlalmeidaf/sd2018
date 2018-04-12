from ClientOnServer import ClientOnServer
import rpyc
class Server(rpyc.Service):
	list_of_clients = [] 
	"""docstring for Server"""
	def __init__(self,args):
		super(Server, self).__init__(args)
		# self.list_of_clients = [] #lista vazia
		
	

	def exposed_enviar_mensagem(self,remetente, client, msg):
		for eachObject in Server.list_of_clients: 
			if eachObject.client == client:
				eachObject.recv_msg(remetente,msg)

	def exposed_recv_msg(self,nome):
	 	for eachObject in Server.list_of_clients: 
			if eachObject.client == nome:
				msg = eachObject.msg
				return msg
				# client.recv_msg(msg)


	def exposed_add(self, client):
		obj_Client = ClientOnServer(client)
		Server.list_of_clients.append(obj_Client)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(Server, port=18861)
    t.start()