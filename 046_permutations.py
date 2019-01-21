#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 17:08
# @Author  : zyk

'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(nums, path, res, l):
            if len(path) == l:
                return res.append(path)
            else:
                for i in range(len(nums)):
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res, l)

        res = []
        dfs(nums, [], res, len(nums))
        return res

print(Solution().permute([1,2,3]))