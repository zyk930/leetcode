#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/14 22:46
#@Author  :ZYK
#@FileName: 030_substring-with-concatenation-of-all-words.py

'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。



示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]
'''


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        # d = {}
        # t = {}
        # ans = []
        # wl = len(words[0])
        # fullscore = 0
        # for word in words:
        #     d[word] = d.get(word, 0) + 1
        #     fullscore += 1
        #
        # for i in range(len(s)):
        #     head = start = i
        #     t = {}
        #     score = 0
        #
        #     while start + wl <= len(s) and s[start:start+wl] in d:
        #         cword = s[start:start+wl]
        #         t[cword] = t.get(cword, 0) + 1
        #         if t[cword] <= d[cword]:
        #             score += 1
        #         else:
        #             break
        #         start += wl
        #
        #         if score == fullscore:
        #             ans.append(head)
        #
        # return ans
        if len(words) == 0:
            return []
        l = len(words[0])
        target = {}
        for w in words:
            target[w] = target.get(w, 0) + 1
        ans = []
        for k in range(l):
            left = k
            count = 0
            window = {}
            for j in range(k, len(s) - l + 1, l):
                m = s[j:j + l]
                if m in target:
                    count += 1
                    window[m] = window.get(m, 0) + 1
                    while window[m] > target[m]:
                        window[s[left:left + l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                else:
                    left = j + l
                    count = 0
                    window = {}
        return ans

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))

