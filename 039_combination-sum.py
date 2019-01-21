#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 9:57
# @Author  : zyk

'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(candidates, start, target, path, res):
            if target == 0:
                return res.append(path)

            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    # path.append(candidates[i])
                    dfs(candidates, i, target - candidates[i], path + [candidates[i]], res)
                    # path.pop()

        res = []
        dfs(candidates, 0, target, [], res)
        return res

print(Solution().combinationSum([2,3,5], 8))