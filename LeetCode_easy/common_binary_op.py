# -*- coding: utf-8 -*-
# 常用的位操作

#本文分两部分，第一部分列举几个有趣的位操作，第二部分讲解算法中常用的 n & (n - 1) 操作，
# 顺便把用到这个技巧的算法题列出来讲解一下。因为位操作很简单，所以假设读者已经了解与、或、异或这三种基本操作。


### 一、几个有趣的位操作
'''
1. 利用或操作 `|` 和空格将英文字符转换为小写

```c
('a' | ' ') = 'a'
('A' | ' ') = 'a'
```

2. 利用与操作 `&` 和下划线将英文字符转换为大写

```c
('b' & '_') = 'B'
('B' & '_') = 'B'
```

3. 利用异或操作 `^` 和空格进行英文字符大小写互换

```c
('d' ^ ' ') = 'D'
('D' ^ ' ') = 'd'
```
python 位运算

<<	按位左移，左移n位相当于乘以2的n次方
>>	按位右移 ，左移n位相当于除以2的n次方
&	按位与，二进制位数同且为1结果位为1
l	按位或 ，二进制位数或有1结果位为1
^	按位异或 ，二进制位数不同结果位为1
~	按位取反，二进制位0和1结果位互换

ord 单个字符转整数ascii

chr ascii整数转字符
'''


def to_lower_case(str):
    return ''.join([chr(ord(s) | ord(' ')) for s in str])


def to_upper_case(str):
    return ''.join([chr(ord(s) & ord('_')) for s in str])


def swap_case(str):
    return ''.join([chr(ord(s) ^ ord(' ')) for s in str])


input = "AbcDEF"

# print(to_lower_case(input))
# print(to_upper_case(input))
# print(exchage_upperlower_case(input))


'''
### 二、算法常用操作 n&(n-1)

这个操作是算法中常见的，作用是消除数字 n 的二进制表示中的最后一个 1。

以上便是一些有趣/常用的位操作。其实位操作的技巧很多，有一个叫做 Bit Twiddling Hacks 的外国网站收集了几乎所有位操作的黑科技玩法

一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1：

```cpp
2^0 = 1 = 0b0001
2^1 = 2 = 0b0010
2^2 = 4 = 0b0100
```

'''


#判断一个数是不是 2 的指数
def isPowerOfTwo(n) :
    if (n <= 0) :
        return False
    return (n & (n - 1)) == 0


input = [2,4,6,8,10,16,18]
for i in input:
    print(isPowerOfTwo(i))
