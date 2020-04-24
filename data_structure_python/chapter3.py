# -*- coding: utf-8 -*-
OK = 1
ERROR = 0

#模拟顺序表获取元素 时间复杂度O(1)
def get_elem(l, i):
    if len(l)==0 or i<1 or i >len(l):
        raise Exception(ERROR)
    e = l[i-1]
    return e


#模拟顺序表插入元素 时间复杂度O(n)
def list_insert(l,i,e):
    MAX_LENGTH = 10
    LIST_LENGTH = 6
    if LIST_LENGTH == MAX_LENGTH:
        raise Exception(ERROR)
    if i<1 or i >len(l):
        raise Exception(ERROR)
    a = list(range(i-1,LIST_LENGTH))
    a.reverse()
    print(a)
    for k in a:
        l[k+1] = l[k]
    l[i-1] = e
    LIST_LENGTH+=1
    return OK

#模拟顺序表删除元素 时间复杂度O(n)
def list_delete(l,i):
    LENGTH = len(l)
    if len(l) == 0 :
        raise Exception(ERROR)
    if i<1 or i >len(l):
        raise Exception(ERROR)
    del_ele = l[i-1] #获取被删除元素
    # print(del_ele)
    if i<len(l):  # 删除的不是最后一个元素
        a = list(range(i - 1, len(l)))
        # print(a)
        for k in a:
            if k == len(l)-1:
                l[k] = ""
            else:
                l[k] = l[k+1]
    else:
        l.pop()   #删除最后一个元素
    # print(l)
    LENGTH -=1
    return OK,LENGTH

if __name__ == "__main__":
    pass
    # LIST = ["a","b","c","a","d","e"]
    # res = ""
    # res = get_elem(LIST,3)
    # print("res=%s" %res)

    #list_insert(LIST,10,"f")
    #LIST = ["a","b","c","a","d","e","","","",""]
    #list_insert(LIST,3,"f")
    #print(LIST)

    #LIST = ["a","b","c","a","d","e","","","k","g"]
    #list_delete(LIST,3)
    #print(LIST)