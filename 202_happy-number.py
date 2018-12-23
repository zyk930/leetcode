#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/18 11:13
#@Author  :ZYK
#@FileName: 202_happy-number.py

'''
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例:

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = []
        while n != 1:
            a = 0
            b = n
            while b > 0:
                a += (b % 10)**2
                b //= 10
            if a in record:
                return False
            else:
                record.append(a)
                n = a
        return True



print(Solution().isHappy(19))