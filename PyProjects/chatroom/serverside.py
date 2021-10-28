import socket, time, sys
"""
    NOTES:
        Create better UI Key features are missing
"""


#   Creation of socket
newSocket = socket.socket()

#   Retriving host name and declaring port
hostName = socket.gethostname()
sIP = socket.gethostbyname(hostName)
port = 8080

#   Binding of the host and port
newSocket.bind((hostName, port))
print("<< Binding successful! >>")
print("<< This is your IP: ", sIP + " >>")

name = input('Enter name: ')

#   Connection listener
newSocket.listen(1)

#   Accepting incoming Connections
conn, add = newSocket.accept()
print("<< Received connection from ", add[0] + " >>")
print("<< Connection Established. Connected From: ",add[0] + " >>")

#   The storing of incoming data
client = (conn.recv(1024)).decode() #   Clients name maximum of 1024 bytes
print("<< " + client + "has connected >>")
conn.send(name.endswith())

#   Message delivery
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024) # Message can be of 1024 bytes
    message = message.decode()
    print(client, ':', message)
