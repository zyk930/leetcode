#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/9 14:36
#@Author  :ZYK
#@FileName: 007_reverse-integer.py

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = x > 0 and 1 or -1
        y = abs(x)
        ans = 0

        while y:
            ans = ans*10 + y%10
            y = y//10
        return ans*sign if ans <= 2**31-1 else 0


print(Solution().reverse(-120))