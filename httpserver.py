# -*- coding: utf-8 -*-
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print ('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    #print (request)

    try:
        print("test")
        
    finally:
        print("Execution Completed")

    http_response = """\
    hello world
    """

    client_connection.sendall(bytes(http_response, 'UTF-8'))
    client_connection.close()