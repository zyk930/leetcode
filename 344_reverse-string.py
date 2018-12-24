#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 9:25
# @Author  : zyk

'''
编写一个函数，其作用是将输入的字符串反转过来。

示例 1:

输入: "hello"
输出: "olleh"
示例 2:

输入: "A man, a plan, a canal: Panama"
输出: "amanaP :lanac a ,nalp a ,nam A"
'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return s[::-1]
        new_strings = []
        index = len(s)
        while index:
            index -= 1
            new_strings.append(s[index])
        return ''.join(new_strings)