#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:32
# @Author  : zyk

'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            tmp = []
            for _ in range(len(queue)):
                root = queue.popleft()
                tmp.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            ans.append(tmp)
        return ans
