import socket
from hashlib import sha256

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
MAXSIZE = (1024*1024*1024) #GB
FORMAT = "utf-8"
SALT = "437982"
SECRET = "war" #You can set any secret you want
SALTED = SECRET+SALT
HASHEDSECRET = sha256(SALTED.encode())