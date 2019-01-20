#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/20 21:24
#@Author  :ZYK
#@FileName: 045_jump-game-ii.py

'''
数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = maxpos = lastpos = 0
        for i in range(len(nums)):
            if i > lastpos:
                lastpos = maxpos
                step += 1
            maxpos = max(maxpos, i + nums[i])
        return step

        # pos = 0
        # ans = 0
        # bound = len(nums)
        # while pos < len(nums) - 1:
        #     dis = nums[pos]
        #     farthest = 0
        #     for i in range(pos + 1, min(pos + dis + 1, bound)):
        #         canReach = i + nums[i]
        #         if i == len(nums) - 1:
        #             return ans + 1
        #         if canReach > farthest:
        #             farthest = canReach
        #             pos = i
        #     ans += 1
        #
        # return ans
print(Solution().jump([2,3,1,1,4]))