#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/17 10:14
#@Author  :ZYK
#@FileName: 136_single-number.py

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #按位或
        ans = 0
        for i in range(len(nums)):
            ans = ans^nums[i]
        return ans

print(Solution().singleNumber([4,1,2,1,2]))