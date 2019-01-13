#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/13 21:38
#@Author  :ZYK
#@FileName: 022_generate-parentheses.py

'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # def dfs(left, path, res, n):
        #     if len(path) == 2 * n:
        #         if left == 0:
        #             res.append("".join(path))
        #         return
        #
        #     if left < n:
        #         path.append('(')
        #         dfs(left+1, path, res, n)
        #         path.pop()
        #     if left > 0:
        #         path.append(')')
        #         dfs(left-1, path, res, n)
        #         path.pop()
        #
        #     return res
        #
        # res = []
        # dfs(0, [], res, n)
        # return res
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans
print(Solution().generateParenthesis(3))