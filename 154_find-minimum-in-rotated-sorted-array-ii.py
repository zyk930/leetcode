#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 10:26
# @Author  : zyk

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

输入: [1,3,5]
输出: 1
示例 2：

输入: [2,2,2,0,1]
输出: 0
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] >= nums[right]:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                left = mid + 1
            elif nums[left] == nums[mid]:
                left += 1
            else:
                right = mid

        return nums[left]

print(Solution().findMin([3,1,3]))