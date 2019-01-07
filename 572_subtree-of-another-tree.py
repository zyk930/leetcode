#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 11:25
# @Author  : zyk

'''
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        def serialize(root):
            ans = []
            stack = [(root, 1)]
            while stack:
                node, p = stack.pop()
                if not node:
                    ans.append("#")
                    continue
                if p == 0:
                    ans.append("|" + str(node.val))
                else:
                    stack.append((node.right, 1))
                    stack.append((node.left, 1))
                    stack.append((node, 0))
            return ",".join(ans)

        print(serialize(t))
        print(serialize(s))
        return serialize(t) in serialize(s)