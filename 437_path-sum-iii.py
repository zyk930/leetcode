#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 20:03
# @Author  : zyk

'''
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        preDict = {0: 1}

        def dfs(p, sum, pathsum, preDict):
            if p:
                pathsum += p.val
                self.count += preDict.get(pathsum - sum, 0)
                preDict[pathsum] = preDict.get(pathsum, 0) + 1
                dfs(p.left, sum, pathsum, preDict)
                dfs(p.right, sum, pathsum, preDict)
                preDict[pathsum] -= 1

        dfs(root, sum, 0, preDict)
        return self.count