#cliente emisor
import socket

host = ' 10.2.61.118'
port = 3333

#socket
sk = socket.socket()

sk.connect((host,port))
print("Conectado al servidor")

while True:
    #entrada de datos
    mens = input("> ")
    
    #enviamos al servidor el menasje
    sk.send(mens.encode())
    
    if mens == "/exit":
        break

sk.close()
print("Conexión cerrada")
