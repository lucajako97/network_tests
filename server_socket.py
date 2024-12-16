import socket
from sys import platform
import re 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
IFACE = "eth1\0"
PROTO = "tcp"
VERSION = 4

if PROTO == "tcp":
    PROTOCOL = socket.SOCK_STREAM
else:
    PROTOCOL = socket.SOCK_DGRAM

if VERSION == 4:
    AF = socket.AF_INET
else:
    AF = socket.AF_INET6

with socket.socket(family=AF, type=PROTOCOL, proto=0, fileno=None) as s:

    if len(re.findall("linux", platform)):
        s.setsockopt(socket.SOL_SOCKET, 25, IFACE.encode('utf-8'))
    else:
        import IN
        s.setsockopt(socket.SOL_SOCKET, IN.SO_BINDTODEVICE, IFACE.encode('utf-8'))

    if PROTO == "tcp":
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
    else:
        while True:
            data = s.recv(1024)
            if not data:
                break
            s.send(data)