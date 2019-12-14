from tkinter import *
from tkinter.messagebox import *
#import sys
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
from Myprotocol.task.request import Request
import os
from client.glo import sock

#注册界面
class signUpPage(object): 
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
        Button(self.page, text='注册', command=self.signUpCheck).grid(row=3, stick=W, pady=10) 
        Button(self.page, text='返回', command=self.back).grid(row=3, column=1, stick=E)
    
    def signUpCheck(self):
        name = self.username.get() 
        secret = self.password.get() 
        #print(os.getcwd())
        if (name == '') or (secret == ''):
            showinfo(title='错误', message='账号或密码格式错误！')
        else:
            with open (name+'.txt','w') as f:
                f.write((secret + '\n'))
            f.close()
            Request('POST',name + '.txt+user',sock)
            os.remove(name+'.txt')
            showinfo(title='成功', message='注册成功！')
            self.page.destroy()
            from client.component.login import LoginPage
            LoginPage(self.root)
    def back(self):
        self.page.destroy()
        from client.component.login import LoginPage
        LoginPage(self.root)