#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 19:00
# @Author  : zyk

'''
对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False



示例：

输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14


注意:

输入的数字 n 不会超过 100,000,000. (1e8)
'''


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        factor = []
        i = 1
        while i * i <= num:
            if num % i == 0:
                factor.append(i)
                j = num // i
                if j != num:
                    factor.append(j)
            i += 1

        return num == sum(factor)


print(Solution().checkPerfectNumber(28))