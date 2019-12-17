import socket

#定义全局变量sock，便于其他文件引用
global sock
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
global bookName
bookName = ''
def init():
    global bookName
    bookName = ''
def set_value(value):
    global bookName
    bookName = value
def get_value():
    global bookName
    return bookName
global userName
userName = ''
def init1():
    global userName
    userName = ''
def set_value1(value):
    global userName
    userName = value
def get_value1():
    global userName
    return userName