import socket

# Connect to the tunnel server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

# Send some data to the server
client_socket.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

# Receive and print the response from the server (which should be forwarded from google.com)
response = client_socket.recv(4096)
print("Received data:", response)

# Close the connection
client_socket.close()