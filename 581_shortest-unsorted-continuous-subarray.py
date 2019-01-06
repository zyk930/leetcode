#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/3 15:57
#@Author  :ZYK
#@FileName: 581_shortest-unsorted-continuous-subarray.py

'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。
'''


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy = nums[:]
        copy.sort()
        i = 0
        j = len(nums)-1
        while i < len(nums) and copy[i] == nums[i]:
            i += 1
        while j > i and copy[j] == nums[j]:
            j -= 1
        return j - i + 1

print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))