#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 20:04
# @Author  : zyk

'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        ans = []
        left, up, right, down = 0, 0, len(matrix[0])-1, len(matrix)-1
        while left <= right and up <= down:
            for i in range(left, right + 1):
                ans.append(matrix[up][i])
            up += 1
            for i in range(up, down + 1):
                ans.append(matrix[i][right])
            right -= 1
            for i in reversed(range(left, right + 1)):
                ans.append(matrix[down][i])
            down -= 1
            for i in reversed(range(up, down + 1)):
                ans.append(matrix[i][left])
            left += 1
        return ans[:len(matrix)*len(matrix[0])]


a = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(a))