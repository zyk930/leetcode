#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:20
# @Author  : zyk

'''
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
'''


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s+s)[1:-1].find(s) != -1

print(Solution().repeatedSubstringPattern("abcabcabcabc"))