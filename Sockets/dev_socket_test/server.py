import socket

# Asigna las propiedades del Socket
host = "127.0.0.1"
port = 65000

# Crea el Socket
socket = socket.socket()
print("Socket creado correctamente")

# Bindea las propiedades y empieza a eschuchar
socket.bind((host, port))
socket.listen(1)
print ("Esperando conexiones entrantes...")

connection, address = socket.accept()
print("Conexion establecida dese:", address)

while True:
    data = connection.recv(512)
    if data:
        print(data.decode())
    else:
        print ("La conexión se ha cortado")
        break