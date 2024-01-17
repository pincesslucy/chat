import socket
import json

HOST = '203.236.8.208'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        message_dict = input()

        s.sendall(message_dict.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print(f'서버응답:{data}')