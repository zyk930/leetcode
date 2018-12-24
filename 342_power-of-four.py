#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 10:30
# @Author  : zyk

'''
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
'''

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num-1) == 0 and num & 0x55555555 != 0
print(Solution().isPowerOfFour(16))