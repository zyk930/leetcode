#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 20:57
# @Author  : zyk

'''
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # from collections import Counter
        #
        # sCount = Counter(s[:len(p) - 1])
        # pCount = Counter(p)
        # ans = []
        #
        # for i in range(len(p) - 1, len(s)):
        #     sCount[s[i]] += 1
        #     if sCount == pCount:
        #         ans.append(i - len(p) + 1)
        #     sCount[s[i - len(p) + 1]] -= 1
        #     if sCount[s[i - len(p) + 1]] == 0:
        #         del sCount[s[i - len(p) + 1]]
        # return ans

        from collections import Counter
        s_len, p_len = len(s), len(p)
        count = p_len
        pChar = Counter(p)

        result = []
        for i in range(s_len):
            if pChar[s[i]] >= 1:
                count -= 1
            pChar[s[i]] -= 1

            if i >= p_len:
                if pChar[s[i - p_len]] >= 0:
                    count += 1
                pChar[s[i - p_len]] += 1
            if count == 0:
                result.append(i - p_len + 1)

        return result


print(Solution().findAnagrams('acbab','ab'))