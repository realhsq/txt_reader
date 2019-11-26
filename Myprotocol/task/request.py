from Myprotocol.header import Header
import struct
import socket

def Request(method, info, sock):
    if 'GET' == method:
        header = Header('txt','utf-8')
        message = 'GET\n' + 'Content-Type: ' + header.showType + '\n' + 'Content-Encoding: ' + header.showEncoding + '\n' + info
        sock.send(message.encode('utf-8'))
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