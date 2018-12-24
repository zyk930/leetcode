#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 18:36
# @Author  : zyk

'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def count(str):
            dic = {}
            for s in str:
                if s not in dic:
                    dic[s] = 1
                else:
                    dic[s] += 1

            return dic
        dic_s = count(s)

        dic_t = count(t)
        return dic_s == dic_t

print(Solution().isAnagram("anagram", "nagaram"))