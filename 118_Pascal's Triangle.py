#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/16 17:16
#@Author  :ZYK
#@FileName: 118_Pascal's Triangle.py

'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
  def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    ans = [[1] * n for n in range(1, numRows+1)]
    if numRows > 2:
        for i in range(2, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    return ans
print(Solution().generate(4))