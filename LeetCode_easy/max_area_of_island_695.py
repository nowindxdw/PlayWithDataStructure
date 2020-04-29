# -*- coding: utf-8 -*-
'''

深度优先搜索算法（Depth First Search，简称DFS）：一种用于遍历或搜索树或图的算法。

'''


class Solution():
    def max_area_of_island(self,matrix):
        output = 0

        m = len(matrix)
        n = len(matrix[0])

        def dfs(i, j):
            matrix[i][j] = 0 #该坐标已被计算过需要置0避免重复计算
            result = 1
            #对坐标（i,j)的4个方向进行深度优先的遍历
            if i + 1 < m and matrix[i + 1][j]:
                result += dfs(i + 1, j)
            if i - 1 >= 0 and matrix[i - 1][j]:
                result += dfs(i - 1, j)
            if j + 1 < n and matrix[i][j + 1]:
                result += dfs(i, j + 1)
            if j - 1 >= 0 and matrix[i][j - 1]:
                result += dfs(i, j - 1)
            return result

        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    output = max(output, dfs(i, j))
        return output


if __name__ == "__main__":
    input = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],
[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0]
]
    solution=Solution()
    result = solution.max_area_of_island(input)
    print(result)

    input2  =[[0,0,0,0,0,0,0,0]]
    result = solution.max_area_of_island(input)
    print(result)