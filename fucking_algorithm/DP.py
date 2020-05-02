# -*- coding: utf-8 -*-
'''
动态规划解题套路框架

求解动态规划的核心问题是穷举。

首先，动态规划的穷举有点特别，因为这类问题存在「重叠子问题」，如果暴力穷举的话效率会极其低下，所以需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算。

而且，动态规划问题一定会具备「最优子结构」，才能通过子问题的最值得到原问题的最值

最优子结构性质作为动态规划问题的必要条件，一定是让你求最值

只有列出正确的「状态转移方程」才能正确地穷举。

带备忘录的动态规划方法叫做「自顶向下」，而dp table动态规划叫做「自底向上」,其本质都是一样的。

'''


# 最长递增子序列（Longest Increasing Subsequence，简写 LIS）是比较经典的
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.
    Follow up: Could you improve it to O(nlogn) time complexity?

给定未排序的整数数组，找到最长的增加子序列的长度。

注意：

    可能有多个LIS组合，只需要您返回长度。
    您的算法应该以O（n 2）复杂度运行。
    跟进：你能把它提高到O（nlogn）时间复杂度吗？
'''

#一、动态规划解法

#动态规划的核心设计思想是数学归纳法
#我们的定义是这样的：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度。
#根据这个定义，我们的最终结果（子序列的最大长度）应该是 dp 数组中的最大值。
'''
result = max(dp)
'''
#d我们可以假设 dp[0...i-1] 都已经被算出来了，然后怎么通过这些结果算出 dp[i]
'''java
for (int j = 0; j < i; j++) {
    if (nums[i] > nums[j]) 
        dp[i] = Math.max(dp[i], dp[j] + 1);
}
'''
'''python
for j in range(0,i):
    if nums[i]>nums[j]:
        dp[i] = max(dp[i],dp[j]+1)
'''


#完整代码如下,时间复杂度为O(n^2)：
def length_LIS(nums):
    dp = [1]*len(nums)  #初始化dp table, 注意这里最小子序列就是自身,故初始化为1,另一些题目中可能需要初始化为不同值
    # print(dp)
    for i in range(len(nums)):
        # print(i)
        for j in range(0, i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    result = max(dp)
    print(result)


input = [10,9,2,5,3,7,101,18]
length_LIS(input)



#二分查找解法
'''
最长递增子序列和一种叫做 patience game 的纸牌游戏有关，甚至有一种排序方法就叫做 patience sorting（耐心排序）
只能把点数小的牌压到点数比它大的牌上。如果当前牌点数较大没有可以放置的堆，则新建一个堆，把这张牌放进去。如果当前牌有多个堆可供选择，则选择最左边的堆放置
按照上述规则执行，可以算出最长递增子序列，牌的堆数就是最长递增子序列的长度
按此定义我们得到的牌堆为


10  5   7 *  101  
      *
9   3         18
   *
2
最长递增序列则如*连接给出

'''


#时间复杂度同二分查找O(nlogn)
def binary_sort_for_LIS(nums):
    piles = 0
    nlen = len(nums)
    top = [0]*nlen
    for i in range(nlen):
        card = nums[i]
        left = 0
        right = piles
        while(left<right):
            mid = left+(right-left)//2
            if top[mid]> card:
                right =mid
            elif top[mid]< card:
                left = mid+1
            else:
                right = mid
        if left == piles:#没找到合适的牌堆，新建一堆
            piles += 1
        top[left] = card #把这张牌放到牌堆顶
    #牌堆数就是LIS长度
    return piles


# print(binary_sort_for_LIS(input))


"""
来说一下背包问题吧，就讨论最常说的 0-1 背包问题。描述：
给你一个可装载重量为 W 的背包和 N 个物品，每个物品有重量和价值两个属性。其中第 i 个物品的重量为 wt[i]，价值为 val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

一个典型的动态规划问题。这个题目中的物品不可以分割，要么装进包里，要么不装，不能说切成两块装一半。这就是 0-1 背包这个名词的来历。

第一步要明确两点，「状态」和「选择」。
先说状态，如何才能描述一个问题局面？只要给几个物品和一个背包的容量限制，就形成了一个背包问题呀。所以状态有两个，就是「背包的容量」和「可选择的物品」。
再说选择，也很容易想到啊，对于每件物品，你能选择什么？选择就是「装进背包」或者「不装进背包」嘛。
明白了状态和选择，动态规划问题基本上就解决了，只要往这个框架套就完事儿了

for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 择优(选择1，选择2...)
            
第二步要明确 dp 数组的定义。
首先看看刚才找到的「状态」，有两个，也就是说我们需要一个二维 dp 数组。
根据这个定义，我们想求的最终答案就是 dp[N][W]。base case 就是 dp[0][..] = dp[..][0] = 0，因为没有物品或者背包没有空间的时候，能装的最大价值就是 0。

int dp[N+1][W+1]
dp[0][..] = 0
dp[..][0] = 0

for i in [1..N]:
    for w in [1..W]:
        dp[i][w] = max(
            把物品 i 装进背包,
            不把物品 i 装进背包
        )
return dp[N][W]

第三步，根据「选择」，思考状态转移的逻辑。
如果你没有把这第 i 个物品装入背包，那么很显然，最大价值 dp[i][w] 应该等于 dp[i-1][w]，继承之前的结果。
如果你把这第 i 个物品装入了背包，那么 dp[i][w] 应该等于 dp[i-1][w - wt[i-1]] + val[i-1]

"""
'''
dp    W=0 W=1 w=2 w=3 w=4
N=0   0   0   0   0  0
N=1   0   0   4   4  4
N=2   0   2   4   6  6
N=3   0   2   4   6  6
'''


def knapsack(W, N,wt,val):
    #初始化一个表示状态的W*N的数组dp table,默认值为0
    # 不可用append赋值二维数组
    #出现这个结果的原因是：list * n—>n shallow copies of list concatenated, n个list的浅拷贝的连接 修改其中的任何一个元素会改变整个列表，
    dp = [([0] *(W+1)) for i in range(N+1)]
    #遍历所有可能状态
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j - wt[i-1]<0: #重量不能为负数，因此不装入背包
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-wt[i-1]]+val[i-1],dp[i-1][j])
    print(dp)
    return dp[N][W]



N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]

knapsack(W,N,wt,val)

