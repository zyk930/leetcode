#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 10:58
# @Author  : zyk

'''
给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。



American keyboard



示例：

输入: ["Hello", "Alaska", "Dad", "Peace"]
输出: ["Alaska", "Dad"]


注意：

你可以重复使用键盘上同一字符。
你可以假设输入的字符串将只包含字母。
'''


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = []
        d = {}
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        for i in row1:
            d[i] = 1
        for i in row2:
            d[i] = 2
        for i in row3:
            d[i] = 3

        for word in words:
            same = True
            pre = d[word[0].lower()]
            for c in word:
                if d[c.lower()] != pre:
                    same = False
                    break
            if same:
                ans.append(word)
        return ans



print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
