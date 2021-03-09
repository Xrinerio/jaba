import socket
import multiprocessing as mp
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(('localhost', 6666))


def write_msg():
    thread = threading.Thread(target=listen_server)
    thread.start()
    #proc = mp.Process(target=listen_server)
    #proc.start()
    while True:
        msg = input()
        server.send(msg.encode('utf-8'))


def listen_server():
    while True:
        data = server.recv(1024)
        print(data.decode('utf-8'))


if __name__ == '__main__':
    write_msg()
