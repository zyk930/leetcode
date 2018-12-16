#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/12 21:40
#@Author  :ZYK
#@FileName: 066_Plus One.py

# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num = ''
        # for i in digits:
        #     num += str(i)
        # tmp = str(int(num)+1)
        # list = [int(j) for j in tmp]
        # return list
        carry = 1
        for i in reversed(range(0, len(digits))):
            if carry == 1:
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0

        if carry == 1:
            return [1] + digits
        return digits


print(Solution().plusOne([4,3,2,1]))