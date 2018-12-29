#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 11:21
# @Author  : zyk

'''
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:

输入: 100
输出: "202"
示例 2:

输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7]
'''

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        if num == 0:
            return '0'
        else:
            x = abs(num)
            while x != 0:
                ans += str(x % 7)
                x //= 7

            return ans[::-1] if num>0 else '-'+ans[::-1]


print(Solution().convertToBase7(-7))