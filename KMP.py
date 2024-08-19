# KMP算法实现

def getNext(s):
    next = [-1] * len(s)  
    i = 0 
    j = -1 
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:

            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next

def pipei(s1, s2):
    i = 0  # s1的下标
    j = 0  # s2的下标
    next = getNext(s2)
    while i < len(s1) and j < len(s2):
        if j == -1 or s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j = next[j]
    if j == len(s2):
        return i - j
    else:
        return - 1


if __name__ == "__main__":
    s1 = 'aabaabaaf'  # 文本串
    s2 = 'abaab'  # 模式串
    # print(getNext(s2))
    print(pipei(s1, s2))

