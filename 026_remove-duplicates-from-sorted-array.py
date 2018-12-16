#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/11 12:29
#@Author  :ZYK
#@FileName: 026_remove-duplicates-from-sorted-array.py

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return  0
        # else:
        #     tmp = nums[0]
        #     i = 1
        #     while i < len(nums):
        #         if nums[i] == tmp:
        #             del nums[i]
        #         else:
        #             tmp = nums[i]
        #             i += 1
        #
        #     return len(nums)
#双指针
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[slow]:
                slow += 1
                nums[slow] = nums[i]
        return slow + 1



print(Solution().removeDuplicates([1,1,2]))