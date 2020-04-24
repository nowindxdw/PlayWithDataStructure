# -*- coding: utf-8 -*-
#O(1)
def run_O1(n):
    sum = (1+n)*n/2
    print("sum:%s" % sum)


#O(n)
def run_ON(n):
    list = [i for i in range(n)]
    print('list:%s' % list)


#O(logN)
def run_OlogN(n):
    count=1
    while(count<n):
        count = count*2
    print('count:%s' % count)


#O(N^2)
def run_ONpower2(n):
    for i in range(n):
        for j in range(n):
            print('index_sum:%s' % (i + j))


if __name__ == "__main__":
    #run_O1(100)
    #run_ON(100)
    #run_OlogN(100)
    run_ONpower2(100)