#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/23 17:41
#@Author  :ZYK
#@FileName: 389_find-the-difference.py

'''
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。



示例:

输入：
s = "abcd"
t = "abcde"

输出：
e

解释：
'e' 是那个被添加的字母。
'''

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # dic = {}
        # for l in s:
        #     if l not in dic:
        #         dic[l] = 1
        #     else:
        #         dic[l] += 1
        # for l in t:
        #     if l not in dic or dic[l] == 0:
        #         return l
        #     else:
        #         dic[l] -= 1
        sum1 = sum(map(ord, [c for c in s]))
        sum2 = sum(map(ord, [c for c in t]))
        return chr(sum2 - sum1)

print(Solution().findTheDifference('abcd', 'abcde'))