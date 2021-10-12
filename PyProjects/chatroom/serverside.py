import socket
import select
import sys
from threading import *

#   AF_INET is the address domain of the socket
#   SOCK_STREAM allow us to pass charckters in a continous flow
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.(socket.SOL_SOCKET, socket.SO_REUSEADDR)

#   Checks if sufficint arguments have been provied
if len(sys.argv) != 3:
    print("*Correct usage: script, IP adress, port number*")
    exit()

IPAdress = str(sys.argv[1])

Port = int(sys.argv[2])