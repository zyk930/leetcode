#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/12 20:28
#@Author  :ZYK
#@FileName: 053_Maximum Subarray.py

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        max_sum = pre_sum = nums[0]
        for i in range(1, len(nums)):
            pre_sum = max(pre_sum+nums[i], nums[i])
            max_sum = max(max_sum, pre_sum)
        return max_sum



print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))