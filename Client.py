import socket


HOST = "127.0.0.1"  # Server address
PORT = 5000         # Server port


def start_client():

    try:
    
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
        client_socket.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")

        
        message = "Hello from the client!"
        client_socket.send(message.encode("utf-8"))

        
        response = client_socket.recv(1024).decode("utf-8")
        print(f"Server response: {response}")

    except socket.error as error:
        print(f"Connection error: {error}")

    finally:
        client_socket.close()
        print("Connection closed.")


if __name__ == "__main__":
    start_client()
  
