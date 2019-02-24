#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/24 20:30
#@Author  :ZYK
#@FileName: 073_set-matrix-zeroes.py

'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_zero = False
        col_zero = False
        for i in matrix[0]:
            if i == 0:
                row_zero = True
        for j in range(rows):
            if matrix[j][0] == 0:
                col_zero = True

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                matrix[row] = [0] * cols

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        if row_zero:
            matrix[0] = [0] * cols

        if col_zero:
            for row in range(rows):
                matrix[row][0] = 0

        # rows = len(matrix)
        # columns = len(matrix[0])
        #
        # row_index = []
        # column_index = []
        #
        # for row in range(rows):
        #     for column in range(columns):
        #         if matrix[row][column] == 0:
        #             row_index.append(row)
        #             column_index.append(column)
        #
        # for r in row_index:
        #     matrix[r] = [0] * columns
        # for c in column_index:
        #     for r in range(rows):
        #         matrix[r][c] = 0

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]

Solution().setZeroes(matrix)
print(matrix)