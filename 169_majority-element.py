#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 16:22
# @Author  : zyk

'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         dic[i] += 1
        #     else:
        #         dic[i] = 1
        # for n in dic:
        #     if dic[n] > len(nums)//2:
        #         return n
        return sorted(nums)[len(nums) // 2]


print(Solution().majorityElement([2,2,1,1,1,2,2]))