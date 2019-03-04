#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/3 19:46
#@Author  :ZYK
#@FileName: 090_subsets-ii.py


'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # nums.sort()
        # res = [[]]
        # for i in nums:
        #     for j in range(len(res)):
        #         tmp = res[j][:]
        #         tmp.append(i)
        #         if tmp not in res:
        #             res.append(tmp)
        # return res
        def dfs(start, nums, path, res, visited):
            res.append(path + [])

            for i in range(start, len(nums)):
                if start != i and nums[i] == nums[i - 1]:
                    continue
                if i not in visited:
                    visited[i] = 1
                    path.append(nums[i])
                    dfs(i + 1, nums, path, res, visited)
                    path.pop()
                    del visited[i]

        nums.sort()
        res = []
        visited = {}
        dfs(0, nums, [], res, visited)
        return res
