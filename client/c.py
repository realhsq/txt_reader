import socket
from tkinter import *
import sys
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
sys.path.append('..')
import os
from client.component.login import LoginPage
from client.glo import sock

def closeWindow():
    root.destroy()

global s
s=1
#建立socket并连接8002端口
sock.connect(('127.0.0.1',8002))
root = Tk()
root.title('test')
root.protocol('WM_DELETE_WINDOW', closeWindow)
# 设置窗口的大小和位置
# width x height + x_offset + y_offset
LoginPage(root)
root.mainloop()
sock.close()