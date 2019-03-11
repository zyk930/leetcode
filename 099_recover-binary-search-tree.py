#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:29
# @Author  : zyk

'''
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.n1 = self.n2 = None
        self.pre = None
        self.findtwonodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    def findtwonodes(self, root):
        if root:
            self.findtwonodes(root.left)
            if self.pre and self.pre.val >= root.val:
                self.n2 = root
                if not self.n1:
                    self.n1 = self.pre
            self.pre = root
            self.findtwonodes(root.right)

