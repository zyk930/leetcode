#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/13 12:55
#@Author  :ZYK
#@FileName: 069_Sqrt(x).py

# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # lo = 0
        # hi = x
        # while lo <= hi:
        #     mid = lo + (hi - lo)//2
        #     tmp = mid*mid
        #     if tmp < x:
        #         lo = mid+1
        #     elif tmp > x:
        #         hi = mid-1
        #     else:
        #         return mid
        # return hi
## 牛顿迭代法

        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)

print(Solution().mySqrt(8))