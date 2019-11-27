from tkinter import *
import socket
import sys
import os
sys.path.append("..")
from Myprotocol.task.request import Request

class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()
    def initWidgets(self):
        Request('GET','1.txt',sock)
        f = open('new_1.txt','r',encoding='utf-8')
        str = f.read()
        f.close()
        lb = Label(root,text = str)
        lb.place(x = 20, y = 36)

def closeWindow():
    os.remove('new_1.txt')
    root.destroy()

#建立socket并连接8002端口
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',8002))
root = Tk()
root.title('test')
root.protocol('WM_DELETE_WINDOW', closeWindow)
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
root.geometry("250x250+30+30")  
App(root)
root.mainloop()
sock.close()