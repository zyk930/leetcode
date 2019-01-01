#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/24 10:47
#@Author  :ZYK
#@FileName: 405_convert-a-number-to-hexadecimal.py

'''
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
示例 1：

输入:
26

输出:
"1a"
示例 2：

输入:
-1

输出:
"ffffffff"
'''


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexRes = []
        if num < 0:
            num+=2**32#处理负数的方法
        if num == 0:
            return '0'
        while num > 0:
            figure = num % 16
            num //= 16
            if figure>=0 and figure<=9:
                hexRes.append(str(figure))
            else:
                hexRes.append(dict[figure])
        hexRes=hexRes[::-1]
        return ''.join(hexRes)#数组转换成字符

print(Solution().toHex(26))