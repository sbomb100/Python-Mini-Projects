import socket
import threading
import ssl 

# Simple TCP tunnel between client and target server
def handle_client(client_socket, target_host, target_port):
    # Connect to the target server
    target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    target_socket.connect((target_host, target_port))

    # Relay data between client and target
    def forward(source, destination):
        while True:
            data = source.recv(4096)
            if not data:
                print("we broke\n")
                break
            destination.send(data)

    # Create threads for bidirectional data transfer
    print("making bidirectional threads: \n")
    threading.Thread(target=forward, args=(client_socket, target_socket)).start()
    threading.Thread(target=forward, args=(target_socket, client_socket)).start()

def vpn():
    # Listening for incoming connections
    #AF_INET is the address family for socket
    #SOCK_STREAM is socket type for bidirecional comms
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 8080))  # Listen on port 8080
    server.listen(5)
    print("Server listening on port 8080...")

    while True:
        try:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}")
        # Forward packets to a target server (example: google.com:80)
            handle_client(client_socket, "google.com", 80)
        except KeyboardInterrupt:
        # This allows the server to exit gracefully when you press Ctrl+C
            signal_handler(None, None)


def sslvpn():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8443))
    server_socket.listen(5)
    print("SSL-enabled server listening on port 8443...")

    while True:
        client_socket, addr = server_socket.accept()
        ssl_client_socket = context.wrap_socket(client_socket, server_side=True)
        print(f"Secure connection from {addr}")

        data = ssl_client_socket.recv(1024)
        print("Received data:", data)
        ssl_client_socket.send(b"Hello, secure world!")
        ssl_client_socket.close()

vpn()