import socket
import struct
import os
import time

def Response(connect):
    message = connect.recv(1024).decode('utf-8')
    if len(message) == 0:
        return
    str = message.split('\n')
    req = str[0]
    #处理GET请求
    if 'GET' == req:
        type = str[1]
        #向客户端发送txt文件
        if 'Content-Type:txt' == type:
            #print(os.getcwd())
            if '+book' in str[3]:
                os.chdir('books')
            elif '+user' in str[3]:
                os.chdir('users')
            filename = str[3][:-5]
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
            os.chdir('..')
        #将全部小说的书名发给客户端
        elif 'Content-Type:all_names' == type:
            os.chdir('books')
            files = os.listdir()
            os.chdir('..')
            names = ''
            for name in files:
                names = names + name + '\n'
            names = names[:-1]
            connect.send(names.encode('utf-8'))
            print(names)
    #处理客户端的POST请求
    elif 'POST' == req:
        type = str[1]
        if 'Content-Type:txt+user' == type:
            FILEINFO_SIZE = struct.calcsize('128sI')
            try:
                #获取打包好的文件信息，并解包
                fhead = connect.recv(FILEINFO_SIZE)
                filename , filesize = struct.unpack('128sI',fhead)
                filename = filename.decode().strip('\00')
                #文件名必须去掉\00，否则会报错，此处为接收文件
                #print(filename)
                #print(os.getcwd())
                os.chdir('users')
                with open (filename,'wb') as f:
                    ressize = filesize
                    while True:
                        if ressize>1024:
                            filedata = connect.recv(1024)
                        else:
                            filedata = connect.recv(ressize)
                            f.write(filedata)
                            break
                        if not filedata:
                            break
                        f.write(filedata)
                        ressize = ressize - len(filedata)
                        if ressize <0:
                            break
                os.chdir('..')
            except Exception as e:
                os.chdir('..')