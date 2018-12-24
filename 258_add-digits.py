#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 20:05
# @Author  : zyk

'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # while num > 9:
        #     sum = 0
        #     while num > 0:
        #         sum += num % 10
        #         num = num // 10
        #
        #     num = sum
        # return num
        if num == 0:
            return 0
        return 1 + (num - 1) % 9



print(Solution().addDigits(2))