#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/3 16:31
#@Author  :ZYK
#@FileName: 590_n-ary-tree-postorder-traversal.py

'''
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :







返回其后序遍历: [5,6,3,2,4,1].


'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # if not root.children:
        #     return [root.val]
        # result = []
        # for child in root.children:
        #     result += self.postorder(child)
        # result += [root.val]
        # return result
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.children:
                curr.children.reverse()
                stack += curr.children
        return result
