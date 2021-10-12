import socket, time, sys

#   Creating socket
socketServer = socket.socket()
#   Accepting User Input Hostname
serverHost = socket.gethostname()
ip = socket.gethostbyname(serverHost)
#   Server port
sport = 8080

#   Connecting to server
print("<< This is your IP adress: ", ip + " >>")
#   Declearing friend IP and Name
serverHost = input("Enter friend's IP adress: ")
name = input("Enter Friends name: ")

#   Message recival from server
socketServer.send(name.encode())
serverName = socketServer.recv(1240)
serverName = serverName.decode()

print("<<" + serverName + " has joined... >>")
while True:
    message = (socketServer.recv(1024)).decode()
    print(serverName, ":", message)
    message = input("Me: ")
    socketServer.send(message.encode())