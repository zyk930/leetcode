#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 15:18
# @Author  : zyk

'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans, left, right = 0, 0, len(height) - 1
        leftwall = rightwall = float('-inf')

        while left <= right:
            if leftwall <= rightwall:
                ans += max(0, leftwall - height[left])
                leftwall = max(leftwall, height[left])
                left += 1
            else:
                ans += max(0, rightwall - height[right])
                rightwall = max(rightwall, height[right])
                right -= 1
        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))