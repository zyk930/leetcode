#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:33
# @Author  : zyk

'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
'''

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        tmp = x^y
        count = 0
        mask = 1
        for _ in range(32):
            if tmp & mask == 1:
                count += 1
            tmp >>= 1
        return count
print(Solution().hammingDistance(1,4))