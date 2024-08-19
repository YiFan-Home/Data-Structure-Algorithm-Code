# 单链表实现

class SingleNode():
    """
    单链表节点：
        object=SingleNode(element)
    """
    def __init__(self,element):
        self.element=element
        self.next=None

class SingleLinkList():
    """
    单链表：
        object=SingleLinkList()
        判断链表是否为空.IsEmpty  链表长度.Lnegth  在表头插入.AddHead(element)
        在表尾插入.AddEnd(element)  在表中给定位置插入.AddMiddle(position : int,element)
        遍历链表.Trave  按元素删除节点.Remove(key)  按位置删除节点.Remove(position : int)
        查询节点是否存在.Search(key)
    """
    def __init__(self,node=None):
        self.head=node
        self.__count=0

    def IsEmpty(self):
        """
        判断链表是否为空
            ：链表为空，返回True ; 链表非空，返回False
        返回类型
            ：bool
        """
        if self.head == None :
            return True
        else:
            return False

    @property
    def Length(self):
        """
        获取链表长度
            ：返回链表的长度（即栈中元素个数）
        返回类型
            ：int
        """
        return self.__count

    def AddHead(self,element):
        node=SingleNode(element)
        node.next=self.head
        self.head=node
        self.__count=self.__count+1

    def AddEnd(self,element):
        node=SingleNode(element)
        if self.IsEmpty() :
            self.head=node
            self.__count=self.__count+1
        else:
            traver=self.head
            while traver.next != None:
                traver=traver.next
            traver.next=node
            self.__count=self.__count+1

    def AddMiddle(self,position : int,element):  
        """
        在表中指定位置插入
            ：在第position个位置前插入（注：头节点位置为0）
            ：当position < 0时默认position = 0
            ：当position超出位置范围时默认为在链表尾部插入
        """
        if position <= 0 :
            self.AddHead(element)
            self.__count=self.__count+1
        elif position >= self.__count:
            self.AddEnd(element)
            self.__count=self.__count+1
        else:
            node=SingleNode(element)
            num=0
            pre_node=self.head
            while num < (position-1):
                pre_node=pre_node.next
                num=num+1
            node.next=pre_node.next
            pre_node.next=node
            self.__count=self.__count+1

    def Trave(self):
        """
        遍历链表
            ：将链表展示出来
        返回类型
            ：无
        """
        if self.IsEmpty():
            print("该单链表为空")
        else:
            travers=self.head
            while travers != None:
                if travers.next == None:
                    print(travers.element,end=' ')
                else:
                    print(travers.element,"——>",end=' ')
                travers=travers.next   
            print("\n遍历完成")

    def Remove(self,key):
        """
        删除节点
            ：根据节点中元素删除，有多个相同元素时仅删除第一个
            key : 关键元素（删除的目标元素）
        返回类型
            ：无
        """
        if self.IsEmpty():
            print("错误：该链表为空")
        elif self.head.element == key:  #若删除的是头节点
            self.head=self.head.next
            self.__count=self.__count-1
        else:
            travers=self.head
            pre_traver=None
            while travers != None:
                if travers.element == key :
                    pre_traver.next=travers.next
                    self.__count=self.__count-1
                    break
                elif travers.next == None :
                    print("错误：该元素不在链表节点当中")
                    break
                else:
                    pre_traver=travers
                    travers=travers.next

    def Remove_pos(self,position : int):
        if self.IsEmpty() :
            print("错误：该链表为空")
        elif position < 0 and position >= self.__count :
            print("错误 ：索引超出范围")
        else:
            if position == 0 :
                self.head=self.head.next
                self.__count=self.__count-1
            else:
                traver = self.head
                pretraver = None
                for i in range(0,position):
                    pretraver = traver
                    traver = traver.next
                pretraver.next = traver.next
                self.__count=self.__count-1
            
    def Search(self,key):
        """
        判断节点是否存在
            ：存在，返回True ; 不存在，返回False
        返回类型
            ：bool
        """
        if self.IsEmpty():
            print("错误：该链表为空")
        else:
            travers=self.head
            while travers != None:
                if travers.element == key :
                    return True
                    break
                elif travers.next == None :
                    return False
                    break
                else:
                    travers=travers.next


if __name__ == "__main__":
    print("创建空链表")
    A=SingleLinkList()
    print("创建完成")
    print("链表是否为空：",A.IsEmpty())
    print("添加元素")
    A.AddEnd(1)
    A.AddEnd("f")
    A.AddEnd(2)
    A.AddEnd("y")
    A.AddEnd(3)
    A.AddEnd("fyf")
    A.AddEnd("好")
    A.Trave()
    print("链表是否为空：",A.IsEmpty())
    print("尾部插入")
    A.AddEnd("尾")
    A.Trave()
    print("头部插入")
    A.AddHead("头")
    A.Trave()
    print("表中插入")
    A.AddMiddle(3,"中")
    A.Trave()
    print("删除表中元素‘好’")
    A.Remove("好")
    A.Trave()
    print("删除单链表第1个位置的节点")
    A.Remove_pos(1)
    A.Trave()
    print("查找元素‘中’是否存在：",A.Search("中"))
    print("表中元素个数：",A.Length)
    print("链表是否为空：",A.IsEmpty())
