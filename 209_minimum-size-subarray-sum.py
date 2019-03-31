#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/29 21:36
#@Author  :ZYK
#@FileName: 209_minimum-size-subarray-sum.py

'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例:

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = float('inf')
        j = 0
        sum = 0
        for i in range(len(nums)):
            while j < len(nums) and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                ans = min(ans, j - i)
            sum -= nums[i]
        return ans if ans != float('inf') else 0



print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))