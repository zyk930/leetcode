#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 16:36
# @Author  : zyk

'''
给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:

输入: [5, 4, 3, 2, 1]
输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。
提示:

N 是一个正整数并且不会超过 10000。
所有运动员的成绩都不相同。
'''


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans = [''] * len(nums)
        scores = []
        for i, num in enumerate(nums):
            scores.append((num,i))
        scores.sort(reverse=True)
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for j, (_, i) in enumerate(scores):
            if j < 3:
                ans[i] = ranks[j]
            else:
                ans[i] = str(j+1)
        return ans



print(Solution().findRelativeRanks([10,3,8,9,4]))