#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/16 12:42
#@Author  :ZYK
#@FileName: 034_find-first-and-last-position-of-element-in-sorted-array.py

'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        found = 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                if target == nums[mid]:
                    found += 1
                right = mid - 1
        if nums[left] == target:
            found += 1

        start = right
        if right < 0 or nums[start] != target:
            start += 1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            else:
                if target == nums[mid]:
                    found += 1
                left = mid + 1
        end = left
        if nums[end] != target:
            end -= 1
        if found == 0:
            return [-1, -1]
        else:
            return [start, end]




print(Solution().searchRange([1],1))