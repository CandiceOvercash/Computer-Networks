#CSCI 3010 - Computer Networking
#Assignment 1 - Server.py
#Candice Overcash - Overcashc17

import socket
import os
import sys

ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12221

ssocket.bind((host, port))
ssocket.listen(5) # because the standard is 5

print('Listening on: %s' % str(host), 'and port:', port)

while True:
    # make a connection
    conn, addr = ssocket.accept()

    print('Got a connection from %s'% str(addr))
    data = conn.recv(1024).decode()
    getData= data.split('\n')[0].split(' ')[1][1:]
    print('Data Received:%s' % str(data))
    if getData == 'page1':
        with open('page1.html','r') as pagefile:
            filedata= pagefile.read().replace('\n', '')
            content_len= str(len(filedata))
            header = "HTTP/1.0 200 OK\r\nContent-Length:" + content_len + "\r\n\n"
            conn.sendall((header + filedata).encode())
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    elif getData == 'info':
        with open('info.html', 'r') as infofile:
            infodata = infofile.read().replace('\n', '')
            info_len = str(len(infodata))
            infoheader = "HTTP/1.0 200 OK\r\nContent-Length:" + info_len + "\r\n\n"
            conn.sendall((infoheader + infodata).encode())
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    elif getData == 'download':
        with open('download.zip', 'rb') as downloadfile:
            downloaddata = downloadfile.read()
            download_len = str(len(downloaddata))
            downloadheader = "HTTP/1.0 200 OK\r\nContent-Length:" + download_len + "\r\nContent-Type:application/zip\r\nContent-Disposition:attachment;filename=download.zip\r\n\nDATA"
            conn.send(downloadheader.encode())
            conn.send(downloaddata)
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

    elif getData == 'link':
        with open('link.html', 'r') as linkfile:
            linkdata = linkfile.read().replace('\n', '')
            link_len = str(len(linkdata))
            linkheader = "HTTP/1.0 200 OK\r\nContent-Length:" + link_len + "\r\n\n"
            linkheader += "<a href=\"/download\" download=\"download.zip\"> Download File: download.zip</a>"
            conn.sendall((linkheader + linkdata).encode())
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()
    elif getData == 'exit':
        with open('exit.html', 'r') as exitfile:
            exitdata = exitfile.read().replace('\n', '')
            exit_len = str(len(exitdata))
            exitheader = "HTTP/1.0 200 OK\r\nContent-Length:" + exit_len + "\r\n\n"
            conn.sendall((exitheader + exitdata).encode())
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

    if "echo" in data.lower():
        print("Echo found! \nThe message recieved from the client is: %s"% data)
        conn.sendall(data.encode()) # sends data recieved to client

    if "exit" in data.lower():
        print("Exit found!")
        conn.sendall("Exit found, exiting\n".encode())
        conn.close()
        exit(0)
