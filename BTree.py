# 二叉树实现

class BTree_node():
    def __init__(self,element):
        self.element = element
        self.left = None
        self.right = None
        self.father = None


class BinaryTree():
    def __init__(self,node = None):
        self.root = None

    def IsEmpty(self):
        if self.root == None :
            return True
        else:
            return False

    def Clear(self):
        self.root = None

    @property
    def Depth(self):
        traver = self.root
        box=[]
        box.append(traver)
        n=0
        while box != [] :
            n+=1
            box2=[]
            for i in box :
                if i.left != None :
                    box2.append(i.left)
                if i.right != None :
                    box2.append(i.right)
            box = box2
        return n

    def Creat_index(self,element : list,index : list):
        if len(element) != len(index) or len(element) == 0 :
            print("错误：两个输入维度不一致或为空列表！")
        else:
            if index[0] != 1 :
                index[0]=1
            tree_node = BTree_node(element[0])
            self.root = tree_node
            element.pop(0)
            index.pop(0)
            pre_layer = []
            pre_layer.append(self.root)
            n=1
            while index != [] :
                layer_min = 2**(n)
                n+=1
                layer_max = 2*layer_min
                layer_ele = [None]*layer_min
                del_index = []
                for i in range(0,len(index)) :
                    if index[i] >= layer_min and index[i] < layer_max :
                        del_index.append(i)
                        lay_pos = index[i] - layer_min
                        layer_ele[lay_pos] = element[i]
                
                if del_index == []:
                    break
                
                del_len = len(del_index)
                for i in range(0,del_len):
                    j=del_index[del_len-i-1]
                    index.pop(j)
                    element.pop(j)

                now_layer = [None]*layer_min
                for i in range(0,layer_min):
                    if layer_ele[i] != None :
                        tree_node = BTree_node(layer_ele[i])
                        if i%2 == 0:
                            father = pre_layer[int(i/2)]
                            if father != None:
                                father.left = tree_node
                                now_layer[i] = tree_node
                        else:
                            father = pre_layer[int((i-1)/2)]
                            if father != None:
                                father.right = tree_node
                                now_layer[i] = tree_node
                pre_layer = now_layer

    def Trave(self,code = "pre"):
        if self.root == None :
            print("错误 ：树为空")
        else:
            self.__trave_res = []
            if code == "pre" :
                self.__Trave_pre(self.root)
                return self.__trave_res
            elif code == "mid" :
                self.__Trave_mid(self.root)
                return self.__trave_res
            elif code == "last" :
                self.__Trave_last(self.root)
                return self.__trave_res
            elif code == "layer" :
                self.__Trave_layer(self.root)
                return self.__trave_res
            else:
                print("错误 : code取值非法！")
    def __Trave_pre(self,node):
        if node != None:
            self.__trave_res.append(node.element)
            self.__Trave_pre(node.left)
            self.__Trave_pre(node.right)
    def __Trave_mid(self,node):
        if node != None :
            self.__Trave_mid(node.left)
            self.__trave_res.append(node.element)
            self.__Trave_mid(node.right)
    def __Trave_last(self,node):
        if node != None :
            self.__Trave_last(node.left)
            self.__Trave_last(node.right)
            self.__trave_res.append(node.element)
    def __Trave_layer(self,node):
        traver = node
        box = []
        box.append(traver)
        while box != [] :
            lay_ele = []
            box2=[]
            for i in box :
                lay_ele.append(i.element)
                if i.left != None :
                    box2.append(i.left)
                if i.right != None :
                    box2.append(i.right)

            self.__trave_res.append(lay_ele)
            box = box2

    def Find_leaf(self):
        self.__leaves = []
        self.__leaf(self.root)
        return self.__leaves
    def __leaf(self,node):
        if node != None :
            if node.left == None and node.right == None :
                self.__leaves.append(node.element)
            self.__leaf(node.left)
            self.__leaf(node.right)

    def Get_treenode(self,index : int):
        if index <= 0 :
            print("错误 ：输入应为大于等于1的整数！")
            return False
        else:
            if index == 1 :
                return self.root
            road = []
            while index != 1 :
                if index % 2 == 0 :
                    road.append(0)
                    index = index / 2
                else:
                    road.append(1)
                    index = index // 2
            traver = self.root
            for i in range(len(road)-1,-1,-1):
                if road[i] == 0 and traver.left != None :
                    traver = traver.left
                elif road[i] == 1 and traver.right != None :
                    traver = traver.right
                else:
                    print("错误 ：无该节点")
                    return False
                    break
            return traver
                    
    def Grow(self,index : int,element,code):
        codelist = ["left","right"]
        if index >= 1 and code in codelist:
            father = self.Get_treenode(index)
            if father != False :
                if code == "left" and father.left == None :
                    newnode = BTree_node(element)
                    father.left = newnode
                    newnode.father = father
                elif code == "right" and father.right == None :
                    newnode = BTree_node(element)
                    father.right = newnode
                    newnode.father = father
                else:
                    print("错误 ：该位置的%s节点以经有元素"%code)
            else:
                print("错误 ：无index对应的该节点！")
        else:
            print("错误 ：index小于1或未找到code！")


if __name__ == "__main__":
    print("构建二叉树")
    T = BinaryTree()
    element = ["A","B","F","C","E","G","D","H"]
    index = [1,2,4,3,6,7,9,20]
    T.Creat_index(element,index)
    print("构建完成！")
    print("----------------------------")
    print("遍历：")
    print("先序遍历")
    a=T.Trave("pre")
    print(a)
    print("中序遍历")
    a=T.Trave("mid")
    print(a)
    print("后序遍历")
    a=T.Trave("last")
    print(a)
    print("层序遍历")
    a=T.Trave("layer")
    print(a)
    print("---------------------------")
    print("深度：",T.Depth)
    leaf = T.Find_leaf()
    print("叶子：",leaf)
    print("---------------------------")
    print("9号位置的元素为：")
    sixnode = T.Get_treenode(9)
    print(sixnode.element)
    print("在9位置的左孩子节点新增'M'")
    T.Grow(9,"M",code="left")
    print("新增完成！")
    leaf = T.Find_leaf()
    print("叶子：",leaf)

