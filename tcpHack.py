import socket

target_host = "142.93.53.141"
target_port = 80

# crear un objeto socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conectar el cliente

client.connect((target_host,target_port))

# envía algunos datos

client.send(b"GET / HTTP/1.1\r\nHost: dakybot.com\r\n\r\n")

# tomar algunos datos

response = client.recv(4096)

print(response.decode())
client.close()

"""Primero creamos un objeto socket con los parámetros AF_INET y SOCK_STREAM . 
El parámetro AF_INET indica que utilizaremos una dirección IPv4 estándar o un nombre de red, 
mientras que SOCK_STREAM indica que el cliente utilizará TCP. 
A continuación nos conectamos al servidor y le enviamos unos datos en bytes. 
El último paso es recibir y emitir una respuesta, tras lo cual se puede cerrar el socket."""


