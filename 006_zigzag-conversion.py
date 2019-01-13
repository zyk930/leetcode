#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/11 21:33
#@Author  :ZYK
#@FileName: 006_zigzag-conversion.py

'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if numRows == 1:
        #     return s
        # a = [[] for _ in range(numRows)]
        # r = 0
        # # direct = 1
        # for c in s:
        #     a[r].append(c)
        #     if r == numRows-1:
        #         direct = -1
        #     elif r == 0:
        #         direct = 1
        #     r += direct
        # ans = ''
        # for i in a:
        #     ans += ''.join(i)
        # return ans
        if numRows == 1:
            return s
        k = len(s)
        rstr = ""

        zlen = 2 * (numRows-1)
        for i in range(0, numRows):
            n1 = 2 * (numRows - i - 1)
            n2 = zlen - n1

            if n1 == 0 or n2 == 0:
                n1 = n2 = zlen

            j = 0
            index = i
            while index < k:
                rstr = rstr + s[index]
                if j % 2 == 0:
                    index = index + n1
                else:
                    index = index + n2
                j += 1
        return rstr

print(Solution().convert("PAYPALISHIRING",4))