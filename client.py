import socket
from config import *
import os

ERROR = '\033[91m'
PRINT = '\033[97m'
NORMAL = '\033[90m'

EXCEPTION_STRING = 'Exception'
EXCEPTION_END_STRING = 'Filename:'
DEBUG_LOG_STRING = '(Filename: C:\\buildslave\\unity\\build\\Runtime/Export/Debug/Debug.bindings.h Line: 39)'

def log(text):
    is_error = False
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if is_error or EXCEPTION_STRING in line:
            is_error = True
            print(ERROR + line)
        elif DEBUG_LOG_STRING in line or (
            i + 1 < len(lines) and
            DEBUG_LOG_STRING in lines[i + 1]
        ):
            print(PRINT + line)
        else:
            print(NORMAL + line)

        if is_error and EXCEPTION_END_STRING in line:
            is_error = False

os.system("")

with socket.socket() as sock:
    sock.connect(IP, PORT)
    while True:
        log(sock.recv(4096).decode())