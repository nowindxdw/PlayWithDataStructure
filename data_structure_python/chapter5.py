# -*- coding: utf-8 -*-


# 朴素的模式匹配：
# t非空， pos>=1,pos<=len(s)
def index_func(s,t,pos):
    n = len(s)
    m = len(t)
    print("n:%s" % n)
    print("m:%s" % m)
    if pos > 0:
        i = pos
        while(i < n-m+1):
            print(i)
            sub_str = s[i:i+m]
            print(sub_str)
            if sub_str != t:
                i+=1
            else:
                return i
    return 0



if __name__ == "__main__":

    s = "ggggooglehello0"
    t = "google"
    print(index_func(s,t,1))