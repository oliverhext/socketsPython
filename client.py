import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

msg = s.recv(1024) # Stream of data chucks of dat 1024 bytes
print(msg.decode("utf-8")) # Received as bytes stream decode to utf text