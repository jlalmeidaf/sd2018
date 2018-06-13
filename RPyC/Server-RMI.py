import rpyc
from time import sleep
class MyService(rpyc.Service):
    def __init__(self,args):
        super(MyService, self).__init__(args)
        self.acumulador = 0

    # def exposed_send_msg(self, msg):
    #     print msg

    def exposed_contarConexoes(self):
        self.acumulador = self.acumulador + 1
        print self.acumulador
        


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()



        