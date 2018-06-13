import rpyc
conn = rpyc.connect("localhost", 18861)

objetoNoServidor = conn.root


objetoNoServidor.exposed_contarConexoes()

