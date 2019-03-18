#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 9:54
# @Author  : zyk

'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        self.dfs(s, wordDict, [], res)
        return res

    def dfs(self, s, wordDict, str_path, res):
        if self.check(s, wordDict):
            if len(s) == 0:
                res.append(' '.join(str_path))

            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, str_path+[s[:i]], res)

    def check(self, s, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            str = s[:i]
            for j in range(i):
                if str[j:] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]



s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, wordDict))