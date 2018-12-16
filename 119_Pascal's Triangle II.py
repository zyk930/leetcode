#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/16 17:51
#@Author  :ZYK
#@FileName: 119_Pascal's Triangle II.py

'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 3
输出: [1,3,3,1]
进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
'''


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # rowIndex += 1
        # ans = [[1] * n for n in range(1, rowIndex + 1)]
        # if rowIndex > 2:
        #     for i in range(2, rowIndex):
        #         for j in range(1, i):
        #             ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        # return ans[-1]

        fact = [1] * (rowIndex + 1)
        ans = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            fact[i] = fact[i - 1] * i
        for i in range(1, rowIndex):
            ans[i] = fact[-1] / (fact[i] * fact[rowIndex - i])
        return ans

# C(k,n) = n!/k!*(n-k)!

print(Solution().getRow(4))