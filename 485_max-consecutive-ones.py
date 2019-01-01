#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/28 23:44
#@Author  :ZYK
#@FileName: 485_max-consecutive-ones.py

'''
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。
'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 0
        ans = max(ans, count)
        return ans

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))