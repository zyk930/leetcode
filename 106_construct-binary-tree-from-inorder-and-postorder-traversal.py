#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 20:07
# @Author  : zyk

'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        dic = {}
        if not postorder:
            return None
        for i, v in enumerate(inorder):
            dic[v] = i
        root = self.dfs(0, len(postorder) - 1, 0, len(postorder) - 1, postorder, inorder, dic)
        return root

    def dfs(self, l1, r1, l2, r2, postorder, inorder, dic):
        if r1 >= l1 and r2 >= l2:
            root = TreeNode(postorder[r1])
            mid = dic[postorder[r1]]

            lsize = mid - l2
            rsize = r2 - mid
            root.left = self.dfs(l1, l1 + lsize - 1, l2, mid - 1, postorder, inorder, dic)
            root.right = self.dfs(l1 + lsize, r1 - 1, mid + 1, mid + rsize, postorder, inorder, dic)
            return root