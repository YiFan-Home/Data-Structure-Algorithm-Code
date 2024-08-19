# 顺序表实现

class FyList():
    '''
    顺序表及其基本操作
    #判断表是否为空.IsEmpty()   #判断是否满.IsFull()   #统计顺序表中元素个数.Count
    #向顺序表输入元素.CreateFylist()    #表尾插入.AddEnd(element)   #表头插入.AddHead(element)   
    #表中某一位置插入.AddMiddle(position,element)
    #查找某元素位置.FindElement(element)    #查看某一位置元素.Look(position)
    #增加顺序表空间.Expand(space)    #删除顺序表空间.Shrink(space)
    #删除某一位置元素.Delete(position)     #修改某一位置元素.UpElement(position,newelement)
    #展示顺序表.ShowList()
    '''
    def __init__(self,max=10):
        self.max=max   #最多容纳个数
        self.num=0   #初始元素个数
        self.data=[None]*self.max  #初始10个none
#显示顺序表
    def ShowList(self):
        print("顺序表：",self.data)
#判断是否为空
    def IsEmpty(self):
        if self.num==0:
            print("顺序表数据为空")
        else:
            print("顺序表不为空")
#判断是否满
    def IsFull(self):
        if self.num==self.max:
            print("顺序表已满")
        else:
            print("顺序表未满")
#向顺序表输入元素
    def CreateFylist(self):
        element=input("请输入元素(按回车确认，按‘#’结束)：")
        while element !='#' :
            if self.num < self.max-1 :
                self.data[self.num]=element   #记录元素
                self.num=self.num+1   #记录元素个数
                element=input("请输入元素(按回车确认，按‘#’结束)：")
            elif self.num == self.max-1 :
                self.data[self.num]=element   #记录元素
                self.num=self.num+1   #记录元素个数
                print("键入完成，顺序表已满")
                break
            else:
                print("顺序表已满，无法键入")
                break
        #print(self.data)
#查找某元素位置
    def FindElement(self,element):
        if element in self.data:
            key_position=self.data.index(element)
            print("查询成功，该元素在顺序表中位置为：",key_position)
        else:
            print("查询失败，该元素不存在于顺序表中")
#删除某一位置元素
    def Delete(self,position : int):
        if position < self.num and position >= 0:
            #print("删除前",self.data)
            self.num=self.num-1
            for i in range (position,self.num):
                self.data[i]=self.data[i+1]   #删除位置后的元素前移
            self.data[self.num]=None
            self.num=self.num-1
        else:
            print("该位置无元素或该位置不在顺序表当中")
#查看某一位置元素
    def Look(self,position : int):
        if position < self.num and position >= 0:
            print("第%d个元素为："%position,self.data[position])
        else:
            print("该位置无元素或该位置不在顺序表当中")
#修改某一位置元素
    def UpElement(self,position : int,newelement):
        if position < self.num and position >= 0:
            #print("修改前",self.data)
            self.data[position]=newelement
            print("修改后:",self.data)
        else:
            print("该位置无元素或该位置不在顺序表当中")
#统计顺序表中元素个数
    @property
    def Count(self):
        print("顺序表中元素个数为：",self.num)
#表尾插入
    def AddEnd(self,element):
        if self.num < self.max:
            self.data[self.num]=element
            self.num=self.num+1
        else:
            print("顺序表已满，无法添加")
#表头插入
    def AddHead(self,element):
        if self.num < self.max:
            for i in range(0,self.num):
                self.data[self.num-i]=self.data[self.num-i-1]   #所有元素后移
            self.data[0]=element
            self.num=self.num+1
        else:
            print("顺序表已满，无法添加")
#表中某一位置插入
    def AddMiddle(self,position : int,element):
        if self.num < self.max:
            if position < self.num and position >= 0 :
                for i in range(0,self.num-position):
                    self.data[self.num-i]=self.data[self.num-i-1]   #插入位置处以后所有元素后移（包括该位置元素）
                self.data[position]=element
                self.num=self.num+1
            else:
                print("该位置无元素或该位置不在顺序表当中")
        else:
            print("顺序表已满，无法添加")
#增加顺序表空间
    def Expand(self,space : int):
        self.max=self.max+space
        for i in range(1,space+1):
            self.data.append(None)    #初始化新增空间为None
        #print(self.data)
#删除顺序表空间(仅可删除无元素的空间)
    def Shrink(self,space : int):
        if space <= self.max-self.num :
            for i in range (0,space):
                del self.data[self.max-1]
                self.max=self.max-1
        else:
            print("删除空间范围大于可删除空间范围")

 
A=FyList(15)
print("判断是否为空")
A.IsEmpty()
print("创建顺序表")
A.CreateFylist()
A.ShowList()
print("缩小5个空间")
A.Shrink(5)
A.ShowList()
print("缩小20个空间")
A.Shrink(20)
A.ShowList()
print("扩大2个空间")
A.Expand(2)
A.ShowList()
print("判断是否满")
A.IsFull()
print("表头插入")
A.AddHead("头")
A.ShowList()
print("表中4位置插入")
A.AddMiddle(4,element="中")
A.ShowList()
print("表尾插入")
A.AddEnd(element="尾")
A.ShowList()
print("查看4位置元素")
A.Look(4)
print("查找‘中’的位置")
A.FindElement("中")
print("修改3位置元素")
A.UpElement(3,"新")
print("删除3位置元素")
A.Delete(3)
A.ShowList()
A.Count