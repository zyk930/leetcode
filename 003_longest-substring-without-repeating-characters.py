#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 19:00
# @Author  : zyk

'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = 0
        start = 0
        for i, c in enumerate(s):
            if c in dic:
                start = max(start, dic[c] + 1)
            dic[c] = i
            ans = max(ans, i-start+1)
        return ans


print(Solution().lengthOfLongestSubstring("abba"))