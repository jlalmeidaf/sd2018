from Client import Client
import rpyc
# from Server import Server

# servidor = Server()

conn = rpyc.connect("localhost", 18861)

client1 = Client("1",conn)
# client2 = Client("2",conn)
client3 = Client("3",conn)

client1.enviar_msg("2","Ola")

# client2.get_msgs_from_servidor()