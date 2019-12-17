from tkinter import *
from Myprotocol.task.request import Request
import sys
#sys.path.append("F:\\学习\\计算机网络\\txt_reader")
import client.glo as g
import math
import os

class BookPage(object):
    def __init__(self, master):
        self.f = open('new_'+g.get_value(),'r',encoding='utf-8')
        #获取用户上次阅读的位置和书签
        f1 = open(g.get_value1(),'r',encoding='utf-8')
        line = f1.readline()
        self.user = line.split(' ')
        self.record = 0
        for j in range(len(self.user)):
            if self.user[j] == g.get_value():
                self.record = j
                break
        self.bookmark = self.user[self.record+2].split(';')
        self.str = ''
        self.fs = self.f.readline()
        self.i = 0
        self.pageNum = 0
        self.root = master
        self.root.geometry('%dx%d' % (400, 510)) #设置窗口大小
        self.createPage()
        self.skipPage(self.pageNum)
    
    def createPage(self):
        while self.fs:
            if(self.fs[0] == '#'):
                break
            self.str += self.fs
            self.fs = self.f.readline()
        self.i = 0
        self.pageNum = int(self.user[self.record+1]) #当前页码
        self.txt = StringVar()
        self.txt.set('第'+str(self.pageNum)+'页')
        self.total = self.getPages() #所有的页数
        self.chapterNum = self.getCurrentChapterByPage() #当前的章节数
        self.chapterName = StringVar()
        self.chapterName.set(self.getNameByChapter())
        self.chapter = self.getChapters() #所有的章节数
        self.l = Label(self.root,textvariable = self.chapterName, fg = 'white', bg = 'gray')
        self.l.pack()
        self.page = Frame(self.root) #创建Frame 
        self.page.pack() 
        self.scroll = Scrollbar()
        self.text = Text(self.page,height = 35)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.text.pack(side=LEFT,fill=Y)
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)
        txt = self.str[self.i:self.i+800]
        self.text.insert('insert',txt)
        self.frame = Frame(self.root)
        self.frame.pack()
        Button(self.frame, text = '<<', command = lambda:self.lastChapter()).grid(row=1, column=1, stick=W)
        Button(self.frame, text = '<', command = lambda:self.lastPage()).grid(row=1, column=2, stick=W)
        Button(self.frame, text = '>', command = lambda:self.nextPage()).grid(row=1, column=4, stick=W)
        Button(self.frame, text = '>>', command = lambda:self.nextChapter()).grid(row=1, column=5, stick=W)
        Button(self.frame, text = '跳页', command = lambda:self.skip()).grid(row=1, column=6, stick=W)
        Button(self.frame, text = '书签', command = lambda:self.mark()).grid(row=1, column=7, stick=W)
        Button(self.frame, text = '返回', command = lambda:self.back()).grid(row=1, column=8,stick=W)
        Label(self.frame,textvariable = self.txt).grid(row=1, column=3,stick=W)
    
    #获得全部页数
    def getPages(self):
        count = 0
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
                count = count+int(math.ceil(len(s)/800))
        return count
    
    #获得全部章数
    def getChapters(self):
        count = 0
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
                count = count + 1
        return count
    
    #通过当前页码获得当前的章
    def getCurrentChapterByPage(self):
        lastPageCount = 0
        pageCount = 0
        chapterCount = -1
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
                lastPageCount = pageCount
                pageCount = pageCount+int(math.ceil(len(s)/800))
                chapterCount = chapterCount+1
                if self.pageNum>lastPageCount and self.pageNum<=pageCount:
                    return chapterCount

    def getNameByChapter(self):
        count = -1
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
                count = count + 1
                if count == self.chapterNum:
                    break
        if count == 0:
            return ''
        else:
            lt = s.split('\n')
            return lt[0]

    #跳页
    def skipPage(self,number):
        num = 0
        j = 0
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while num < number:
            if len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
            if num + int(math.ceil(len(s)/800)) < number:
                num = num + int(math.ceil(len(s)/800))
                continue
            elif num + int(math.ceil(len(s)/800)) == number:
                j = 800*(int(math.ceil(len(s)/800))-1)
                num = num + int(math.ceil(len(s)/800))
            else:
                j = 800*(int(number-num-1))
                num = number
                break
        self.pageNum = number
        self.chapterNum = self.getCurrentChapterByPage()
        self.chapterName.set(self.getNameByChapter())
        self.txt.set('第'+str(self.pageNum)+'页')
        self.text.delete('1.0','end')
        self.text.insert('insert',s[j:j+800])

    #跳章
    def skipChapter(self,number):
        lastPageCount = 0
        pageCount = 0
        chapterCount = -1
        file = open('new_'+g.get_value(),'r',encoding='utf-8')
        s = ''
        line = file.readline()
        while len(line) != 0:
                s = ''
                s += line
                line = file.readline()
                while line:
                    if(line[0] == '#'):
                        break
                    s += line
                    line = file.readline()
                lastPageCount = pageCount
                pageCount = pageCount+int(math.ceil(len(s)/800))
                chapterCount = chapterCount+1
                if chapterCount == number:
                    break
        self.skipPage(lastPageCount+1)
    
    #上一页
    def lastPage(self):
        if self.pageNum == 1:
            return
        self.skipPage(self.pageNum-1)
    
    #下一页
    def nextPage(self):
        if self.pageNum == self.total:
            return
        self.skipPage(self.pageNum+1)
    
    #上一章
    def lastChapter(self):
        if self.chapterNum==0:
            return
        self.skipChapter(self.chapterNum-1)
    
    #下一章
    def nextChapter(self):
        if self.chapterNum==self.chapter:
            return
        self.skipChapter(self.chapterNum+1)

    #用户跳页界面
    def skip(self):
        self.top = Toplevel()
        self.top.title('跳页')
        num = IntVar()
        Entry(self.top, textvariable=num).pack()
        Button(self.top, text='确定', command=lambda:self.comfirmSkip(num.get())).pack()
        Label(self.top, text = '共'+str(self.total)+'页').pack()
    
    #确认跳页
    def comfirmSkip(self,num):
        if num<1 or num>self.total:
            self.top.destroy()
        else:
            self.top.destroy()
            self.skipPage(num)
    
    #书签
    def mark(self):
        self.top1 = Toplevel()
        self.top1.title('书签')
        self.lb = Listbox(self.top1)
        self.lb.pack()
        for bm in self.bookmark:
            if int(bm) != 0:
                self.lb.insert(END,bm)
        Button(self.top1, text = '跳转', command=lambda:self.click()).pack()
        Button(self.top1, text = '删除', command=lambda:self.doubleClick()).pack()
        Button(self.top1, text = '添加', command=lambda:self.addMark()).pack()

    #单击书签跳转
    def click(self):
        s = str(self.lb.curselection())
        p = int(self.lb.get(int(s[1])))
        self.top1.destroy()
        self.skipPage(p)

    #双击书签删除该书签
    def doubleClick(self):
        s = str(self.lb.curselection())
        self.bookmark.remove(str(self.lb.get(int(s[1]))))
        self.lb.delete(int(s[1]))

    #添加书签
    def addMark(self):
        self.bookmark.insert(len(self.bookmark),str(self.pageNum))
        self.lb.insert(END,str(self.pageNum))

    #返回
    def back(self):
        self.user[self.record+1] = str(self.pageNum)
        line = ''
        for bm in self.bookmark:
            line = line+bm+';'
        line = line[:-1]
        self.user[self.record+2] = line
        line = ''
        for i in range(len(self.user)):
            line = line+self.user[i]+' '
        line = line[:-1]
        with open(g.get_value1(),'w',encoding='utf-8') as f1:
            f1.write(line)
            f1.close()
        from client.component.mainPage import MainPage
        self.page.destroy()
        self.l.destroy()
        self.frame.destroy()
        self.scroll.destroy()
        MainPage(self.root)
        self.f.close()
        os.remove('new_'+g.get_value())