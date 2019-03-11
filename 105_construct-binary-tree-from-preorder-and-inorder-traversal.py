#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 17:43
# @Author  : zyk

'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
    #     dic = {}
    #     if not preorder:
    #         return None
    #     for i, v in enumerate(inorder):
    #         dic[v] = i
    #     root = self.dfs(0, len(preorder) - 1, 0, len(preorder) - 1, preorder, inorder, dic)
    #     return root
    #
    # def dfs(self, l1, r1, l2, r2, preorder, inorder, dic):
    #     if r1 >= l1 and r2 >= l2:
    #         root = TreeNode(preorder[l1])
    #         mid = dic[preorder[l1]]
    #
    #         lsize = mid - l2
    #         rsize = r2 - mid
    #         root.left = self.dfs(l1 + 1, l1 + lsize, l2, mid - 1, preorder, inorder, dic)
    #         root.right = self.dfs(l1 + lsize + 1, l1 + lsize + rsize, mid + 1, mid + rsize, preorder, inorder, dic)
    #         return root

        dic = {}
        for i, v in enumerate(inorder):
            dic[v] = i
        root = self.dfs(0, len(preorder) - 1, preorder, inorder, dic)
        return root


    def dfs(self, start, end, preorder, inorder, dic):
        if start <= end:
            root = TreeNode(preorder[self.preindex])
            mid = dic[preorder[self.preindex]]
            self.preindex += 1
            root.left = self.dfs(start, mid - 1, preorder, inorder, dic)
            root.right = self.dfs(mid + 1, end, preorder, inorder, dic)
            return root