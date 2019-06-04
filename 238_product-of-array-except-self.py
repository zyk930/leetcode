#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 15:28
# @Author  : zyk

'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         left = [1] * len(nums)
#         right = [1] * len(nums)
#         res = [1] * len(nums)
#         for i in range(1, len(nums)):
#             left[i] = nums[i-1] * left[i-1]
#             right[-i-1] = nums[-i] * right[-i]
#         for i in range(len(nums)):
#             res[i] = left[i] * right[i]
#         return res


class Solution:
    def productExceptSelf(self, nums):
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i], l = res[i] * l, l * nums[i]
            res[j], r = res[j] * r, r * nums[j]
        return res