#Adapted From: https://github.com/nikhilroxtomar/File-Transfer-using-TCP-Socket-in-Python3
from serverConfig import *

def main():
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        """ Server has accepted the connection from the client. """
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected. Waiting for Secret....")

        providedSecret = conn.recv(SIZE).decode(FORMAT) + SALT
        hashedProvidedSecret = sha256(providedSecret.encode())

        if hashedProvidedSecret.hexdigest() == HASHEDSECRET.hexdigest():
            conn.send("Secret Verified".encode(FORMAT))
            """ Receiving the filename from the client. """
            filename = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving the filename.")
            file = open(f'/Users/farhanishraq/Downloads/Summer 2022/Summer-Projects/fileTransfers/recv/{filename}', "wb")
            conn.send("Filename received.".encode(FORMAT))

            """ Receiving the file data from the client. """
            #data = conn.recv(SIZE).decode(FORMAT)
            bytes_read = 0
            #capable of transfering 1GB of data
            while bytes_read<MAXSIZE:
                data = conn.recv(SIZE)
                #if there's no more data, simply exit
                if len(data)==0:
                    break
                print(f"[RECV] Receiving the file data.")
                file.write(data)
                bytes_read += len(data)
                conn.send(f"File data received {bytes_read} bytes".encode(FORMAT))
            """ Closing the file. """
            file.close()

            """ Closing the connection from the client. """
            conn.close()
            print(f"[DISCONNECTED] {addr} disconnected.")
        else:
            conn.send("Secret Not Valid. Closing Connection...".encode(FORMAT))
            conn.close()
            print(f"[DISCONNECTED] {addr} disconnected. Verification Failed")

if __name__ == "__main__":
    main()