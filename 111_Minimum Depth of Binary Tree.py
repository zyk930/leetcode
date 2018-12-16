#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/16 16:17
#@Author  :ZYK
#@FileName: 111_Minimum Depth of Binary Tree.py

'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if not left and not right:
                return 1
            elif not left:
                return right+1
            elif not right:
                return left+1
            else:
                return min(left,right)+1