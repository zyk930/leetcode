#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:20
# @Author  : zyk

'''
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
'''

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0

    #由于输入是int，正数范围是0-2^31，在此范围中允许的最大的3的次方数为3^19=116226146