#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/29 11:35
#@Author  :ZYK
#@FileName: 200_number-of-islands.py

'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.change(grid, i, j)
        return res

    def change(self, grid, i, j):
        grid[i][j] = 0
        if i > 0 and grid[i - 1][j] == '1':
            self.change(grid, i - 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            self.change(grid, i, j - 1)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            self.change(grid, i + 1, j)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            self.change(grid, i, j + 1)
