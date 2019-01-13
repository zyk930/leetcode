#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 9:30
# @Author  : zyk


'''
集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

示例 1:

输入: nums = [1,2,2,4]
输出: [2,3]
注意:

给定数组的长度范围是 [2, 10000]。
给定的数组是无序的。
'''


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        # dic = {}
        # for num in nums:
        #     dic[num] = dic.get(num, 0) + 1
        # for i in range(1, n+1):
        #     if i in dic and dic[i] == 2:
        #         a = i
        #     if i not in dic:
        #         b = i
        # return [a, b]
        ori = (1 + n) * n // 2
        now = sum(set(nums))
        b  = ori - now
        total = sum(nums)
        a = total - now
        return [a, b]




print(Solution().findErrorNums([1,2,2,4]))