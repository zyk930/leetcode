#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/28 11:30
#@Author  :ZYK
#@FileName: 479_largest-palindrome-product.py

'''
你需要找到由两个 n 位数的乘积组成的最大回文数。

由于结果会很大，你只需返回最大回文数 mod 1337得到的结果。

示例:

输入: 2

输出: 987

解释: 99 x 91 = 9009, 9009 % 1337 = 987

说明:

n 的取值范围为 [1,8]。
'''


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 9
        # for a in range(2, 9 * 10 ** (n - 1)):
        #     hi = (10 ** n) - a
        #     lo = int(str(hi)[::-1])
        #     print(hi)
        #     print(lo)
        #     print(a ** 2 - 4 * lo)
        #     if a ** 2 - 4 * lo < 0:
        #         continue
        #
        #     if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):
        #         return (lo + 10 ** n * (10 ** n - a)) % 1337
        if n == 1:
            return 9
        x = 10 ** n
        s = 10 ** n
        while 1:
            x -= 1
            num = int(str(x) + str(x)[::-1])
            limit = num ** 0.5
            for i in range(num // s + 1, int(limit)):
                if num % i == 0:
                    return num % 1337


print(Solution().largestPalindrome(2))