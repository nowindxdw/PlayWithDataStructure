561.Array Partition I
```
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), …, (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Input: [1,4,3,2]

Output: 4

Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
1
2
3
4
5
Note:

n is a positive integer, which is in the range of [1, 10000].

All the integers in the array will be in the range of [-10000, 10000].
```




566.Reshape the Matrix
```
In MATLAB, there is a very useful function called ‘reshape’, which can reshape a matrix into a new one with different size but keep its original data.

You’re given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the ‘reshape’ operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example1

Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example2

Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

```


485.Max Consecutive Ones
```
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Note:

The input array will only contain 0 and 1.

The length of input array is a positive integer and will not exceed 10,000
```


695. Max Area of Island（python+cpp）
```
Given a non-empty 2D array grid of 0’s and 1’s, an island is a group of 1’s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
Example 1:
[
[0,0,1,0,0,0,0,1,0,0,0,0,0],  
[0,0,0,0,0,0,0,1,1,1,0,0,0], 
[0,1,1,0,1,0,0,0,0,0,0,0,0],  
[0,1,0,0,1,1,0,0,1,0,1,0,0], 
[0,1,0,0,1,1,0,0,1,1,1,0,0],  
[0,0,0,0,0,0,0,0,0,0,1,0,0], 
[0,0,0,0,0,0,0,1,1,1,0,0,0],  
[0,0,0,0,0,0,0,1,1,0,0,0,0]
] 

Given the above grid, return 6. Note the answer is not 11, because the island
must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]] 
Given the above grid, return 0. 
Note: The length of each dimension in the given grid does not exceed 50.
```



448. Find All Numbers Disappeared in an Array
```
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```
LeetCode 198. House Robber

```
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
示例：
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
 ```