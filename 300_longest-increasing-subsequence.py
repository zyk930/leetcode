#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 9:33
# @Author  : zyk

'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

# class Solution(object):
#     def lengthOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dp = [1] * len(nums)
#         res = 0
#         for i in range(0, len(nums)):
#             for j in range(0, i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#             res = max(res, dp[i])
#         return res

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        if not nums:
            return 0
        ans.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                position = self.binary_search(ans, nums[i], 0, len(ans))
                ans[position] = nums[i]
        return len(ans)

    def binary_search(self, ans, num, start, end):
        if start == end:
            return start
        while start < end:
            mid = (start + end) // 2
            if mid == start:
                if ans[start] < num:
                    return end
                else:
                    return start
            if num < ans[mid]:
                return self.binary_search(ans, num, start, mid)
            else:
                return self.binary_search(ans, num, mid, end)