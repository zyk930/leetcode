#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 11:09
# @Author  : zyk

'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def dfs(root, s, path, res):
            if root:
                path.append(root.val)
                s -= root.val
                left = dfs(root.left, s, path, res)
                right = dfs(root.right, s, path, res)
                if not left and not right and s == 0:
                    res.append(path + [])
                path.pop()
                return True

        res = []
        dfs(root, sum, [], res)
        return res