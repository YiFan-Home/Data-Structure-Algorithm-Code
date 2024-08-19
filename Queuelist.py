# 队列实现

class QueueList():
    """
    队列及其基本操作：
        object=QueueList()
        判断队列是否为空.IsEmpty()  入队.Append(element)  队列的长度.Length
        获取队列头部元素.Head  出队列.Out()  删除队列头部元素.DeleteHead()
        显示队列.Show()  清空队列.Clear()
    """
    def __init__(self):
        self.__queue=[]
        self.__quetail=0

    def IsEmpty(self):
        if self.__quetail==0:
            return True
        else:
            return False    

    def Append(self,element):
        self.__queue.append(element)
        self.__quetail=self.__quetail+1

    @property
    def Length(self):
        return self.__quetail

    @property
    def Head(self):
        if self.IsEmpty() :
            print("错误：该队列为空")
        else:
            return self.__queue[0]

    def Out(self):
        if self.IsEmpty() :
            print("错误：该队列为空")
        else:
            box=self.__queue[0]
            del self.__queue[0]
            self.__quetail=self.__quetail-1
            return box

    def DeleteHead(self):
        if self.IsEmpty() :
            print("错误：该队列为空")
        else:
            del self.__queue[0]
            self.__quetail=self.__quetail-1

    def Show(self):
        if self.IsEmpty() :
            print("错误：该队列为空")
        else:
            print("队列头部",self.__queue,"队列尾部")

    def Clear(self):
        self.__queue.clear()
        self.__quetail=0


if __name__ == "__main__":
    A = QueueList()
    print("队列是否为空：",A.IsEmpty())
    print("向队列中添加元素")
    A.Append(1)
    A.Append("f")
    A.Append(2)
    A.Append("y")
    A.Append(3)
    A.Append("fyf")
    A.Append("好")
    A.Show()
    print("入队列：‘new’")
    A.Append("new")
    A.Show()
    print("出队列，并返回出队列元素")
    print("出队列元素为：",A.Out())
    A.Show()
    print("获取队列头部元素")
    print("队列头部元素为：",A.Head)
    A.Show()
    print("删除队列头部元素，无返回")
    A.DeleteHead()
    A.Show()
    print("队列的长度为：",A.Length)
    print("清空队列")
    A.Clear()
    print("队列是否为空：",A.IsEmpty())
