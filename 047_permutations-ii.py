#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 19:52
# @Author  : zyk

'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, path, res, l):
            if len(path) == l:
                return res.append(path)
            else:
                for i in range(len(nums)):
                    if i > 0 and nums[i] == nums[i-1]:
                        continue
                    else:
                        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res, l)
        res = []
        nums.sort()
        dfs(nums, [], res, len(nums))
        return res