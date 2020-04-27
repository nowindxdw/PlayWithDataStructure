# -*- coding: utf-8 -*-
'''
直接思考若不易得出排序取偶数结论

不妨用归纳思想，先假设数字4个
1，2，3，4 要取最大和无论4和谁比较，都不会拿到4，为了拿次大的必须拿3
那顺序确定为（3,4）(1,2)
再增加一对更大的数
1,2,3,4,n, n+m(n>4）同理则为（n,n+m）(3,4)(1,2)
再增加n对值同理可知是按顺序排列下来成对组合

排序时间复杂度为O(nlogn)
'''


class Solution():
    def array_pair_sum(self,nums):
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    input = [1,4,3,2]
    solution=Solution()
    result = solution.array_pair_sum(input)
    print(result)

