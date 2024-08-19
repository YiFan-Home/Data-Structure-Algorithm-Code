# 利用栈实现括号匹配检查

from Stacklist import StackList

class IsLegal():
    def __new__(self,obj):
        self.__obj=list(obj)
        self.__stack=StackList()
        for i in self.__obj :
            if i =="(" or i =="[" :
                self.__stack.Push(i)
            elif i == ")" or i == "]" :
                if self.__stack.IsEmpty() :
                    print("括弧使用非法")
                    return False
                else:
                    if i == ")" and self.__stack.Top == "(" :
                        self.__stack.DeleteTop()
                    elif i == "]" and self.__stack.Top == "[" :
                        self.__stack.DeleteTop()
                    else:
                        print("括弧使用非法")
                        return False
        if self.__stack.IsEmpty() :
            print("括弧使用合法")
            return True
        else:
            print("括弧使用非法")
            return False


if __name__ == "__main__":
    IsLegal("3+((5+4)*9)+[8-(9*[7-9])/8]")
    IsLegal("(3+((5+4)*9)+[8-(9*[7-9])/8]")
    IsLegal("()")
