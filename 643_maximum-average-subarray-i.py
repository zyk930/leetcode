#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/4 21:54
# @Author  : zyk

'''
给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。

示例 1:

输入: [1,12,-5,-6,50,3], k = 4
输出: 12.75
解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
'''

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = 0
        ans = -float('inf')
        queue = []
        for num in nums:
            queue.append(num)
            total += num
            if len(queue) > k:
                total -= queue.pop(0)
            if len(queue) == k:
                ans = max(ans, float(total) / k)
        return ans