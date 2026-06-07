
import socket


HOST = "127.0.0.1"  # Localhost
PORT = 5000         # Port number


def start_server():
    
    try:
      
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        
        server_socket.bind((HOST, PORT))

        
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

      
        data = client_socket.recv(1024).decode("utf-8")
        print(f"Received from client: {data}")

        
        response = "Hello from the server!"
        client_socket.send(response.encode("utf-8"))

        
        client_socket.close()
        print("Client connection closed.")

    except socket.error as error:
        print(f"Socket error: {error}")

    finally:
        server_socket.close()
        print("Server shut down.")


if __name__ == "__main__":
    start_server()
