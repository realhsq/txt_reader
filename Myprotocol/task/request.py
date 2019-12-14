import struct
import socket
import os
#import sys
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
from Myprotocol.header import Header

def Request(method, info, sock):
    #客户端发送GET请求
    if 'GET' == method:
        #请求获取txt文件
        if '.txt' in info:
            header = Header('txt','utf-8')
            message = 'GET\n' + 'Content-Type:' + header.showType() + '\n' + 'Content-Encoding:' + header.showEncoding() + '\n' + info
            sock.send(message.encode('utf-8'))
            FILEINFO_SIZE = struct.calcsize('128sI')
            try:
                #fhead = sock.recv(1024)
                fhead = sock.recv(FILEINFO_SIZE)
                filename , filesize = struct.unpack('128sI',fhead)
                #接收文件
                if '+user' in info:
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
            return
        #请求获取所有小说的书名
        elif 'all_names' == info:
            header = Header('all_names','utf-8')
            message = 'GET\n' + 'Content-Type:' + header.showType() + '\n' + 'Content-Encoding:' + header.showEncoding() + '\n' + info
            sock.send(message.encode('utf-8'))
            names = sock.recv(1024).decode('utf-8')
            return names
    #客户端发送POST请求
    elif 'POST' == method:
        #上传用户信息
        if '.txt+user' in info:
            header = Header('txt+user','utf-8')
            message = 'POST\n' + 'Content-Type:' + header.showType() + '\n' + 'Content-Encoding:' + header.showEncoding() + '\n' + info
            sock.send(message.encode('utf-8'))
            #print(os.getcwd())
            files = os.listdir()
            filename = info[:-5]
            while True:
                if filename in files:
                    break
            fhead = struct.pack('128sI',filename.encode(),os.stat(filename).st_size)
            sock.send(fhead)
            #传送文件
            with open (filename,'rb') as f:
                while True:
                    filedata = f.read(1024)
                    if not filedata:
                        break
                    sock.send(filedata)