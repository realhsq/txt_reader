import socket
import struct
import operator
import time
import os
import sys
sys.path.append("..")
from Myprotocol.task.request import Request

def download(sock):
    filename = input('请输入要下载的文件名:\n')
    Request('GET',filename,sock)

def  handle(sock):
    while True:
        order = input()
        if operator.eq(order,'1'):
            sock.send(order.encode())
            download(sock)
        elif operator.eq(order,'2'):
            sock.send(order.encode())
            #upload(sock)
        elif operator.eq(order,'3'):
            print('正在关闭连接...')
            time.sleep(0.5)
            sock.send(order.encode())
            break
        else:
            print('命令错误,请重新输入！')
            continue
        line = sock.recv(1024)
        print(line.decode())

if __name__ == '__main__':
    #建立socket并连接8002端口
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('127.0.0.1',8002))
    line = sock.recv(1024)
    print(line.decode())
    handle(sock)
    sock.close()