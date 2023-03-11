import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print ("Socket creado correctamente")
except socket.error as err:
	print ("Creacion del Socket fallida %s" %(err))

# El puerto por defecto que utilizaremos para conectarnos
port = 65000

try:
	host_ip = socket.gethostbyname('127.0.0.1')
except socket.gaierror:

	# this means could not resolve the host
	print ("No se ha podido resolver el host")
	sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("El Socket se ha conectado correctamente a:",host_ip,"usando el puerto",port)