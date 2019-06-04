#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 21:07
# @Author  : zyk

'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '(' + s + ')'
        tmp = []
        stack = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '(':
                tmp.append(len(stack))
                i += 1
            elif s[i] == ')':
                start = tmp.pop()
                j = start
                a = stack[j]
                while j + 2 < len(stack):
                    ops = stack[j+1]
                    if ops == '+':
                        a += stack[j+2]
                    else:
                        a -= stack[j+2]
                    j += 2
                k = len(stack) - start
                while k > 0:
                    stack.pop()
                    k -= 1
                stack.append(a)
                i += 1
            elif s[i] in '+-':
                stack.append(s[i])
                i += 1
            else:
                start = i
                while i < len(s) and s[i] not in '+-()':
                    i += 1
                num = int(s[start:i])
                stack.append(num)
        return stack[0]


print(Solution().calculate("1+2"))