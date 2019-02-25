#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/21 9:48
# @Author  : zyk

'''
输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in dic:
                dic[tuple(count)] = [s]
            else:
                dic[tuple(count)].append(s)
        return [dic[k] for k in dic]
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))