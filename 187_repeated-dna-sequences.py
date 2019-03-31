#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/29 10:10
#@Author  :ZYK
#@FileName: 187_repeated-dna-sequences.py

'''
所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。

示例:

输入: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

输出: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        ans = []
        for i in range(len(s) - 9):
            str = s[i:i+10]
            dic[str] = dic.get(str, 0) + 1
            if dic[str] == 2:
                ans.append(str)
        return ans