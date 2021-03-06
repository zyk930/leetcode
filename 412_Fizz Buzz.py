#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/24 11:36
#@Author  :ZYK
#@FileName: 412_Fizz Buzz.py

'''
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                tmp = "FizzBuzz"
            elif i % 3 == 0:
                tmp = "Fizz"
            elif i % 5 == 0:
                tmp = "Buzz"
            else:
                tmp = str(i)
            ans.append(tmp)
        return ans


print(Solution().fizzBuzz(15))