from Client import Client
# from Server import Server

# servidor = Server()


client1 = Client("1")
client2 = Client("2")
client3 = Client("3")


client1.enviar_msg("2","Ola")

client2.get_msgs_from_servidor()