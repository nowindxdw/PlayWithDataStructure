# -*- coding: utf-8 -*-
'''
717. 1-bit and 2-bit Characters

We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:

Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:

Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:

1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.


'''


class Solution():
    #按照题意，给定的元素只能是0,10,11,而且最后一位必须是0
    #从头开始遍历直到倒数第二位（最后一位必然是0），遇到0 j+=1遇到1 j+=2 最后判断j和len(nums)-1就是结果
    def is_one_bit_character(self,nums):
        j = 0
        nums_size = len(nums)
        while j < nums_size-1:
            j = j + 1 if nums[j] == 0 else j + 2
        # print(j)
        return j == nums_size-1


if __name__ == "__main__":
    input =  [1, 1, 1, 0]
    solution=Solution()
    result = solution.is_one_bit_character(input)
    print(result)

    # 生成位数为n的0-1随机数组方法如下
    import random
    n = 10
    list = [random.randint(0,1) for i in range(n-1)]
    list.append(0)
    print(list)

