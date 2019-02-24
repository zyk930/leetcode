#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/18 19:59
#@Author  :ZYK
#@FileName: 056_merge-intervals.py

'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for i in sorted(intervals, key=lambda x: x.start):
            if ans and ans[-1].end >= i.start:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)

        return ans