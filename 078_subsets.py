#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/26 20:31
#@Author  :ZYK
#@FileName: 078_subsets.py

'''
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # def dfs(nums, index, path, ans):
        #     ans.append(path)
        #     for i in range(index, len(nums)):
        #         dfs(nums, i+1, path + [nums[i]], ans)
        #
        # ans = []
        # dfs(nums, 0, [], ans)
        # return ans
        res = [[]]
        for i in nums:
            for j in range(len(res)):
                tmp = res[j][:]
                tmp.append(i)
                res.append(tmp)

        return res
print(Solution().subsets([1,2,3]))