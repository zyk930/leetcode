#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/29 10:36
#@Author  :ZYK
#@FileName: 199_binary-tree-right-side-view.py

'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        deque = [root]
        while deque:
            tmp = []
            res.append(deque[-1].val)
            for node in deque:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            deque = tmp
        return res