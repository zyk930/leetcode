#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/9 20:27
#@Author  :ZYK
#@FileName: 020_valid-parentheses.py

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true


#使用栈
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = ['()', '[]', '{}']

        for i in range(len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in dic:
                stack.pop()
                stack.pop()
        return stack == []



print(Solution().isValid('([)]'))