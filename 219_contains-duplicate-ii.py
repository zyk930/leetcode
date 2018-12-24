#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 10:07
# @Author  : zyk

'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len <= 1:
            return False
        nums_dict = {}
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if i-nums_dict[nums[i]] <= k:
                    return True
            nums_dict[nums[i]] = i
            print(nums_dict)
        return False
print(Solution().containsNearbyDuplicate([1,0,1,1],1))