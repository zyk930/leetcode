#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 20:47
# @Author  : zyk

'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。



示例 :

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：


'''


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(grid, i ,j):
            res = 0
            if grid[i][j] == 0:
                return 0
            if i == 0 or i > 0 and grid[i-1][j] == 0:
                res += 1
            if i == len(grid)-1 or i < len(grid) - 1 and grid[i+1][j] == 0:
                res += 1
            if j == 0 or j > 0 and grid[i][j-1] == 0:
                res += 1
            if j == len(grid[0])-1 or j < len(grid[0]) - 1 and grid[i][j+1] == 0:
                res += 1
            return res

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += helper(grid, i, j)
        return ans


print(Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))