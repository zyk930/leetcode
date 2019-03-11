#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 15:55
# @Author  : zyk

'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        ans = []
        odd = True
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
            if odd:
                ans.append(tmp)
            else:
                ans.append(tmp[::-1])
            odd = not odd
        return ans