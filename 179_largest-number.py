#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 9:46
# @Author  : zyk

'''
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
'''


class Solution(object):
    def cmpFunc(self, a, b):
        if str(a) + str(b) > str(b) + str(a):
            return -1
        elif str(a) + str(b) < str(b) + str(a):
            return 1
        else:
            return 0

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(self.cmpFunc))
        if nums[0] == 0:
            return '0'
        return ''.join(str(num) for num in nums)



print(Solution().largestNumber([3,4,34,5,9]))