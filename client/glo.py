import socket

#定义全局变量sock，便于其他文件引用
global sock
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)