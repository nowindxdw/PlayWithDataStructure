# -*- coding: utf-8 -*-
'''
283. Move Zeroes

Given an array nums, write a function to move all 0’s to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

You must do this in-place without making a copy of the array.

Minimize the total number of operations.

'''


class Solution():
    #普通解法：把所有非0元素移动到数组最前面，剩下位置填充0 需要2个非嵌套For循环遍历N次复杂度O(n)
    def move_zeros_normal(self,nums):
        j = 0
        nums_size = len(nums)
        for i in range(nums_size):
            if nums[i]!=0:
                nums[j] = nums[i]
                j += 1
        for n in range(j,nums_size):
            nums[n] = 0
        return nums

    #利用sort函数的高级用法，一行解决问题，技巧性太强，不特别推荐
    def move_zeros_advance(self,nums):
        nums.sort(key=bool, reverse=True)
        return nums


if __name__ == "__main__":
    input = [0, 1, 0, 3, 12]
    solution=Solution()
    result = solution.move_zeros_normal(input)
    print(result)

