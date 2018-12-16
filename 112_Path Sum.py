#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/16 16:28
#@Author  :ZYK
#@FileName: 112_Path Sum.py

'''
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        queue = [(root, root.val)]
        while queue:
            tmp = []
            for node, v in queue:
                if node.left:
                    tmp.append((node.left, v + node.left.val))
                if node.right:
                    tmp.append((node.right, v + node.right.val))
                if not node.left and not node.right and v == sum:
                    return True
            queue = tmp
        return False
