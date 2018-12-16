#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/13 11:13
#@Author  :ZYK
#@FileName: 067_Add Binary.py

# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        if la > lb:
            b = (la - lb) * '0' + b
        else:
            a = (lb - la) * '0' + a

        res = ''
        carry = 0
        for i in reversed(range(len(a))):
            num_a = int(a[i])
            num_b = int(b[i])
            if carry == 0:
                tmp = num_a + num_b
                if tmp > 1:
                    res = '0' + res
                    carry = 1
                else:
                    res = str(tmp) + res
                    carry = 0
            else:
                if num_a == 0 and num_b == 0:
                    res = '1' + res
                    carry = 0
                elif num_a == 1 and num_b == 1:
                    res = '1' + res
                    carry = 1
                else:
                    res = '0' + res
                    carry = 1
        if carry == 1:
            res = '1' + res
        return res

print(Solution().addBinary("1010","1011"))