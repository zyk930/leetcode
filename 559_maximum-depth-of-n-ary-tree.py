#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/2 23:49
#@Author  :ZYK
#@FileName: 559_maximum-depth-of-n-ary-tree.py

'''
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :







我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        ans = []
        for i in root.children:
            depth = self.maxDepth(i)
            ans.append(depth)
        return max(ans) + 1
