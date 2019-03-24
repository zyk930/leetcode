#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/20 20:14
#@Author  :ZYK
#@FileName: 150_evaluate-reverse-polish-notation.py

'''
根据逆波兰表示法，求表达式的值。

有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

说明：

整数除法只保留整数部分。
给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
示例 1：

输入: ["2", "1", "+", "3", "*"]
输出: 9
解释: ((2 + 1) * 3) = 9
示例 2：

输入: ["4", "13", "5", "/", "+"]
输出: 6
解释: (4 + (13 / 5)) = 6
示例 3：

输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
输出: 22
解释:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in['+', '-', '*', '/']:
                num1, num2 = stack.pop(), stack.pop()
                if token == '+':
                    res = num1 + num2
                if token == '-':
                    res = num2 - num1
                if token == '*':
                    res = num2 * num1
                if token == '/':
                    res = int(float(num2) / float(num1))
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()

print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
