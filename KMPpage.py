import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import time

class KMPPage():
    def __init__(self,root):
        self.root=root
        self.root.title('KMP_Show')
        self.root.geometry('1300x800')
        self.root.resizable(height = False,width = False)
        self.string1 = tk.StringVar()
        self.string2 = tk.StringVar()
        self.ans_var = tk.StringVar()
        self.CraetPage()

    def CraetPage(self):
        s = ttk.Style()
        s.configure('my.TButton', font=('FangSong',15,'bold'))
        ttk.Label(self.root,text="动 画 演 示 框",font=30).place(x=600,y=12,width=600,height=25)
        self.figure = tk.Canvas(self.root,bg='darkblue',width=1200,height=500)
        self.figure.place(x=50,y=50)
        ttk.Label(self.root,text="请输入主串：",font=30).place(x=65,y=600,width=120,height=50)
        self.entry_S1 = ttk.Entry(self.root,textvariable=self.string1,font=30)
        self.entry_S1.place(x=200,y=600,width=400,height=50)
        ttk.Label(self.root,text="请输入子串：",font=30).place(x=640,y=600,width=120,height=50)
        self.entry_S2 = ttk.Entry(self.root,textvariable=self.string2,font=30)
        self.entry_S2.place(x=775,y=600,width=400,height=50)
        ttk.Label(self.root,text="查找结果：",font=30).place(x=65,y=700,width=120,height=50)
        self.ans_text=tk.Text(self.root,font=60,height=2)
        self.ans_text.place(x=200,y=700,width=500,height=50)
        ttk.Button(self.root,text="动画演示",style='my.TButton',command = self.Show).place(x=1000,y=700,width=100,height=50)
        ttk.Button(self.root,text="开始查找",style='my.TButton',command = self.Search).place(x=800,y=700,width=100,height=50)
        ttk.Button(self.root,text="清除",style='my.TButton',command = self.Clear).place(x=1150,y=700,width=50,height=50)

    def GetNext(self):
        next = [-1] * self.len_s2
        i = 0 
        j = -1 
        while i < self.len_s2 - 1:
            if j == -1 or self.S2[i] == self.S2[j]:

                i += 1
                j += 1
                next[i] = j
            else:
                j = next[j]
        return next

    def Establish(self):
        self.figure.delete(tk.ALL)
        left = -30
        right = 20
        #显示主串
        for i in range (0,self.len_s1):
            left += 55
            right += 55
            self.figure.create_rectangle(left,100,right,150,fill='darkorange',outline='white',width=2)
            self.figure.create_text((left+25,125),text=self.S1[i],fill='green',font =('微软雅黑',15,'bold'))
        #获取NEXT数组
        self.nextlist = self.GetNext()
        #显示子串
        left = -30
        right = 20
        self.son_rec = []
        self.son_string = []
        self.next_num = []
        for i in range (0,self.len_s2):
            left += 55
            right += 55
            rec = self.figure.create_rectangle(left,160,right,210,fill='darkorange',outline='white',width=2)
            self.son_rec.append(rec)
            string = self.figure.create_text((left+25,185),text=self.S2[i],fill='green',font =('微软雅黑',15,'bold'))
            self.son_string.append(string)
            num = self.figure.create_text((left+25,220),text=self.nextlist[i],fill='white',font =('微软雅黑',15,'bold'))
            self.next_num.append(num)
        #显示箭头
        point_i = [(35, 25), (65, 25), (65, 70), (50, 95), (35, 70)]
        self.arrowhead_i = self.figure.create_polygon(point_i, fill='pink',outline='white',width=2)
        point_j = [(35, 300), (65, 300), (65, 255), (50, 230), (35, 255)]
        self.arrowhead_j = self.figure.create_polygon(point_j, fill='pink',outline='white',width=2)

    def Show(self):
        self.S1 = self.string1.get()
        self.S2 = self.string2.get()
        if self.S1 == "" or self.S1 == "" :
            return False
        self.len_s1 = len(self.S1)
        self.len_s2 = len(self.S2)
        if self.len_s1 >= 20 :
            self.figure.create_text((600,400),text="进行动画演示的主串长度请勿超过20",fill='deeppink',font =('微软雅黑',45,'bold'))
            return False
        self.Establish()
        self.figure.update_idletasks()
        time.sleep(2)
        i = 0  
        j = 0  
        while i < self.len_s1 and j < self.len_s2 and i + self.len_s2 -j <= self.len_s1:
            if j == -1 or self.S1[i] == self.S2[j]:
                i += 1
                j += 1
                self.figure.move(self.arrowhead_i,55,0)
                self.figure.move(self.arrowhead_j,55,0)
                self.figure.update_idletasks()
                time.sleep(0.5)
            else:
                judge = self.figure.create_text((50+55*i,320),text="NO",fill='red',font =('微软雅黑',25,'bold'))
                self.figure.update_idletasks()
                time.sleep(1)
                self.figure.delete(judge)
                self.figure.update_idletasks()
                move = j - self.nextlist[j]
                j = self.nextlist[j]
                for r in range(0,self.len_s2):
                    self.figure.move(self.son_rec[r],55*move,0)
                    self.figure.move(self.son_string[r],55*move,0)
                    self.figure.move(self.next_num[r],55*move,0)
                self.figure.update_idletasks()
                time.sleep(1)                
        if j == self.len_s2:
            index = i - j + 1
            self.figure.create_text((600,400),text="匹配成功！起始位置为第%d位"%index,fill='deeppink',font =('微软雅黑',45,'bold'))
            self.figure.update_idletasks()
        else:
            self.figure.create_text((600,400),text="匹配失败！",fill='deeppink',font =('微软雅黑',45,'bold'))
            self.figure.update_idletasks()

    def Search(self):
        self.ans_text.delete('1.0','end')
        self.S1 = self.string1.get()
        self.S2 = self.string2.get()
        if self.S1 == "" or self.S1 == "" :
            return False 
        self.len_s1 = len(self.S1)
        self.len_s2 = len(self.S2)
        i = 0
        j = 0
        nextlist = self.GetNext()
        while i < self.len_s1 and j < self.len_s2:
            if j == -1 or self.S1[i] == self.S2[j]:
                i += 1
                j += 1
            else:
                j = nextlist[j]
        if j == self.len_s2:
            index = i - j + 1
            self.ans_var = "查找成功！起始位置为第%d位"%index + "\n"
            self.ans_text.insert("end",self.ans_var)
        else:
            self.ans_var = "查找失败！" + "\n"
            self.ans_text.insert("end",self.ans_var)

    def Clear(self):
        self.entry_S1.delete(0,'end')
        self.entry_S2.delete(0,'end')
        self.figure.delete(tk.ALL)
        self.ans_text.delete('1.0','end')


root=tk.Tk()
KMPPage(root)
root.mainloop()