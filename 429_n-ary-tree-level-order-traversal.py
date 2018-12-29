#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/24 19:45
# @Author  : zyk

'''
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :







返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]


说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while len(queue):
            l = len(queue)
            tmp = []
            for i in range(l):
                current = queue.pop(0)
                tmp.append(current.val)
                for children in current.children:
                    queue.append(children)
            res.append(tmp)
        return res
