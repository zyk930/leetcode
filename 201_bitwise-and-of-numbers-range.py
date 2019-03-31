#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/29 14:54
#@Author  :ZYK
#@FileName: 201_bitwise-and-of-numbers-range.py

'''
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1:

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i
print(Solution().rangeBitwiseAnd(5,7))