#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 21:42
# @Author  : zyk

'''
给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。

这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_lst = str.split()
        a = zip(pattern, str_lst)
        return len(pattern) == len(str_lst) and len(set(pattern)) == len(set(a)) == len(set(str_lst))




print(Solution().wordPattern('abba', 'dog dog dog dog'))