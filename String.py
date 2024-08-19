# 字符串实现

class String ():
    """
    串及其基本操作：
        object=String(max : int,string : str)
        串的长度.Length  获取指定位置的元素.Get(index : int)  将串以字符数组的形式展示.DataShow()
        将串以字符串的形式展示.StrShow()  串的空间.Space  串扩展空间.Expand(newspace : int)
        按索引获取子串.Substring(start : int,end : int)  向串中添加.Add(newstr : str,index : int,space_code : bool)
        在串尾部添加.Append(newstr : str,space_code : bool)  删除指定位置长度的子串.Detele(index : int,length : int)
        连接两个串Connect(str1,str2)  从某位置开始查找子串.Search(obj : str,start : int,time_code : bool)
        替换字串.Replace(substr : str,obj : str,time_code : bool,space_code : str)  
        判断两串是否相等StrIsequal(str1,str2)
    """
    def __init__(self,max : int,string=None):
        self.__max=max   #最多容纳个数
        self.__num=0   #初始元素个数
        self.__data=[None]*self.__max  #初始10个none
        if string != None :
            self.__num=min(len(string),self.__max)
            for i in range (0,self.__num):
                self.__data[i]=string[i]
    @property
    def Length (self) :
        return self.__num

    def Get(self,index : int):
        if index >= self.__num :
            print("error : index is out of range")
        else:
            if index <0 :
                index=0
            return self.__data[index]

    def DataShow(self):
        print(self.__data)

    def StrShow(self):
        data=self.__data[:self.Length]
        Str="".join('%s'%i for i in data)
        print(Str)

    @property
    def Space (self) :
        return self.__max

    def Expand(self,newspace : int):
        """
        扩展串空间
            newspace : 新增的空间
        返回类型
            :无
        """
        if newspace < 0 :
            newspace = 0
        self.__max=self.__max+newspace
        for i in range(0,newspace):
            self.__data.append(None)

    def Substring(self,start : int,end : int):
        """
        获取子串
            ：获取从start开始（包括start）到end（包括end）之间的子串，并返回
            start : int 开始索引位置 （Length > start >= 0）
            end : int 结束索引位置 （Length > end > 0）
            : start <= end 
        返回类型
            : String
        """
        if start >= self.__num or end >= self.__num :
            print("error : The parameter is out of range")
        elif start < 0 or end <= 0 :
            print("error : start should be greater than or equal to 0 ; end should be greater than 0")
        elif start > end :
            print("error : end should be greater than start")
        else:
            substring=String(end-start+1)
            if start == end :
                substring.Append(self.Get(end))
                return substring
            else:
                for i in range (start,end+1):
                    substring.Append(self.Get(i))
                return substring

    def Add(self,newstr : str,index : int,space_code : str ="fixed"):
        """
        向串中添加
            ：在index位置前添加新串newstr,space_code默认为"fixed"
            newstr : str 将要添加的串
            index : int 添加的位置
            space_cod : str {fixed:空间固定 ； expand:空间自动扩张} 
            : 当index < 0 时默认index = 0
            : 当index >= Length 时默认在串的尾部添加
            ：当空间不可自动扩张时：
                若在串中添加，空间不足时将报错，新串无法添加
                若在串的尾部添加，空间不足时，可以添加部分新串使空间填满，但会警告
            ：当空间可自动扩张时，若原空间不足将自动补齐缺少的空间
        返回类型
            : 无
        """
        #if index > self.__num:
            #print("error : index is out of range")
        if index >= self.__num:
            self.Append(newstr,space_code=space_code)
        else:
            if index < 0:
                index=0

            if space_code == "fixed" :
                self.__add_fixed(newstr,index)
            elif space_code == "expand" :
                self.__add_expand(newstr,index)
            else:
                print("error : space_code hase not found")
    def __add_fixed(self,newstr,index):
        length=len(newstr)
        if length+self.__num > self.__max :
            print("error : data overflow")
        else:
            t=self.__num+length
            for i in range (1,self.__num-index+1):
                #print(self.__data[self.__num-i])
                self.__data[t-i]=self.__data[self.__num-i]
            for i in range (0,length):
                self.__data[index+i]=newstr[i]
            self.__num=t
    def __add_expand(self,newstr,index):
        length=len(newstr)
        if length+self.__num > self.__max :
            self.Expand(length+self.__num-self.__max)
        self.__add_fixed(newstr,index)

    def Append(self,newstr : str,space_code : str ="fixed"):
        """
        向串尾部添加
            ：space_code默认为"fixed"
            newstr : str 将要添加的串
            space_cod : str {fixed:空间固定 ； expand:空间自动扩张} 
            ：当空间不可自动扩张时：空间不足时，可以添加部分新串使空间填满，但会警告
            ：当空间可自动扩张时，若原空间不足将自动补齐缺少的空间
        返回类型
            : 无
        """
        if space_code == "fixed" :
            self.__append_fixed(newstr)
        elif space_code == "expand" :
            self.__append_expand(newstr)
        else:
             print("error : space_code hase not found")   
    def __append_fixed(self,newstr):
        length=len(newstr)
        t = 0
        for i in range (0,min((self.__max-self.__num),length)):
            t += 1
            self.__data[self.__num]=newstr[i]
            self.__num = self.__num + 1
        if t < length :
            print("warning : data overflow")
    def __append_expand(self,newstr):
        length=len(newstr)
        if length+self.__num > self.__max :
            self.Expand(length+self.__num-self.__max)
        for i in range (0,length):
            self.__data[self.__num]=newstr[i]
            self.__num=self.__num+1

    def Detele(self,index : int,length : int):
        """
        删除指定位置长度的子串
            : 删除串中从index位置（包括index）开始长度为length的子串
            index : int 开始位置 (index < Length)
            length : int 删除串的长度 
            ：index < 0 时默认index = 0
            ：允许删除位置超出串
        返回类型
            : 无
        """
        if index >=self.__num :
            print("error : index is out of range")
        else:
            if index < 0 :
                index = 0
            if index+length >= self.__num :
                for i in range (index,self.__num-1):
                    self.__data[i]=None
                    self.__num = index
            else:
                for i in range (index,index+length):
                    self.__data[i]=None
                for i in range (index+length,self.__num):
                    self.__data[i-length]=self.__data[i]
                    self.__data[i]=None
                self.__num=self.__num-length

    @staticmethod
    def Connect(str1,str2):
        """
        连接两串
            ：静态方法
            ：将两串连接，并返回连接后的串(str1在前)
            str1 : String 将要连接的串
            Str2 : String 将要连接的串
            ：连接后新串的空间为两串的长度和
        返回类型
            ：String
        """
        box=String(str1.Length+str2.Length)
        for i in range (0,str1.Length):
            box.Append(str1.Get(i))
        for i in range (0,str2.Length):
            box.Append(str2.Get(i))
        return box
