#Buffer and streaming data.  What happen when we exceed the buffer size 
# and keep the stream open
import socket 
import time

HEADERSIZE = 10

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")
    
    msg = "AAAAABBBBBCCCCCDDDDDEEEEEFFFFFGGGGGHHHHHIIIIIJJJJJKKKKKLLLLL"
    msg = f"{len(msg):<{HEADERSIZE}}"+msg  
    
    clientsocket.send(bytes(msg, "utf-8"))
    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f"{len(msg):{HEADERSIZE}}"+msg         
        clientsocket.send(bytes(msg, "utf-8"))
        
   