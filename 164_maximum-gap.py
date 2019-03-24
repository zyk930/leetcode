#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/24 16:49
#@Author  :ZYK
#@FileName: 164_maximum-gap.py

'''
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
'''


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        a, b = min(nums), max(nums)
        if a == b:
            return 0
        size = (b - a) // (len(nums) - 1) or 1
        buckets = [[None, None] for _ in range((b - a) // size + 1)]
        for num in nums:
            bucket = buckets[(num - a) // size]
            bucket[0] = num if bucket[0] is None else min(bucket[0], num)
            bucket[1] = num if bucket[1] is None else max(bucket[1], num)
        buckets = [bucket for bucket in buckets if bucket[0] is not None]
        ans = 0
        for i in range(1, len(buckets)):
            ans = max(ans, buckets[i][0] - buckets[i-1][1])
        return ans
print(Solution().maximumGap([3,6,9,1]))