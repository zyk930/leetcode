#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/12 12:59
#@Author  :ZYK
#@FileName: 028_Implement strStr().py


# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        for i in range(len(haystack)):
            k = i
            j = 0
            while k<len(haystack) and j<len(needle) and haystack[k] == needle[j]:
                k += 1
                j += 1
            if j == len(needle):
                return i
        return -1 if needle else 0



print(Solution().strStr('hello','ll'))