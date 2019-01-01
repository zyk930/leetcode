#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/24 11:15
#@Author  :ZYK
#@FileName: 407_longest-palindrome.py

'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
假设字符串的长度不会超过 1010。

示例 1:

输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
'''

class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: int
    """
    maxLen = 0
    single = False
    d = {}
    for c in s:
      d[c] = d.get(c, 0) + 1

    for key in d:
        if d[key] > 1:
            count = d[key]
            left = d[key] % 2
            d[key] = left
            maxLen += count - left
        if not single:
            if d[key] == 1:
                maxLen += 1
                single = True

    return maxLen


print(Solution().longestPalindrome('abccccdd'))