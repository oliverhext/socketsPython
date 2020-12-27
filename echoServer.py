#!/usr/bin/enc python3

import socket

HOST = "0.0.0.0" # Listen on IP
PORT = "8080" # Port to listen on (1 -65535)
# Creates a socket, the AF_INET is the IPV4 address familiy
# SOCK_STREAM is for TCP (reliable transfer) used to transport the message
# with statement https://www.geeksforgeeks.org/with-statement-in-python/
# Assign socket to object s

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST, PORT) # Assoicate the socket with the IP and PORT
    s.listen() # To accept connection the server listens
    # When a client connects it returns a new socket connection
    # The client IP address
    # We have a new socket opject from accept() and is distinct
    # from the listening port
    conn, addr = s.accept()
    # Using the with statement with conn automatically closes the socket
    # at the end of the block
    
    with conn:
        print("Connected by",addr)
        # Enter infinite loop
        while True:
            # This reads the data the client sends
            data = conn.recv(1024)
            # data in in bytes.  If null breaks
            if not data:
                break
            # Echo the data back using conn.sendall()
            conn.sendall(data)
            