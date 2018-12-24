#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 10:29
# @Author  : zyk

'''
不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1
'''

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return sum([a,b])
        no_carry_sum=a^b#a与b不进位时的和，恰好与异或性质一样
        carry=(a&b)<<1#a与b的和的进位，恰好是或操作再左移位
        return sum([no_carry_sum,carry])#前两者之和