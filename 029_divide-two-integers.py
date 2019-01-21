#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/15 10:25
# @Author  : zyk

'''
示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans = 0
        sign = 1 if dividend * divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        subsum = divisor
        cnt = 1
        while divisor <= dividend:
            while (subsum << 1) <= dividend:
                cnt <<= 1
                subsum <<= 1
            ans += cnt
            cnt = 1
            dividend -= subsum
            subsum = divisor

        return max(min(sign * ans, 2147483647), -2147483648)

print(Solution().divide(7, -2))