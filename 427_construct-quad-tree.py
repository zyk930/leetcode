#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 19:25
# @Author  : zyk

'''
我们想要使用一棵四叉树来储存一个 N x N 的布尔值网络。网络中每一格的值只会是真或假。树的根结点代表整个网络。对于每个结点, 它将被分等成四个孩子结点直到这个区域内的值都是相同的.

每个结点还有另外两个布尔变量: isLeaf 和 val。isLeaf 当这个节点是一个叶子结点时为真。val 变量储存叶子结点所代表的区域的值。

你的任务是使用一个四叉树表示给定的网络。下面的例子将有助于你理解这个问题：

给定下面这个8 x 8 网络，我们将这样建立一个对应的四叉树：



由上文的定义，它能被这样分割：





对应的四叉树应该像下面这样，每个结点由一对 (isLeaf, val) 所代表.

对于非叶子结点，val 可以是任意的，所以使用 * 代替。



提示：

N 将小于 1000 且确保是 2 的整次幂。
如果你想了解更多关于四叉树的知识，你可以参考这个 wiki 页面。
'''

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if len(grid) == 1:
            return Node(grid[0][0], True, None, None, None, None)
        real = False
        fatal = False
        for row in grid:
            if True in row:
                real = True
            if False in row:
                fatal = True
            if real and fatal:
                break
        if real and not fatal:     #当前矩阵为真
            return Node(True, True, None, None, None, None)
        if not real and fatal:      #当前矩阵为假
            return  Node(False, True, None, None, None, None)
        if real and fatal:          #当前矩阵既包含真值又包含假值，将矩阵等分四份
            topleft = self.construct([row[0:len(grid) // 2] for row in grid[0:len(grid) // 2]])
            topRight = self.construct([row[len(grid) // 2:] for row in grid[0:len(grid) // 2]])
            bottomLeft = self.construct([row[0:len(grid) // 2] for row in grid[len(grid) // 2:]])
            bottomRight = self.construct([row[len(grid) // 2:] for row in grid[len(grid) // 2:]])
            return Node("*", False, topleft, topRight, bottomLeft, bottomRight)
