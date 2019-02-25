#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 9:58
# @Author  : zyk

'''
给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

说明:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
示例:

输入:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
示例 2:

输入:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。
     第二行同样为左对齐，这是因为这行只包含一个单词。
示例 3:

输入:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # def space(words, s, flag):
        #     print(words)
        #     res = words[0]
        #     if flag:
        #         if len(words) > 1:
        #             for i in words[1:]:
        #                 res += ' ' + i
        #         return res
        #     if len(words) > 1:
        #         l = s // (len(words) - 1)
        #         k = s % (len(words) - 1)
        #         for i in words[1:]:
        #             if k == 0:
        #                 res += ' ' * (l + 1) + i
        #             else:
        #                 res += ' ' * (l + 2) + i
        #                 k -= 1
        #     else:
        #         res += ' ' * s
        #     return res
        #
        # ans = []
        # i, L = 0, 0
        # while i < len(words):
        #     if len(words[i]) + L + i <= maxWidth:
        #         if i == len(words) - 1:
        #             cur = space(words, maxWidth - L - i + 1, True)
        #             cur += ' ' * (maxWidth - len(cur))
        #             ans.append(cur)
        #             return ans
        #         L += len(words[i])
        #         i += 1
        #     else:
        #         cur = space(words[:i], maxWidth - L - i + 1, False)
        #         ans.append(cur)
        #         words = words[i:]
        #         i, L = 0, 0
        res = []
        i = 0
        while i < len(words):
            k, l = 0, 0
            while i + k < len(words) and l + len(words[i+k]) <= (maxWidth-k):
                l += len(words[i+k])
                k += 1
            tmp = words[i]
            j = 0
            while j < k-1:
                if i + k == len(words):
                    tmp += ' '
                else:
                    tmp += ' ' * ((maxWidth - l)//(k-1) + (j < ((maxWidth - l)%(k-1))))
                tmp += words[i+j+1]
                j += 1
            tmp += ' ' * (maxWidth - len(tmp))
            res.append(tmp)
            i += k
        return res





words = ["This", "is", "an", "example", "of", "text", "justification."]
print(Solution().fullJustify(words, 16))