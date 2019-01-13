#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/12 21:31
#@Author  :ZYK
#@FileName: 016_3sum-closest.py

'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = float('inf')
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum > target:
                    if abs(sum-target) < diff:
                        diff = abs(sum-target)
                        ans = sum
                    end -= 1
                else:
                    if abs(sum-target) < diff:
                        diff = abs(sum-target)
                        ans = sum
                    start += 1
        return ans

print(Solution().threeSumClosest([-1, 2, 1,-4],2))