#time_code:{false:一次匹配 ； ture:全部匹配}
    def Search(self,obj : str,start : int = 0,time_code : bool =False):
        """
        从某位置开始查找子串
            ：从某位置开始查找子串，若存在则返回其所在位置索引，若不存在返回False
            obj : str 查找的目标
            start : int (start < Length)
            time_code : bool {False:一次匹配 ； Ture:全部匹配} 
        返回类型
            若仅匹配一次 : int
            若全部匹配 : 列表
        """
        if start >= self.__num :
            print("error : index is out of range")
        else:
            if start < 0 :
                start = 0
            if time_code == False :
                return self.__search_false(obj,start)
            elif time_code == True :
                return self.__search_true(obj,start)
            else:
                print("error : time_code hase not found")
    def __search_false(self,obj,start):
        length=len(obj)
        finder=0
        while start+length <= self.__num and finder == 0 :
            for i in range (0,length):
                if self.__data[start+i] != obj[i] :
                    finder=0
                    break
                else:
                    finder=finder+1
            if finder != 0 :
                return start
            else:
                start = start + 1
        return False
    def __search_true(self,obj,start):
        length=len(obj)
        finder=0
        index=[]
        while start+length <= self.__num and finder == 0 :
            for i in range (0,length):
                if self.__data[start+i] != obj[i] :
                    finder=0
                    break
                else:
                    finder=finder+1
            if finder != 0 :
                index.append(start)
                start = start + length
                finder = 0
            else:
                start = start + 1
        if index == []:
            return False
        else:
            return index
#time_code:{false:一次匹配 ； ture:全部匹配} ； space_code:{fixed:空间固定 ； expand:空间自动扩张}
    def Replace(self,substr : str,obj : str,time_code : bool =False,space_code : str ="fixed"):
        """
        替换子串
            ：space_code默认为"fixed" ；time_code默认为False
            substr : str 将要被替换的串
            obj : str 替换入串的子串
            time_code : bool {False:一次匹配 ； Ture:全部匹配}
            space_cod : str {fixed:空间固定 ； expand:空间自动扩张} 
            :若空间不可自动扩张，不允许替换后的串超出空间范围，否则替换失败
        返回类型
            : 无
        """
        if self.Search(substr) == False:
            print("error : there is no substr")
        else:
            if time_code == False :
                self.__replace_false(substr,obj,space_code)
            elif time_code == True :
                self.__replace_ture(substr,obj,space_code)
            else:
                print("error : time_code hase not found")
    def __replace_false(self,substr,obj,space_code):
        if space_code == "fixed" :
            if self.__max < self.__num-len(substr)+len(obj) :
                print("error : space is not enough")
            else:
                self.__replace_ff(substr,obj)
        elif space_code == "expand" :
            newspace=self.__num-len(substr)+len(obj)-self.__max
            self.Expand(newspace)
            self.__replace_ff(substr,obj)
        else:
            print("error : space_code hase not found")
    def __replace_ff(self,substr,obj):
        index=self.Search(substr)
        sub_len=len(substr)
        self.Detele(index,sub_len)
        self.Add(obj,index)
    def __replace_ture(self,substr,obj,space_code):
        indexs=self.Search(substr,time_code=True)
        sub_num=len(indexs)
        if space_code == "fixed" :
            if self.__max < self.__num-(len(substr)-len(obj))*sub_num :
                print("error : space is not enough")
            else:
                self.__replace_tf(substr,obj,indexs,sub_num)
        elif space_code == "expand" :
            newspace=self.__num-(len(substr)-len(obj))*sub_num-self.__max
            self.Expand(newspace)
            self.__replace_tf(substr,obj,indexs,sub_num)
    def __replace_tf(self,substr,obj,indexs,sub_num):
        sub_len=len(substr)
        ob_len=len(obj)
        change=ob_len-sub_len
        time=0
        while time < sub_num :
            index=indexs[time]+time*change
            self.Detele(index,sub_len)
            self.Add(obj,index)
            time=time+1

    @staticmethod
    def StrIsequal(str1,str2):
        """
        比较两串
            ：静态方法
            ：比较两串，相等返回Ture,否则返回False
            str1 : String 将要比较的串
            Str2 : String 将要比较的串
            ：比较不包括两串的空间，仅比较两串中的元素
        返回类型
            ：bool
        """
        if isinstance(str1,String) and isinstance(str2,String) :          
            if str1.Length != str2.Length :
                return False
            else:
                for i in range(0,str1.Length) :
                    if str1.Get(i) != str2.Get(i) :
                        return False
                return True
        else:
            print("错误 ：输入类型不对")



