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


