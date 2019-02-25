#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 16:16
# @Author  : zyk

'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
'''


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            if not n:
                return 1
            res = 1
            for i in range(1, n+1):
                res *= i
            return res

        visited = [0 for _ in range(n)]
        fact = [factorial(n-1-i) for i in range(n)]
        ans = ""
        k -= 1
        for i in range(n):
            t = k // fact[i]
            for j in range(n):
                if not visited[j]:
                    if t == 0:
                        break
                    t -= 1
            ans += str(j + 1)
            k %= fact[i]
            visited[j] = 1
        return ans


print(Solution().getPermutation(4,9))