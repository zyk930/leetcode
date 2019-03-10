#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/10 22:43
#@Author  :ZYK
#@FileName: 114_flatten-binary-tree-to-linked-list.py


'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return root

            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return root

            if not right:
                root.right = root.left
                root.left = None
                return left

            if not left:
                return right

            tmp = root.right
            root.right = root.left
            root.left = None
            left.right = tmp
            return right

        dfs(root)