# -*- coding: utf-8 -*-
'''
寻找丢失的数
先对已知长度数组去重，然后构建1～n完全数组求差集
'''


class Solution():
    def find_dispeared_nums(self,input):
        distinct = set(input)
        comlete_list = set([i+1 for i in range(len(input))])
        output = comlete_list.difference(distinct)
        return list(output)


if __name__ == "__main__":
    input =  [4,3,2,7,8,2,3,1]
    solution=Solution()
    result = solution.find_dispeared_nums(input)
    print(result)
