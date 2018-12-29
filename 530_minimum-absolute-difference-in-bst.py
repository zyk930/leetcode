#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 19:53
# @Author  : zyk

'''
给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。

示例 :

输入:

   1
    \
     3
    /
   2

输出:
1

解释:
最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
注意: 树中至少有2个节点。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.val = None
        self.ans = float("inf")

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.val is not None:
                self.ans = min(self.ans, abs(root.val - self.val))
            self.val = root.val
            inorder(root.right)

        inorder(root)
        return self.ans
