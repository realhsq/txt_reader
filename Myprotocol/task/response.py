import socket
import struct
import os

def Response(connect):
    message = connect.recv(1024).decode('utf-8')
    str = message.split('\n')
    filename = str[3]
    files = os.listdir()
    while True:
        if filename in files:
            break
    fhead = struct.pack('128sI',filename.encode(),os.stat(filename).st_size)
    connect.send(fhead)
    with open(filename,'rb') as f:
            while True:
                filedata = f.read(1024)
                if not filedata:
                    break
                connect.send(filedata)