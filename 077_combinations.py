#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 16:46
# @Author  : zyk

'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        elif n == k:
            return [[i for i in range(1, n+1)]]
        else:
            l = self.combine(n-1, k)
            part = self.combine(n-1, k-1)
            for p in part:
                p += [n]
            l += part
            return l

print(Solution().combine(4, 2))