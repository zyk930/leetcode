#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 15:51
# @Author  : zyk
'''
给定一个正整数，返回它在 Excel 表中相对应的列名称。

例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
示例 1:

输入: 1
输出: "A"
示例 2:

输入: 28
输出: "AB"
示例 3:

输入: 701
输出: "ZY"
'''
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = ""
        while n > 0:
            y = n % 26
            if y == 0:
                char = "Z"
                n -= 26
            else:
                char = chr(ord("A") + y - 1)
            n = n // 26
            ans += char

        return ans[::-1]

print(Solution().convertToTitle(52))