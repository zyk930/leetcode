#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/3 16:26
#@Author  :ZYK
#@FileName: 589_n-ary-tree-preorder-traversal.py

'''
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :







返回其前序遍历: [1,3,5,6,2,4]。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)
        return result