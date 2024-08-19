# 基于链表实现多项式的加、减、乘计算

class PolynomialNode():
    def __init__(self,coefficient,frequency):
        self.coefficient=int(coefficient)
        self.frequency=int(frequency)
        self.next=None

class PolynomialLink():
    def __init__(self,equation : str):
        self.head=None
        if equation != 0:
            coef_list , freq_list = self.__CFExtract(equation)
            for i in range(0,len (coef_list)) :
                node = PolynomialNode(coef_list[i],freq_list[i])
                if self.IsEmpty() :
                    self.head=node
                else:
                    traver=self.head
                    while traver.next != None:
                        traver=traver.next
                    traver.next=node
            #self.Trave()

    def IsEmpty(self):
        if self.head == None :
            return True
        else:
            return False

    def __CFExtract(self,equation : str) :
        # 提取系数，和指数
        equ_list=list(equation)
        i=0
        while i < len(equ_list) :
            if equ_list[i] == "-" :
                equ_list.insert(i,"+")
                i=i+2
            else:
                i=i+1
        equstr="".join(equ_list)
        equ_list=equstr.split("+")
        coef_list=[]
        freq_list=[]
        for i in equ_list :
            if i[0] == "x" :
                coef_list.append(1)
                if "^" in i :
                    box = i.split("^")
                    freq_list.append(int(box[1]))
                else:
                    freq_list.append(1)
            elif "-x" in i :
                coef_list.append(-1)
                if "x^" in i :
                    box=i.split("-x^")
                    freq_list.append(int(box[1]))
                else:
                    freq_list.append(1)
            else:
                if "x^" in i :
                    box = i.split("x^")
                    coef_list.append(int(box[0]))
                    freq_list.append(int(box[1]))
                else:
                    if "x" in i :
                        freq_list.append(1)
                        box = i.split("x")
                        coef_list.append(int(box[0]))
                    else :
                        freq_list.append(0)
                        coef_list.append(int(i))
        return coef_list , freq_list

    def Trave(self):
        if self.IsEmpty():
            print("错误：该单链表为空")
        else:
            travers=self.head
            while travers != None:
                if travers.next == None:
                    print(travers.coefficient,":",travers.frequency)
                else:
                    print(travers.coefficient,":",travers.frequency,"——>",end=' ')
                travers=travers.next

    def AddEnd(self,coefficient,frequency):
        node=PolynomialNode(int(coefficient),int(frequency))
        if self.IsEmpty() :
            self.head=node
        else:
            traver=self.head
            while traver.next != None:
                traver=traver.next
            traver.next=node

    def Show(self):
        if self.IsEmpty():
            print("0")
        else:
            travers=self.head
            while travers != None:
                if travers.next == None:
                    print(travers.coefficient,"x^",travers.frequency)  #可改进输出以+3x^5的形式
                else:
                    print(travers.coefficient,"x^",travers.frequency,"+",end='')
                travers=travers.next

    def ThrowZero(self):
        traver=self.head
        while traver != None and traver.coefficient == 0 :
            self.head=traver.next
            traver=self.head
        if traver != None:
            while traver.next != None :
                if traver.next.coefficient == 0 :
                    traver.next=traver.next.next
                else:
                    traver=traver.next

    def Change(self):
        if self.IsEmpty():
            return 0
        else:
            result=""
            travers=self.head
            while travers != None:
                if travers.next == None:
                    result=result+str(travers.coefficient)+"x^"+str(travers.frequency)
                else:
                    result=result+str(travers.coefficient)+"x^"+str(travers.frequency)+"+"
                travers=travers.next
            result=result.replace("+-","-")
            result=result.replace("x^0","")
            result=result.replace("1x","x")
            return result

