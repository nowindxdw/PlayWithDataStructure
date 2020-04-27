# -*- coding: utf-8 -*-
'''
矩阵的重排问题
先将输入转为1维，再比较输入维度,若维度不合理，返回原值，若合理则截取对应长度数组组成新数组
时间复杂度为输入矩阵的row值O(n)和目标r值O(r),总复杂度为线性级别
'''


class Solution():
    def reshape_matrix(self,matrix,r,c):
        list_length = 0
        vec = []
        output = []
        for i in range(len(matrix)):
            list_length += len(matrix[i])
            vec += matrix[i]
        if r * c > list_length:
            output = matrix
        else:
            for each in range(r):
                output.append(vec[each * c:(each + 1) * c])

        return output


if __name__ == "__main__":
    input = [[1,2], [3,4]]
    solution=Solution()
    result = solution.reshape_matrix(input,1,4)
    print(result)

    input = [[1,2], [3,4]]
    solution=Solution()
    result = solution.reshape_matrix(input,2,4)
    print(result)
