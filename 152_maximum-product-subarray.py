#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 17:19
# @Author  : zyk

'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        maxdp = [0] * len(nums)
        mindp = [0] * len(nums)
        maxdp[0] = nums[0]
        mindp[0] = nums[0]
        for i in range(1, len(nums)):
            maxdp[i] = max(maxdp[i-1] * nums[i], mindp[i-1] * nums[i], nums[i])
            mindp[i] = min(maxdp[i-1] * nums[i], mindp[i-1] * nums[i], nums[i])
            ans = max(ans, maxdp[i])
        return ans

print(Solution().maxProduct([2,3,-2,4]))