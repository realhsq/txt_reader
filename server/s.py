import threading
import socket
import time
import operator
import os
import struct
import sys
sys.path.append("..")
from Myprotocol.task.response import Response

def handle(connect,address):
    print ('%s:%s is connectting...'%(address))
    while True:
        Response(connect)

if __name__ == '__main__':
    if not os.path.exists('files'):
        os.mkdir('files')
    #工作目录换到files文件夹
    os.chdir('files')
    #建立socket链接，并监听8002端口
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('',8002))
    sock.listen(100)
    while True:
        connect,address = sock.accept()
        t = threading.Thread(target = handle,args = (connect,address))
        t.setDaemon(True)
        t.start()
    sock.close()