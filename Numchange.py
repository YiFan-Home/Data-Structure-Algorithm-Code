# 基于栈实现进制转换

from Stacklist import StackList

class IntChang():
    """
    进制转换，默认10进制转换为其余进制
    """
    def __new__(self,num : int,system : int =2):
        self.__system = int(system)
        self.__num = int(num)
        self.__result=StackList()
        r=self.__num
        if self.__num < self.__system :
            if self.__system == 16:
                if self.__num == 10 :
                    return "A"
                elif self.__num == 11 :
                    return "B"
                elif self.__num == 12 :
                    return "C"
                elif self.__num == 13 :
                    return "D"
                elif self.__num == 14 :
                    return "E"
                else:
                    return "F"
            else:
                return self.__num
        else:
            while self.__num >= self.__system :
                remainder=self.__num % self.__system
                self.__num=self.__num//self.__system
                self.__result.Push(remainder)
            self.__result.Push(self.__num)
            new_num=self.__result.AllPop()
            if self.__system == 16 :
                i=0
                while i < len(new_num) :
                    if new_num[i] == 10 :
                        new_num[i] = "A"
                        i=i+1
                    elif new_num[i] == 11 :
                        new_num[i] = "B"
                        i=i+1
                    elif new_num[i] == 12 :
                        new_num[i] = "C"
                        i=i+1
                    elif new_num[i] == 13 :
                        new_num[i] = "D"
                        i=i+1
                    elif new_num[i] == 14 :
                        new_num[i] = "E"
                        i=i+1
                    elif new_num[i] == 15 :
                        new_num[i] = "F"
                        i=i+1
                    else:
                        i=i+1
            result = "".join(map(str,new_num))
            return result

class IntToTen():
    def __new__(self,oldnum,oldsystem : int):
        oldnum = str(oldnum)
        if oldsystem == 10 :
            return oldnum
        elif oldsystem == 16 :
            newnumber = 0
            num_len = len(oldnum)
            for i in range(1,num_len+1):
                if oldnum[num_len-i] == "A" :
                    newnumber = newnumber + 10*(16**(i-1))
                elif oldnum[num_len-i] == "B" :
                    newnumber = newnumber + 11*(16**(i-1))
                elif oldnum[num_len-i] == "C" :
                    newnumber = newnumber + 12*(16**(i-1))
                elif oldnum[num_len-i] == "D" :
                    newnumber = newnumber + 13*(16**(i-1))
                elif oldnum[num_len-i] == "E" :
                    newnumber = newnumber + 14*(16**(i-1))
                elif oldnum[num_len-i] == "F" :
                    newnumber = newnumber + 15*(16**(i-1))
                else:
                    newnumber = newnumber + int(oldnum[num_len-i])*(16**(i-1))
            return newnumber
        else:
            newnumber=0
            num_len = len(oldnum)
            for i in range(1,num_len+1) :
                newnumber = newnumber + int(oldnum[num_len-i])*(oldsystem**(i-1))
            return newnumber

class SystemChange():
    def __new__(self,oldnum,oldsystem : int,newsystem : int):
        if oldsystem == newsystem :
            return oldnum
        else:
            tennum=IntToTen(oldnum,oldsystem)
            newnum=IntChang(int(tennum),newsystem)
            return newnum


if __name__ == "__main__":
    # 100的16进制
    print(SystemChange(100,10,16))
    # 100的2进制
    print(SystemChange(100,10,2))

