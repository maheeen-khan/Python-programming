import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

SERVER_HOST = 'localhost'  
SERVER_PORT = 5002


def main():

    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, output=True, frames_per_buffer=CHUNK)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Connected to audio server at {SERVER_HOST}:{SERVER_PORT}")
    except Exception as e:
        print(f"Cannot connect: {e}")
        return


    try:
        while True:
            data = client_socket.recv(CHUNK)
            if not data:
                break
            stream.write(data)
    except KeyboardInterrupt:
        print("\nStopping audio client.")
    finally:
        client_socket.close()
        stream.stop_stream()
        stream.close()
        audio.terminate()



if __name__ == "__main__":
    main()
