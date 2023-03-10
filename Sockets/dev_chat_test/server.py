import socket
from threading import *

# Establecemos los parametros del socket (host y puerto)
server_socket = socket.socket()
host = "localhost"
port = 65000

# Asignamos las propiedades del socket al socket
server_socket.bind((host, port))

# Creamos un hilo con las propiedades del socket

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

# Comprueba continuamente si ha recibido algo por parte del cliente
    def run(self):
        while 1:
            print('Cliente:', self.sock.recv(1024).decode())
            self.sock.send(b'')


# Lo ponemos a escuchar
server_socket.listen()
print('server started and listening')
while 1:
    clientsocket, address = server_socket.accept()
    client(clientsocket, address)
