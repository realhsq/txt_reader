from tkinter import *
from Myprotocol.task.request import Request
import sys
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
from client.glo import sock

#主界面，显示所有可阅读的小说
class MainPage:
    def __init__(self, master):
        self.root = master
        self.root.geometry('%dx%d' % (400, 500)) #设置窗口大小
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)
        self.page.place(x = 0,y = 0)
        str = Request('GET','all_names',sock)
        names = str.split('\n')
        #names = ['abc.txt','def.txt']
        i = 0
        for name in names:
            Button(self.page,text = name[:-4],width = 56,padx = 0).grid(row = i)
            i = i + 1
