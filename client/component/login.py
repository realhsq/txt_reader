from tkinter import *
from tkinter.messagebox import *
import sys
import os
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
#sys.path.append('..')
from client.component.mainPage import MainPage
from client.component.signUp import signUpPage
from Myprotocol.task.request import Request
from client.glo import *

#登录界面
class LoginPage(object): 
    def __init__(self, master=None): 
        self.root = master #定义内部变量root 
        self.root.geometry('%dx%d' % (300, 180)) #设置窗口大小 
        self.username = StringVar() 
        self.password = StringVar() 
        self.createPage() 
  
    def createPage(self): 
        self.page = Frame(self.root) #创建Frame 
        self.page.pack() 
        Label(self.page).grid(row=0, stick=W) 
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10) 
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E) 
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10) 
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E) 
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10) 
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)
        Button(self.page, text='注册', command=self.signUp).grid(row=3, column=2, stick=E) 
  
    def loginCheck(self): 
        name = self.username.get() + '.txt'
        secret = self.password.get()
        Request('GET',name+'+user',sock)
        line = ''
        with open('new_'+name,encoding='utf-8') as f:
            line = f.readline()
            f.close()
        with open(name, 'w', encoding='utf-8') as f1:
            f1.write(line)
            f1.close()
        if secret == line.split(' ')[0]: 
            set_value1(name)
            os.remove('new_'+name)
            self.page.destroy() 
            MainPage(self.root) 
        else: 
            os.remove('new_'+name)
            showinfo(title='错误', message='账号或密码错误！')
    def signUp(self):
        self.page.destroy()
        signUpPage(self.root)