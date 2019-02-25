#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/19 17:38
# @Author  : zyk

'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans = [[0] * n for _ in range(n)]
        left, right, up, down = 0, n-1, 0, n-1
        k = 1
        while left <= right and up <= down:
            for i in range(left, right+1):
                ans[up][i] = k
                k += 1
            up += 1
            for i in range(up, down+1):
                ans[i][right] = k
                k += 1
            right -= 1
            for i in reversed(range(left, right+1)):
                ans[down][i] = k
                k += 1
            down -= 1
            for i in reversed(range(up, down+1)):
                ans[i][left] = k
                k+= 1
            left += 1
        return ans

print(Solution().generateMatrix(3))