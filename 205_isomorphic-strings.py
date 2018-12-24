#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 20:05
# @Author  : zyk

'''
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(set(s)) != len(set(t)):
        #     return False
        #
        # alp_map = {}
        # for i, alp in enumerate(s):
        #     if alp not in alp_map:
        #         alp_map[alp] = t[i]
        #     else:
        #         if alp_map[alp] != t[i]:
        #             return False
        # return True
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))




print(Solution().isIsomorphic('paper','title'))