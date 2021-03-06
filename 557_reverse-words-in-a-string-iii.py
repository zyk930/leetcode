#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/2 20:27
#@Author  :ZYK
#@FileName: 557_reverse-words-in-a-string-iii.py

'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc"
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        for i, word in enumerate(s):
            s[i] = word[::-1]
        return " ".join(s)

print(Solution().reverseWords("Let's take LeetCode contest"))
