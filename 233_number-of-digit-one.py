#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 10:41
# @Author  : zyk

'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
'''


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        m = 1
        while m <= n:
            r = (n / m) % 10
            if r > 1:
                ans += m
            elif r == 1:
                ans += n % m + 1

            ans += (n / (m * 10)) * m
            m *= 10
        return ans



