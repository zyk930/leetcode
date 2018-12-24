#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 9:33
# @Author  : zyk

'''
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"
说明:
元音字母不包含字母"y"。
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        alp_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] not in alp_list:
                start += 1
            elif s[end] not in alp_list:
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        return ''.join(s)

print(Solution().reverseVowels('leetcode'))