import socket			

# el objeto de la función socket se va a llamar 's'
socket = socket.socket()		
print ("Socket successfully created")

# Vamos a utilizar el puerto 65000
port = 65000			

# Con la funcion bind, bindearemos el puerto de escucha
socket.bind(('', port))		
print ("socket binded to %s" %(port))

# Ponemos el socket en modo 'listening'
socket.listen()	
print ("socket is listening")		

# Creamos un bucle infinito para que no pare hasta que se lo ordenemos
while True:

# Establecemos una conexión con el 
    c, addr = socket.accept()	
print ('Got connection from', addr )

# Cerramos la conexion con el cliente
c.close()