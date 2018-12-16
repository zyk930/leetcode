#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/12 16:46
#@Author  :ZYK
#@FileName: 038_Count and Say.py


# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.
# 1
# 2.
# 11
# 3.
# 21
# 4.
# 1211
# 5.
# 111221
# 1
# 被读作
# "one 1"("一个一"), 即
# 11。
# 11
# 被读作
# "two 1s"("两个一"）, 即
# 21。
# 21
# 被读作
# "one 2", "one 1" （"一个二", "一个一"), 即
# 1211。
#
# 给定一个正整数
# n（1 ≤ n ≤ 30），输出报数序列的第
# n
# 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
#
# 示例
# 1:
#
# 输入: 1
# 输出: "1"
# 示例
# 2:
#
# 输入: 4
# 输出: "1211"

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        n -= 1
        while n > 0:
            res = ''
            pre = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if ans[i] == pre:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res
            n -= 1
        return ans


print(Solution().countAndSay(4))