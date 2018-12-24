#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 15:04
# @Author  : zyk

'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # isPrime = [1]*n
        # i = 2
        # while i*i < n:
        #     if isPrime[i] == 0:
        #         continue
        #     for j in range(i*i, n, i):
        #         isPrime[j] = 0
        #     i += 1
        # return isPrime
        # count = 0
        # for i in isPrime[2:]:
        #     if i == 1:
        #         count += 1
        # return count
        if n < 2:
            return 0
        isPrime = [1]*n
        isPrime[0] = 0
        isPrime[1] = 0
        for i in range(2,n):
            if isPrime[i] == 1:
                j = i*i
                if j >= n:
                    break
                while j < n:
                    isPrime[j] = 0
                    j += i

        return sum(isPrime)

print(Solution().countPrimes(14))