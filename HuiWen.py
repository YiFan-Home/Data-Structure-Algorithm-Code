# 基于栈和队列实现回文匹配

from Stacklist import StackList
from Queuelist import QueueList

class IsPalindrome():
    def __new__(self,string):
        self.__string=list(string)
        self.__stack=StackList()
        self.__queue=QueueList()
        for i in self.__string :
            self.__stack.Push(i)
            self.__queue.Append(i)
        while self.__stack.IsEmpty() != True :
            if self.__stack.Top == self.__queue.Head :
                self.__stack.DeleteTop()
                self.__queue.DeleteHead()
            else:
                print(string,"该文本不是回文")
                return False
        if self.__stack.IsEmpty() :
            print(string,"该文本是回文")
            return True


if __name__ == "__main__":
    string1="好啊你啊好"
    string2="ABCDEABCDE"
    IsPalindrome(string1)
    IsPalindrome(string2)