if __name__ == "__main__":
    print("创建串：",end="")
    A = String(20,"ftddr43sgg好很好分辨可以退")
    A.StrShow()
    print("串的长度为：",A.Length," ","串的空间大小为：",A.Space)
    print("第1个字符为：",A.Get(1)," ","第13个字符为：",A.Get(13))
    print("位置1到13的子串为：",end="")
    A.Substring(1,13).StrShow()
    print("------------------------------------------------")
    print("在串中插入：")
    print("1、空间不可自动改变")
    A.Add("新添加1",3,space_code="fixed")
    A.StrShow()
    print("2、空间可自动改变")
    A.Add("新添加1",3,space_code="expand")
    A.StrShow()
    print("串的长度为：",A.Length," ","串的空间大小为：",A.Space)
    print("------------------------------------------------")
    print("在串尾插入：")
    print("1、空间不可自动改变")
    A.Append("新添加2",space_code="fixed")
    A.StrShow()
    print("2、空间可自动改变")
    A.Append("新添加2",space_code="expand")
    A.StrShow()
    print("串的长度为：",A.Length," ","串的空间大小为：",A.Space)
    print("------------------------------------------------")
    print("删除：")
    print("1、从22位置开始删除长度为10")
    A.Detele(22,10)
    A.StrShow()
    print("2、从2位置开始删除长度为2")
    A.Detele(2,2)
    A.StrShow()
    print("------------------------------------------------")
    print("两串连接：")
    print("A串：",end="")
    A.StrShow()
    print("A串的长度为：",A.Length," ","串的空间大小为：",A.Space)
    B = String(10,"连接串啊好呀")
    print("B串：",end="")
    B.StrShow()
    print("B串的长度为：",B.Length," ","串的空间大小为：",B.Space)
    print("连接后串：",end="")
    C = String.Connect(A,B)
    C.StrShow()
    print("C串的长度为：",C.Length," ","串的空间大小为：",C.Space)
    print("------------------------------------------------")
    print("查找：")
    print("1、查找一次")
    print("'好'在串中第一次出现的位置是：",C.Search("好",time_code=False))
    print("2、查找全部")
    print("'好'在串中出现的位置是：",C.Search("好",time_code=True))
    print("------------------------------------------------")
    print("替换：")
    print("1、一次替换，不可变空间:'可以'--》'maybe'")
    C.Replace("可以","maybe",time_code=False,space_code="fixed")
    C.StrShow()
    print("2、一次替换，可变空间:'可以'--》'maybe'")
    C.Replace("可以","maybe",time_code=False,space_code="expand")
    C.StrShow()
    print("3、一次替换，不可变空间:'g'--》'G'")
    C.Replace("g","G",time_code=False,space_code="fixed")
    C.StrShow()
    print("4、多次替换，可变空间:'好'--》'棒'")
    C.Replace("好","棒",time_code=True,space_code="fixed")
    C.StrShow()
    print("------------------------------------------------")
    A = String(4,"好啊好")
    B = String(3,"好啊好")
    C = String(4,"好啊啊")
    print("A串：",end="")
    A.StrShow()
    print("A串的长度为：",A.Length," ","A串的空间大小为：",A.Space)
    print("B串：",end="")
    B.StrShow()
    print("B串的长度为：",B.Length," ","B串的空间大小为：",B.Space)
    print("C串：",end="")
    C.StrShow()
    print("C串的长度为：",C.Length," ","C串的空间大小为：",C.Space)
    print("A,B是否相等：",String.StrIsequal(A,B))
    print("A,C是否相等：",String.StrIsequal(A,C))
    print("C,B是否相等：",String.StrIsequal(C,B))
