#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/21 22:49
#@Author  :ZYK
#@FileName: 065_valid-number.py

'''
验证给定的字符串是否为数字。

例如:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。
'''


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num, dot, sign, exp = False, False, False, False
        numafterE = True
        for i in range(len(s)):
            if s[i] == ' ':
                if i < len(s) - 1 and s[i + 1] != ' ' and (num or dot or sign or exp):
                    return False
            elif s[i] == '+' or s[i] == '-':
                if i > 0 and s[i - 1] != ' ' and s[i - 1] != 'e':
                    return False
                sign = True
            elif s[i] >= '0' and s[i] <= '9':
                num = True
                numafterE = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or (not num):
                    return False
                exp = True
                numafterE = False
            else:
                return False

        return num and numafterE
