#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/16 22:31
#@Author  :ZYK
#@FileName: 125_valid-palindrome.py

'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # tmp1 = tmp2 = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         tmp1 += s[i].lower()
        #         tmp2 = s[i].lower()+tmp2
        # return tmp1 == tmp2
        start = 0
        end = len(s)-1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))