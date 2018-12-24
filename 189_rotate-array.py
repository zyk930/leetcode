#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 16:58
# @Author  : zyk

'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
'''

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def reverse(start, end, s):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        n = len(nums)-1
        k = k%len(nums)
        reverse(0, n-k, nums)
        reverse(n-k+1, n, nums)
        reverse(0, n, nums)
        return  nums

print(Solution().rotate([1,2,3,4,5,6,7],3))