# -*- coding: utf-8 -*-
"""
栈（stack）是很简单的一种数据结构，先进后出的逻辑顺序，符合某些问题的特点，比如说函数调用栈。

单调栈实际上就是栈，只是利用了一些巧妙的逻辑，使得每次新元素入栈后，栈内的元素都保持有序（单调递增或单调递减）。

听起来有点像堆（heap）？不是的，单调栈用途不太广泛，只处理一种典型的问题，叫做 Next Greater Element。

本文用讲解单调队列的算法模版解决这类问题，并且探讨处理「循环数组」的策略。

首先，讲解 Next Greater Number 的原始问题：给你一个数组，返回一个等长的数组，对应索引存储着下一个更大元素，如果没有更大的元素，就存 -1。不好用语言解释清楚，直接上一个例子：

给你一个数组 [2,1,2,4,3]，你返回数组 [4,2,4,-1,-1]。

解释：第一个 2 后面比 2 大的数是 4; 1 后面比 1 大的数是 2；第二个 2 后面比 2 大的数是 4; 4 后面没有比 4 大的数，填 -1；3 后面没有比 3 大的数，填 -1。

这道题的暴力解法很好想到，就是对每个元素后面都进行扫描，找到第一个更大的元素就行了。但是暴力解法的时间复杂度是 O(n^2)。

这个问题可以这样抽象思考：把数组的元素想象成并列站立的人，元素大小想象成人的身高。这些人面对你站成一列，如何求元素「2」的 Next Greater Number 呢？很简单，如果能够看到元素「2」，那么他后面可见的第一个人就是「2」的 Next Greater Number，因为比「2」小的元素身高不够，都被「2」挡住了，第一个露出来的就是答案。
"""

#暴力破解
def next_greater_number(input):
    output = []
    for i in range(len(input)):
        for j in range(i+1,len(input)):
                if input[j]>input[i]:
                    output.append(input[j])
                    break
        else:
            output.append(-1)
    return output


def next_greater_number_by_stack(input):
    answers = []
    stack = []
    # 倒着遍历
    for i in input[::-1]:
        print(i)
        while(len(stack)!=0 and stack[-1]<=i): #判定哪个更大
            stack.pop()                        #更小的数直接踢出
        answers.insert(0,(-1 if len(stack)==0 else stack[-1]))# 为保证输出顺序，使用头插法，效率更高的是输出前 answer.reverse()
        stack.append(i)
    return answers


input =  [2,1,2,4,3]
# output = next_greater_number(input)
# print(output)

# result = next_greater_number_by_stack(input)
# print(result)


"""
继续看一个变形：
给你一个数组 T = [73, 74, 75, 71, 69, 72, 76, 73]，这个数组存放的是近几天的天气气温（这气温是铁板烧？不是的，这里用的华氏度）。
你返回一个数组，计算：对于每一天，你还要至少等多少天才能等到一个更暖和的气温；如果等不到那一天，填 0 。
"""

def next_greater_temperature_by_stack(input):
    answers = []
    stack = []
    # 倒着遍历
    print(len(input))
    index_order = range(len(input))
    for i in reversed(index_order):
        print(i)
        while(len(stack)!=0 and input[stack[-1]]<=input[i]): #判定哪个更大
            stack.pop()                        #更小的数直接踢出
        answers.insert(0,(0 if len(stack)==0 else stack[-1]-i))# 为保证输出顺序，使用头插法，效率更高的是输出前 answer.reverse()
        stack.append(i)
    return answers

# input_T =  [73, 74, 75, 71, 69, 72, 76, 73]
# result = next_greater_temperature_by_stack(input_T)
# print(result)

"""
单调栈讲解完毕。下面开始另一个重点：如何处理「循环数组」。

同样是 Next Greater Number，现在假设给你的数组是个环形的，如何处理？

给你一个数组 [2,1,2,4,3]，你返回数组 [4,2,4,-1,4]。拥有了环形属性，最后一个元素 3 绕了一圈后找到了比自己大的元素 4 。

![ink-image](../pictures/%E5%8D%95%E8%B0%83%E6%A0%88/2.png)


首先，计算机的内存都是线性的，没有真正意义上的环形数组，但是我们可以模拟出环形数组的效果，一般是通过 % 运算符求模（余数），获得环形特效：

```java
int[] arr = {1,2,3,4,5};
int n = arr.length, index = 0;
while (true) {
    print(arr[index % n]);
    index++;
}
```

怎么实现呢？你当然可以把这个双倍长度的数组构造出来，然后套用算法模板。但是，我们可以不用构造新数组，而是利用循环数组的技巧来模拟
"""
def nextGreaterElementCircle(input):
    n = len(input)
    answers = [0 for i in range(n)]
    stack = []
    # 倒着遍历
    # print(len(input))
    index_order = range(2*n)
    for i in reversed(index_order):
        # print("i=" + str(i))
        # print("i%n=" +str(i%n))
        # print("inpurt[i%n]=" + str(input[i%n]))
        while(len(stack)!=0 and stack[-1]<=input[i%n]): #判定哪个更大
            stack.pop()                        #更小的数直接踢出
        # print("while stack=%s" % stack)
        answers[i%n]= -1 if len(stack)==0 else stack[-1]#
        stack.append(input[i%n])
        # print("answers=%s" % answers)
        # print("stack=%s" % stack)
    return answers

input =  [2,1,2,4,3]
output = nextGreaterElementCircle(input)
print(output)