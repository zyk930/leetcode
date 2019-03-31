#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/30 23:38
#@Author  :ZYK
#@FileName: 213_house-robber-ii.py


'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [2,3,2]
输出: 3
解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2:

输入: [1,2,3,1]
输出: 4
解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) <= 3:
            return max(nums)
        else:
            dp_1, dp_2 = [0] * (len(nums) - 1), [0] * (len(nums) - 1)
            dp_1[0] = nums[0]
            dp_1[1] = max(nums[0], nums[1])
            for i in range(2, len(nums) - 1):
                dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + nums[i])
            dp_2[0] = nums[1]
            dp_2[1] = max(nums[1], nums[2])
            for i in range(2, len(nums) - 1):
                dp_2[i] = max(dp_2[i - 1], dp_2[i - 2] + nums[i + 1])

            return max(dp_1[-1], dp_2[-1])