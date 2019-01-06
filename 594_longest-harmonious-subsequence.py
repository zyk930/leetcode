#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/3 16:43
#@Author  :ZYK
#@FileName: 594_longest-harmonious-subsequence.py

'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
'''


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Map = {}
        ans = 0
        for i in nums:
            Map[i] = Map.get(i, 0) + 1
        for x in Map:
            if x + 1 in Map:
                ans = max(ans, Map[x] + Map[x + 1])
        return ans

print(Solution().findLHS([1,3,2,2,5,2,3,7]))