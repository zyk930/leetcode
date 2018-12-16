#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/12 21:26
#@Author  :ZYK
#@FileName: 058_Length of Last Word.py

# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1]) if s.split() else 0

print(Solution().lengthOfLastWord(" "))