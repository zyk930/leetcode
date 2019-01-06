#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/6 20:28
#@Author  :ZYK
#@FileName: 665_non-decreasing-array.py

'''
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:

输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。
'''


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True
        count = 0 if nums[0] <= nums[1] else 1
        for i in range(2, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if count > 1:
                   return False
                if nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i-2]
        return count <= 1


print(Solution().checkPossibility([3, 4, 2, 3]))