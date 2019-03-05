#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:29
# @Author  : zyk

'''
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例:

输入:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
输出: 6
'''


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        def largestRectangleArea(heights):
            """
            :type heights: List[int]
            :rtype: int
            """
            if not heights:
                return 0
            stack = []
            ans = 0
            heights.append(0)
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    ans = max(ans, h * w)
                stack.append(i)
            return ans

        ans = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            if i == 0:
                dp[i] = [int(h) for h in matrix[i]]
            else:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == '1':
                        dp[i][j] = dp[i-1][j] + 1
            ans = max(ans, largestRectangleArea(dp[i]))
        return ans



a = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(Solution().maximalRectangle(a))