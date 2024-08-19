# 哈夫曼编码实现

class huffnode():
    def __init__(self,element):
        self.element = element
        self.left = None
        self.right = None
        self.father = None
        self.children = []

class HuffmanCode():
    @staticmethod
    def code_str(string : str):
        char_count = {} 
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        char_count = dict(sorted(char_count.items(), key=lambda item: item[1]))
        obj = list(char_count.keys())
        fre = list(char_count.values())
        code_dic = HuffmanCode.code_list(obj,fre)
        return code_dic #, fathernode

    @staticmethod
    def code_list(obj : list,fre : list):
        char_num = len(obj)
        huffmancod = []
        for i in range(0,char_num):
            huffmancod.append([])
        L = obj.copy()
        while len(L) != 1 :
            fathernode = huffnode("#")
            if isinstance(L[0],huffnode) :
                fathernode.left = L[0]
                L[0].father = fathernode
                fathernode.children.extend(L[0].children)
                for i in L[0].children :
                    index = obj.index(i)
                    huffmancod[index].append(0)
            else:
                kids = huffnode(L[0])
                fathernode.left = kids
                kids.father = fathernode
                fathernode.children.append(L[0])
                index = obj.index(L[0])
                huffmancod[index].append(0)
            if isinstance(L[1],huffnode) :
                fathernode.right = L[1]
                L[1].father = fathernode
                fathernode.children.extend(L[1].children)
                for i in L[1].children :
                    index = obj.index(i)
                    huffmancod[index].append(1)
            else:
                kids = huffnode(L[1])
                fathernode.right = kids
                kids.father = fathernode
                fathernode.children.append(L[1])
                index = obj.index(L[1])
                huffmancod[index].append(1)

            newfre = fre[0] + fre[1]
            fre.pop(0)
            fre.pop(0)
            L.pop(0)
            L.pop(0)
            fre_len = len(fre)
            for i in range(0,fre_len):
                if newfre <= fre[i] :
                    fre.insert(i,newfre)
                    L.insert(i,fathernode)
                    break
                else:
                    if i == fre_len-1 :
                        fre.append(newfre)
                        L.append(fathernode)
            if fre_len == 0 :
                L.append(fathernode)
        codes = []
        for i in range(0,char_num):
            code = ""
            for j in range(len(huffmancod[i])-1,-1,-1):
                code += str(huffmancod[i][j])
            codes.append(code)
        keys = obj
        values = codes
        code_dic = dictionary = dict(zip(keys, values))
        return code_dic #, fathernode

    @staticmethod
    def encrype(string : str,dictionary : dict):
        encrype_str = ""
        for i in string :
            encrype_str += dictionary[i]
        return encrype_str

    @staticmethod
    def decrypt(string : str,dictionary : dict):
        decrypt_tree = HuffmanCode.__get_huffmantree(dictionary)
        interpreter = decrypt_tree
        decrypt_str = ""
        for i in string :
            if i == "0" :
                interpreter = interpreter.left
                if interpreter.left == None :
                    decrypt_str += interpreter.element
                    interpreter = decrypt_tree
            elif i == "1" :
                interpreter = interpreter.right
                if interpreter.right == None :
                    decrypt_str += interpreter.element
                    interpreter = decrypt_tree
            else:
                print("错误 ：密文不合法！")
        return decrypt_str

    @staticmethod
    def __get_huffmantree(dictionary : dict):
        hufftreenode = huffnode("#")
        hufftree_head = hufftreenode
        traver = hufftree_head
        for i in dictionary :
            code = dictionary[i]
            for j in code :
                if j == "0" :
                    if traver.left != None :
                        traver = traver.left
                    else:
                        hufftreenode = huffnode("#")
                        hufftreenode.father = traver
                        traver.left = hufftreenode
                        traver = traver.left
                else:
                    if traver.right != None :
                        traver = traver.right
                    else:
                        hufftreenode = huffnode("#")
                        hufftreenode.father = traver
                        traver.right = hufftreenode
                        traver = traver.right
            traver.element = i
            traver = hufftree_head
        return hufftree_head


if __name__ == "__main__":
    string = "aaaf   ff你sddg:fbb好chef gwtdgggsfs11111ss你你"
    print("进行Huffman编码的字符串：",string)

    code_dict = HuffmanCode.code_str(string)
    print("huffman码表字典：",code_dict)
    print("码表：")
    for i in code_dict :
        print(i," : ",code_dict[i])

    print("huffman编码结果：")
    newstr = HuffmanCode.encrype(string,code_dict)
    print(newstr)
    print("huffman解码结果：")
    jiemi = HuffmanCode.decrypt(newstr,code_dict)
    print(jiemi)

