#cliente receptor
import socket

host = ' 10.2.61.118'
port = 3333

#socket
sk = socket.socket()

sk.connect((host,port))
print("Conectado al servidor")

while True:
    recibido = sk.recv(1024)
    print(recibido.decode())
    
    if recibido.decode() == "/exit":
        break

sk.close()
print("Conexión cerrada")
