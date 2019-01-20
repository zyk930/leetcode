#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/16 20:40
#@Author  :ZYK
#@FileName: 037_sudoku-solve.py

'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。
'''


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        def helper(board, i, j, rows, columns, boxes):
            if board[i][j] == '.':
                for k in range(1, 10):
                    box_index = (i // 3) * 3 + j // 3
                    if rows[i][k-1] == 1 or columns[j][k-1] == 1 or boxes[box_index][k-1] == 1:
                        continue

                    rows[i][k-1] = columns[j][k-1] = boxes[box_index][k-1] = 1
                    board[i][j] = str(k)
                    if i == j == 8:
                        return True
                    if i + 1 < 9:
                        if helper(board, i + 1, j, rows, columns, boxes):
                            return True
                    elif j + 1 < 9:
                        if helper(board, 0, j + 1, rows, columns, boxes):
                            return True

                    rows[i][k - 1] = columns[j][k - 1] = boxes[box_index][k - 1] = 0
                    board[i][j] = '.'
            else:
                if i == j == 8:
                    return True
                if i + 1 < 9:
                    if helper(board, i + 1, j, rows, columns, boxes):
                        return True
                elif j + 1 < 9:
                    if helper(board, 0, j + 1, rows, columns, boxes):
                        return True
            return False


        for i in range(9):
            for j in range(9):
                box_index = (i // 3) * 3 + j // 3
                if board[i][j] != '.':
                    k = int(board[i][j]) - 1
                    rows[i][k] = columns[j][k] = boxes[box_index][k] = 1
        helper(board, 0, 0, rows, columns, boxes)
        print(board)


a = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(Solution().solveSudoku(a))