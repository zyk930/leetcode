#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/11 20:42
#@Author  :ZYK
#@FileName: 005_longest-palindromic-substring.py

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        start, maxl = 0, 0
        for i in range(n):
            print(i)
            print(maxl)
            print('---')
            if i - maxl >= 1 and s[i-maxl-1:i+1] == s[i-maxl-1:i+1][::-1]:
                start = i-maxl-1
                maxl += 2
            elif i - maxl >= 0 and s[i-maxl:i+1] == s[i-maxl:i+1][::-1]:
                start = i-maxl
                maxl += 1
        return s[start:start+maxl]

print(Solution().longestPalindrome("dabad"))