#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/18 21:13
#@Author  :ZYK
#@FileName: 057_insert-interval.py

'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        ans = []
        for i in sorted(intervals, key=lambda x: x.start):
            if ans and ans[-1].end >= i.start:
                ans[-1].end = max(ans[-1].end, i.end)
            else:
                ans.append(i)

        return ans

'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s, e = newInterval.start, newInterval.end
        left = filter(lambda x: x.end < s, intervals)
        right = filter(lambda x: x.start > e, intervals)
        if left + right != intervals:
            s = min(intervals[len(left)].start, s)
            e = max(intervals[len(intervals) - len(right) - 1].end, e)
        return left + [Interval(s, e)] + right
'''