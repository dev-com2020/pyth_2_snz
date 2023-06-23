# import serial
#
# ser = serial.Serial('COM4', 9600, timeout=1)
# while True:
#     line = ser.readline()
#     print(line)

import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('serwer ready...')

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Połączenie z {addr}")

        data = client_socket.recv(1024)
        print(f'Odebrane dane: {data.decode()}')

        client_socket.sendall(data)
        client_socket.close()

def start_client():
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(('localhost',12345))
    client_socket.sendall(b'Hello TCP!')
    data = client_socket.recv(1024)
    print(f'Odebrane dane: {data.decode()}')
    client_socket.close()


def start_server_udp():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))
    print('serwer ready...')

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Połączenie z {addr}, odebrano dane {data.decode()}")

        server_socket.sendto(data,addr)


def start_client_udp():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b'HEELO',('localhost',12345))
    data, addr = client_socket.recvfrom(1024)


if __name__ == '__main__':
    start_server_udp()
