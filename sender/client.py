#Adapted From: https://github.com/nikhilroxtomar/File-Transfer-using-TCP-Socket-in-Python3
import socket
from hashlib import sha256
from clientFunctions import *

#if you are sending file over local host, use the below config
IP = socket.gethostbyname(socket.gethostname())
#if you are transfering file from one computer to another, get the IP address of the server
#IP = "" #paste the IP within paratheses, and uncoment the line
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024*1024

def main():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    """ Send Secret """
    whatIsSecret = input("Please enter the secret: ")
    client.send(whatIsSecret.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Opening and reading the file data. """
    path,filename = getFileForTransfer()
    file = open(path, "rb")
    data = file.read(SIZE)

    """ Sending the filename to the server. """
    client.send(filename.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Sending the file data to the server. """
    #client.send(data.encode(FORMAT))
    client.sendall(data)
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the file. """
    file.close()

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()