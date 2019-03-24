#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/24 17:50
#@Author  :ZYK
#@FileName: 166_fraction-to-recurring-decimal.py

'''
如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"
'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans += str(numerator // denominator)
        if numerator % denominator:
            ans += '.'
        else:
            return ans
        numerator = (numerator % denominator) * 10
        d = {}
        res = []
        while True:
            if numerator in d:
                idx = d[numerator]
                return ans + ''.join(res[:idx]) + '(' + ''.join(res[idx:]) + ')'
            r = numerator % denominator
            v = numerator // denominator
            res.append(str(v))
            d[numerator] = len(res) - 1
            if r == 0:
                return ans + ''.join(res)
            numerator = r * 10

print(Solution().fractionToDecimal(2,3))