
###算法时间复杂度大O阶

####常数阶

常见的赋值，只执行有限次（与N增长无关）的计算，有限次比较，打印等，统统记为O(1) 不存在O（100）这样的
```
#O(1)
n=100
sum = (1+n)*n/2
print("sum:%s" % sum)

```

####线性阶

随着N的增长线性增加
```
#O(n)
n=100
list = [i for i in range(n)]
print('list:%s' % list)
```

####对数阶

```
#O(logN)
n=100
count=1
while(count<n):
    count = count*2
print('count:%s' % count)
```


####平方阶

```
#O(N^2)
n=100
for i in range(n):
    for j in range(n):        
        print('index_sum:%s' % (i+j))
```


####常见时间复杂度大小排序：

O(1)<O(logN)<O(N)<O(NlogN)<O(n^2)<O(n^3)<O(2^N)<O(N!)<O(N^N)