#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 20:21
# @Author  : zyk

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [i for i in range(-1, len(s))]
        is_palindrome = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[i-1] == s[j] and (i - j <= 2 or is_palindrome[j+1][i-1]):
                    is_palindrome[j][i] = True
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[-1]


print(Solution().minCut("aabac"))