#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/2/26 19:48
#@Author  :ZYK
#@FileName: 076_minimum-window-substring.py

'''
给定一个字符串 S 和一个字符串 T，请在 S 中找出包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。
'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        score = 0
        start, end = len(s), 2*len(s)
        wanted = collections.Counter(t)
        d = {}
        deq = collections.deque([])
        for i, c in enumerate(s):
            if c in wanted:
                d[c] = d.get(c, 0) + 1
                deq.append(i)
                if d[c] <= wanted[c]:
                    score += 1
                while deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
                    d[s[deq.popleft()]] -= 1
                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]
        return s[start: end+1]


print(Solution().minWindow("ADOBECODEBANC", 'ABC'))