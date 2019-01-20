#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/15 20:27
#@Author  :ZYK
#@FileName: 032_longest-valid-parentheses.py


'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = dp[i-2] + 2
            if s[i] == s[i-1] == ')':
                if i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-2-dp[i-1]]


        return max(dp)


print(Solution().longestValidParentheses(")()())"))