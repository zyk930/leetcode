#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 20:53
# @Author  : zyk

'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5


示例2:

输入: 3
输出: False
'''


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        start = 0
        end = int(c ** 0.5)
        print(end)
        while start <= end:
            mid = start ** 2 + end ** 2
            if mid == c:
                return True
            elif mid < c:
                start += 1
            else:
                end -= 1
        return False


print(Solution().judgeSquareSum(2))