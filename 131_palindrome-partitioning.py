#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/14 15:20
# @Author  : zyk

'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return 0
        else:
            res = []
            self.helper(s, [], res)
            return res

    def helper(self, s, path, res):
        if len(s) == 0:
            res.append(path)
        for i in range(1, len(s)+1):
            if self.ispartition(s[:i]):
                self.helper(s[i:], path + [s[:i]], res)

    def ispartition(self, s):
        if len(s) == 0:
            return False
        start = 0
        end = len(s) - 1
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True



print(Solution().partition("aab"))
