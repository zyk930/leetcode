#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/23 17:36
#@Author  :ZYK
#@FileName: 387_first-unique-character-in-a-string.py

'''
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
'''


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for l in s:
            if l not in dic:
                dic[l] = 1
            else:
                dic[l] += 1
        for i in range(len(s)):
             if dic[s[i]] == 1:
                 return i
        return -1


print(Solution().firstUniqChar('leetcode'))