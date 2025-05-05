import socket
import os

HOST = 'localhost'  
PORT = 5001
BUFFER_SIZE = 4096  # 4KB buffer


def main():


    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5) 
    print("Hey Client!\n")
    print(f"Listening on {HOST}:{PORT}")


    while True:

        client_socket, addr = server_socket.accept()
        print(f"{addr} connected.")

        # Receive filename length first
        filename_length = int.from_bytes(client_socket.recv(4), 'big')
        filename = client_socket.recv(filename_length).decode()
        print(f"Receiving file: {filename}")

        # Receive file size
        filesize = int.from_bytes(client_socket.recv(8), 'big')
        print(f"File size: {filesize} bytes")


        with open(f"received_{filename}", "wb") as f:
            bytes_read = 0
            while bytes_read < filesize:
                data = client_socket.recv(min(BUFFER_SIZE, filesize - bytes_read))
                if not data:
                    break
                f.write(data)
                bytes_read += len(data)



        print(f"File {filename} received successfully.")
        client_socket.close()



if __name__ == "__main__":
    main()
