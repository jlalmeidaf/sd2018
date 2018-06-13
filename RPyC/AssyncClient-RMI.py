import rpyc
c = rpyc.connect("localhost", 18861)
print 'Para sair use CTRL+X\n'
msg = raw_input()


async_send_msg = rpyc.async(c.root.send_msg)
async_send_msg(msg)

