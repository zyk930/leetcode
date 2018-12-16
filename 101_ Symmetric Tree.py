#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/14 12:44
#@Author  :ZYK
#@FileName: 101_ Symmetric Tree.py

# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isMirror(root, mirror):
            if not root and not root:
                return True
            if root and mirror and root.val == mirror.val:
                return isMirror(root.left, mirror.right) and isMirror(root.right, mirror.left)
            return False

        return isMirror(root, root)