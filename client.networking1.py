#client side
import socket

host = socket.gethostname()
port = 12221
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host, port))

x = str(input("put your message "))
s.sendall(x.encode('ascii')) #anything you want to send you must first encode, converts string to bit
data = s.recv(1024)
s.close()

print("Received", repr(data))