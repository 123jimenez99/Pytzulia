import socket
import mysql.connector

# Asignamos propiedades al socket
host = "127.0.0.1"
port = 65000

# Creamos el socket
socket = socket.socket()
print("Socket creado correctamente")

# Bindeamos y eschuchamos
socket.bind((host, port))
socket.listen(1)
print ("Esperando conexiones entrantes...")

connection, address = socket.accept()
print("Conexion establecida dese:", address)

while True:
    data = connection.recv(1024)
    print("Algo ha llegado")
    ese