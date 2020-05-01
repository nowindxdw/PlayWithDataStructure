# -*- coding: utf-8 -*-
'''

对于比较小的数字，做运算可以直接使用编程语言提供的运算符，但是如果相乘的两个因数非常大，语言提供的数据类型可能就会溢出。
一种替代方案就是，运算数以字符串的形式输入，然后模仿我们小学学习的乘法算术过程计算出结果，并且也用字符串表示。
在Python中，整数的值不受位数的限制，可以扩展到可用内存的限制。因此，我们永远不需要任何特殊的安排来存储大数字（想象一下在C / C ++中进行上述算术）。
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                temp = int(num1[i]) * int(num2[j])
                res[i+j+1] += temp % 10
                res[i+j] += temp // 10
        for i in range(len(res)-1, -1, -1):
            if int(res[i]) > 9:
                res[i-1] += res[i] // 10
                res[i] = res[i] % 10
        res = ''.join([str(s) for s in res]).lstrip('0') #结果前缀可能存的 0（未使用的位）
        if not res:
            return '0'
        return res

num1 = 123456789987654321
num2 = 987654321123456678899
print(num1*num2)


result = Solution().multiply(str(num1),str(num2))
print(result)