class Pol_Calculate():
    def Add_func(self,equ1,equ2):
        if isinstance(equ1 , str) :
            A=PolynomialLink(equ1)
        else:
            A=equ1
        if isinstance(equ2 , str) :
            B=PolynomialLink(equ2)
        else:
            B=equ2
        if A.head != None and B.head != None:
            curA=A.head
            curB=B.head
            while curB.frequency < curA.frequency :    #预先整理链表前端
                if curB.next == None :
                    curB.next=curA
                    return B
                else:
                    if curB.next.frequency >= curA.frequency :
                        cur=curB.next
                        curB.next=curA
                        A.head=B.head
                        B.head=cur
                        break
                    else:
                        curB=curB.next
            curB=B.head
            while curB != None and curA != None:     #保证每次循环都有初始curB系数都一定大于初始curA系数
                if curB.frequency == curA.frequency :
                    curA.coefficient = curA.coefficient + curB.coefficient
                    B.head=curB.next
                    curB=B.head
                elif curA.next == None :
                    curA.next=curB
                    B.head = None
                    curB = B.head
                else:
                    if curB.frequency < curA.next.frequency :
                        B.head=curB.next
                        curB.next=curA.next
                        curA.next=curB
                        curA=curA.next
                        curB=B.head
                    else:
                        curA=curA.next
            A.ThrowZero()
            return A
        elif A.head != None and B.head == None:
            return A
        elif B.head != None and A.head == None :
            return B
        else:
            res=PolynomialLink(0)

    def Minus_func(self,equ1,equ2):
        if isinstance(equ1 , str) :
            A=PolynomialLink(equ1)
        else:
            A=equ1
        if isinstance(equ2 , str) :
            B=PolynomialLink(equ2)
        else:
            B=equ2
        curA=A.head
        curB=B.head
        while curB != None :
            curB.coefficient= 0-curB.coefficient
            curB=curB.next
        result=self.Add_func(A,B)
        return result

    def Multiply_func(self,equ1,equ2):
        if isinstance(equ1 , str) :
            A=PolynomialLink(equ1)
        else:
            A=equ1
        if isinstance(equ2 , str) :
            B=PolynomialLink(equ2)
        else:
            B=equ2
        if A.head != None and B.head != None:
            box1=PolynomialLink(0)
            box2=PolynomialLink(0)
            curB=B.head
            while curB != None :
                curA=A.head
                while curA != None:
                    newfrequency=curA.frequency+curB.frequency
                    newcoefficient=curA.coefficient * curB.coefficient
                    box1.AddEnd(newcoefficient,newfrequency)
                    curA=curA.next
                box2.head=self.Add_func(box1,box2).head
                box1.head=None
                curB=curB.next
            return box2
        else:
            result=PolynomialLink(0)
            return result

    def Derivat_func(self,equ1):
        if isinstance(equ1 , str) :
            A=PolynomialLink(equ1)
        else:
            A=equ1

        if A.head == None :
            return A
        else:
            curA=A.head
            if curA.frequency == 0 :
                A.head = curA.next
            curA=A.head
            while curA != None :
                curA.coefficient=curA.coefficient*curA.frequency
                curA.frequency=curA.frequency-1
                curA=curA.next
            return A

class Pol_IsLegal():
    def __new__(self,equation : str):
        self.__equ=equation
        self.__equ="0+"+self.__equ
        self.__equ = self.__equ.replace("x","1x")
        self.__equ = self.__equ.replace("+-","-")
        self.__equ = self.__equ.replace("-","+-")
        self.__equ = self.__equ.replace("x+","x^1+")
        self.__equ = self.__equ.replace("x^","+")
        print(self.__equ)
        exa=self.__equ.split("+")
        try:
            for i in exa :
                num = int(i)
        except:
            return False
        return True


if __name__ == "__main__":
    #A=PolynomialLink("3-x-5x^3-x^7+7x^9+10x^13")
    res=Pol_Calculate().Minus_func("1-x+x^4-13x^8","2x+4x^3-10x^5")
    res.Show()
    print(res.Change())
