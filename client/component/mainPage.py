from tkinter import *
from tkinter.messagebox import *
from Myprotocol.task.request import Request
import sys
import os
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
from client.component.bookPage import BookPage
from client.glo import *
import client.glo as g

#主界面，显示所有可阅读的小说
class MainPage:
    def __init__(self, master):
        self.root = master
        self.root.geometry('%dx%d' % (400, 250)) #设置窗口大小
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)
        self.page.place(x = 0,y = 0)
        self.lb = Listbox(self.page,width = 56)
        self.lb.pack()
        str = Request('GET','all_names',sock)
        names = str.split('\n')
        #names = ['abc.txt','def.txt']
        i = 0
        for name in names:
            #Button(self.page,text = name[:-4],width = 56,padx = 0,command = lambda:self.openBook()).grid(row = i)
            self.lb.insert(END,name[:-4])
            i = i + 1
        self.lb.bind("<Double-1>", self.click)
        Button(self.page, text = '返回', command = lambda:self.back()).pack()
        Button(self.page, text = '下载', command = lambda:self.download()).pack()
    
    def click(self, event):
        s = str(self.lb.curselection())
        g.set_value(str(self.lb.get(int(s[1]))) + '.txt')
        print(g.get_value())
        Request('GET',g.get_value()+'+book',sock)
        f = open(g.get_value1(),'r',encoding='utf-8')
        line = f.readline()
        f.close()
        strs = line.split(' ')
        if g.get_value() not in strs:
            line = line+' '+g.get_value()+' '+str(1)+' '+'1'
        with open(g.get_value1(),'w',encoding='utf-8') as f1:
            f1.write(line)
            f1.close()
        self.page.destroy()
        BookPage(self.root)

    def back(self):
        Request('POST',g.get_value1()+'+user',sock)
        os.remove(g.get_value1())
        from client.component.login import LoginPage
        self.page.destroy()
        LoginPage(self.root)

    def download(self):
        s = str(self.lb.curselection())
        value = str(self.lb.get(int(s[1]))) + '.txt'
        os.chdir('download')
        Request('GET',value+'+book',sock)
        showinfo(title='成功', message='下载成功！')
        os.chdir('..')