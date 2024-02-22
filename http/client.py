import socket

def perform_handshake(client_socket):
    # Send WebSocket handshake request
    client_socket.send(b"GET / HTTP/1.1\r\n"
                       b"Host: localhost:8765\r\n"
                       b"Upgrade: websocket\r\n"
                       b"Connection: Upgrade\r\n"
                       b"Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
                       b"Sec-WebSocket-Version: 13\r\n\r\n")

    # Receive WebSocket handshake response
    response = client_socket.recv(4096)
    print(response.decode())
    print("Handshake complete")

def main():
    server_host = 'localhost'
    server_port = 8765

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    # Perform WebSocket handshake
    perform_handshake(client_socket)

    # Proceed with WebSocket communication
    # while True:
    #     pass

    # Close the connection with the server
    print("Connection closed...")
    client_socket.close()

if __name__ == "__main__":
    main()
