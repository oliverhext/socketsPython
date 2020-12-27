# Sockets in Python 3

Python’s socket module provides an interface to the Berkeley sockets API. This is the module that we’ll use and discuss in this tutorial.

The primary socket API functions and methods in this module are:

socket()
bind()
listen()
accept()
connect()
connect_ex()
send()
recv()
close()

![TCP Connection](tcpCapture.PNG)

We look at a simple socket example using server.py and client.py.  The wireshark screen shot shows the initial TCP connection
being setup then the message sent.  The server PORT of 1234 and client PORT 25946 
1.  SYN
2.  SYN/ACK
3.  ACK
4.  PSH, ACK (send the data "Welcome to the server")
5.  ACK
6.  FIN, ACK
7.  ACK


References:

Lesson learnt from https://realpython.com/python-sockets/ and https://www.youtube.com/watch?v=Lbfe3-v7yE0

