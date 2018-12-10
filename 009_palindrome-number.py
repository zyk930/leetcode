#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/9 15:31
#@Author  :ZYK
#@FileName: 009_palindrome-number.py

# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0:
        #     return False
        # y = 0
        # tmp = x
        # while x:
        #     y = y * 10 + x % 10
        #     x = x // 10
        # return tmp == y
        # 常规：把整个数反转
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10
        return x == half or half // 10 == x
        #只反转一半的数字

        #时间复杂度：O(log10(n))
print(Solution().isPalindrome(121))