#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/8 20:40
#@Author  :ZYK
#@FileName: 001_two sum.py

# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ### 蛮力搜索 时间复杂度O(n2)###
        # for i in range(len(nums)):
        #     for j in range(i+1,(len(nums))):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], i]
            d[num] = i

        # 哈希表， 用空间换时间 时间复杂度O(n)

if __name__ == '__main__':
    print(Solution().twoSum([3,3], 6))
