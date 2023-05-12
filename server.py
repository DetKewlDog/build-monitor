import socket
import monitor
from config import *

msg = monitor.init()
with socket.socket() as server:
    server.bind((IP, PORT))
    server.listen()
    sock, addr = server.accept()
    with sock:
        while True:
            msg = monitor.get_msg()
            if msg == "":
                continue
            sock.send(msg.encode())