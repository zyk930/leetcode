#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/2 0:10
#@Author  :ZYK
#@FileName: 541_reverse-string-ii.py

'''
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:

该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
'''


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans = []
        a = ''
        b = ''
        cnt = 0
        isFirst = True
        for c in s:
            if isFirst:
                a += c
            else:
                b += c
            cnt += 1
            if cnt == k:
                if isFirst:
                    a = a[::-1]
                    ans.append(a)
                    a = ''
                else:
                    ans.append(b)
                    b = ''
                cnt = 0
                isFirst = not isFirst
        return ''.join(ans)+a[::-1]+b



print(Solution().reverseStr("abcdefg", 2))