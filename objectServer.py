# Sending and receiving objects using the pickle module
# concerts to bytes
import socket
import time
import pickle

HEADERSIZE = 10
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    d = {1: "An", 2: "Object"} # A dictionary
    print("The object is of type:",type(d))
    msg = pickle.dumps(d)
    print(msg)
    
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    clientsocket.send(bytes(msg))

