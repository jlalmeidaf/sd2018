from Client import Client
import rpyc


conn = rpyc.connect("localhost", 18861)
client2 = Client("2",conn)
client2.get_msgs_from_servidor()