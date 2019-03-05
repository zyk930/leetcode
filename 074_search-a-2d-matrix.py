#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 10:44
# @Author  : zyk

'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        if matrix[0][0] == target or matrix[m - 1][n - 1] == target:
            return True
        start, end = 0, m * n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid // n][mid % n] < target:
                start = mid
            elif matrix[mid // n][mid % n] > target:
                end = mid
            else:
                return True

        return False

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 4
print(Solution().searchMatrix(matrix, target))