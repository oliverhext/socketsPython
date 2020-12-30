import socket
import pickle


HEADERSIZE = 10
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    # Set values:  clear full_msg and set new_msg to true
    full_msg = b""
    new_msg = True
    while True:
        # Receive the message in chunkc of 16
        msg = s.recv(16)
        #If new_msg is true print the message
        if new_msg:
            print(f"The message HEADER length is {HEADERSIZE}")
            print(f"NEW message is  {msg}")
            # Keep receiving data based on the message size
            print(f"The mesage length is: {msg[:HEADERSIZE]}")
            
            msglen = int(msg[:HEADERSIZE])
            print(f"The message length is {msglen}")
            new_msg = False
        print(f"START BUILDING MESSAGE  {msg}")    
        full_msg += msg
        if len(full_msg)-HEADERSIZE == msglen:
            print("Full msg received")
            #Print full message minus the HEADER SIZE
            print(full_msg[HEADERSIZE:])
            print("Pickle the object")
            d= pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b""
            
    print(full_msg)