#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 16:52
# @Author  : zyk

'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        m = {}
        res = 0
        for i in nums:
            if i not in m:
                l = 0
                r = 0
                if i - 1 in m:
                    l = m[i - 1]
                if i + 1 in m:
                    r = m[i + 1]
                m[i] = 1 + r + l
                m[i - l] = 1 + r + l
                m[i + r] = 1 + r + l
                res = max(res, m[i])
        return res
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))