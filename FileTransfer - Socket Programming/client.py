import socket
import os

SERVER_HOST = 'localhost'  
SERVER_PORT = 5001
BUFFER_SIZE = 4096


def main():

    filename = input("Enter filename to send: ")
    if not os.path.exists(filename):
        print("File not found.")
        return

    filesize = os.path.getsize(filename)


    try:
        client_socket = socket.socket()
        client_socket.connect((SERVER_HOST, SERVER_PORT))
    except socket.error as e:
        print(f"Cannot connect to server: {e}")
        return


    # First Send filename length and filename
    filename_bytes = filename.encode()
    client_socket.send(len(filename_bytes).to_bytes(4, 'big'))
    client_socket.send(filename_bytes)

    # Then Send filesize
    client_socket.send(filesize.to_bytes(8, 'big'))


    # Send file data
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)



    print(f"File {filename} sent successfully.")
    client_socket.close()



if __name__ == "__main__":
    main()
