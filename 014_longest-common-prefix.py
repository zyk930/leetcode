#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/9 17:27
#@Author  :ZYK
#@FileName: 014_longest-common-prefix.py

# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        i = 0
        j = 0
        end = 0
        while i < len(strs) and j < len(strs[i]):
            if i == 0:
                pos = strs[i][j]
            else:
                if strs[i][j] != pos:
                    break

            if i == len(strs)-1:
                j += 1
                i = 0
                end += 1
            else:
                i += 1
        return strs[i][:end]


print(Solution().longestCommonPrefix([]))
