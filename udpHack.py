import socket

target_host = "127.0.0.1"
target_port = 9090

# crear un objeto socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((target_host, target_port))
# envía algunos datos

client.sendto(b"hola Python",(target_host,target_port))

# tomar algunos datos

data, addr = client.recvfrom(8)

print(data)
client.close()


