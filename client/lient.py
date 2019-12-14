
#coding:utf-8

'''

    @DateTime: 	2017-09-24 14:26:31

    @Version: 	1.0

    @Author: 	Unname_Max

'''

import socket

import struct

import operator

import time

import os

#实现下载功能

def download(sock):

    #从服务端接收文件列表

    filelist = sock.recv(1024).decode()

    if operator.eq(filelist,''):

        print ('没有可以下载的文件')

    print (filelist)

    #从用户中输入接收文件名，并发送给服务端

    filename = input('请输入要下载的文件名:\n')

    sock.send(filename.encode())
    
    #获取包大小，并解压

    FILEINFO_SIZE = struct.calcsize('128sI')

    try:

        fhead = sock.recv(1024)

        fhead = sock.recv(FILEINFO_SIZE)

        filename , filesize = struct.unpack('128sI',fhead)

        #接收文件

        with open ('new_'+filename.decode().strip('\00'),'wb') as f:

            ressize = filesize

            while True:

                if ressize>1024:

                    filedata = sock.recv(1024)

                else:

                    filedata = sock.recv(ressize)

                    f.write(filedata)

                    break

                if not filedata:

                    break

                f.write(filedata)

                ressize = ressize - len(filedata)

                if ressize <0:

                    break

        print ('文件传输成功!')

    except Exception as e:

        print (e)

        print ('文件传输失败!')

#实现上传功能

def upload(sock):

    #获取文件路径，并将文件信息打包发送给服务端

    path = input('请输入要上传的文件路径\n')

    filename = input('请输入文件名\n')

    fhead = struct.pack('128sI',filename.encode(),os.stat(filename).st_size)

    sock.send(fhead)

    #传送文件

    with open (path,'rb') as f:

        while True:

            filedata = f.read(1024)

            if not filedata:

                break

            sock.send(filedata)

    print('文件传输结束')

 

def  handle(sock):

    while True:

        order = input()

        if operator.eq(order,'1'):

            sock.send(order.encode())

            download(sock)

        elif operator.eq(order,'2'):

            sock.send(order.encode())

            upload(sock)

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
