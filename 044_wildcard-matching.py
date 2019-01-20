#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/20 18:17
#@Author  :ZYK
#@FileName: 044_wildcard-matching.py

'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        # dp[0][0] = True
        # for j in range(1, len(p)+1):
        #     if p[j-1] == '*':
        #         dp[0][j] = dp[0][j-1]
        # for i in range(1, len(s)+1):
        #     for j in range(1, len(p)+1):
        #         if p[j-1] == '*':
        #             # 空字符 一个字符 多个字符
        #             dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]
        #         else:
        #             dp[i][j] = (s[i-1] == p[j-1] or p[j-1] == '?') and dp[i-1][j-1]
        #
        # return dp[-1][-1]
        i, j = 0, 0
        lastMatchPos, lastStarPos = 0, -1
        while i < len(s):
            if j < len(p) and p[j] in (s[i], '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                lastMatchPos = i
                lastStarPos = j
                j += 1
            elif lastStarPos > -1:
                i = lastMatchPos + 1
                lastMatchPos += 1
                j = lastStarPos + 1
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)



print(Solution().isMatch("acdcb", "a*d?b"))