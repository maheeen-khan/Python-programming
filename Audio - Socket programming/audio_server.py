import socket
import pyaudio

CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  

HOST = 'localhost'
PORT = 5002  


def main():


    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True, frames_per_buffer=CHUNK)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)


    print(f"Audio server listening on {HOST}:{PORT}...")
    client_socket, addr = server_socket.accept()
    print(f"Client {addr} connected for audio.")


    try:
        while True:
            data = stream.read(CHUNK)
            client_socket.sendall(data)
    except KeyboardInterrupt:
        print("\nStopping audio server.")
    finally:
        client_socket.close()
        stream.stop_stream()
        stream.close()
        audio.terminate()



if __name__ == "__main__":
    main()
