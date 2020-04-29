# -*- coding: utf-8 -*-
'''
最大连续数

遍历目标数组，并计数，时间复杂度O(n)
注意处理末尾为1和0的情况
'''


class Solution():
    def max_consecutive(self,input):
        max_num = 0
        temp = 0
        for i in input:
            if i == 1:
                temp+=1
            else:
                max_num =max(temp,max_num)
                temp =0
        return max(max_num,temp)


if __name__ == "__main__":
    input =  [1,1,0,1,1,1]
    solution=Solution()
    result = solution.max_consecutive(input)
    print(result)
