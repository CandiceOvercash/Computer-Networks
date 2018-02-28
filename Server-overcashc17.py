#CSCI 3010 - Computer Networking
#Assignment 1 - Server.py
#Candice Overcash - Overcashc17

import socket

ssocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()  #name of local host
port = 12221

ssocket.bind((host,port))
ssocket.listen(5) #because the standard is 5

print('Listening on: %s'% str(host), 'and port:' , port)

while True:
    #make a connection
    conn, addr = ssocket.accept()

    print('Got a connection from %s'% str(addr))
    data = conn.recv(1024).decode()

    if "echo" in data.lower():
        print("Echo found! \nThe message recieved from the client is: %s"% data)
        conn.sendall(data.encode())#sends data recieved to client

    if "exit" in data.lower():
        print("Exit found!")
        conn.sendall("Exiting now!".encode())
        exit()

    conn.close()

ssocket.close()