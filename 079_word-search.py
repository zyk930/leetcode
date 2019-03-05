#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 9:47
# @Author  : zyk

'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # if word == '':
        #     return True
        # if len(board) == 0 or len(board[0]) == 0:
        #     return False
        # m = len(board)
        # n = len(board[0])
        #
        # def bfs(x, y, index):
        #     i, j = x, y
        #     visited[x][y] = True
        #     if index == len(word) - 1:
        #         return True
        #     for (x, y) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        #         if x >= 0 and x <= m - 1 and y >= 0 and y <= n-1 and not visited[x][y] and board[x][y] == word[index+1] and bfs(x, y, index + 1):
        #             return True
        #     visited[i][j] = False
        #     return False
        #
        # visited = [[False] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == word[0] and bfs(i, j, 0):
        #             return True
        # return False
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False

        def helper(self, board, i, j, word):
            if board[i][j] != word[0]:
                return False
            if not word[1:]:
                return True
            board[i][j] = '#'
            if i > 0 and self.helper(board, i - 1, j, word[1:]):
                return True
            if i < len(board) - 1 and self.helper(board, i + 1, j, word[1:]):
                return True
            if j > 0 and self.helper(board, i, j - 1, word[1:]):
                return True
            if j < len(board[0]) - 1 and self.helper(board, i, j + 1, word[1:]):
                return True
            board[i][j] = word[0]
            return False



board = [["a"]]


word = "a"
print(Solution().exist(board, word))