#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/3 0:27
#@Author  :ZYK
#@FileName: 563_binary-tree-tilt.py

'''
给定一个二叉树，计算整个树的坡度。

一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。

整个树的坡度就是其所有节点的坡度之和。

示例:

输入:
         1
       /   \
      2     3
输出: 1
解释:
结点的坡度 2 : 0
结点的坡度 3 : 0
结点的坡度 1 : |2-3| = 1
树的坡度 : 0 + 0 + 1 = 1
注意:

任何子树的结点的和不会超过32位整数的范围。
坡度的值不会超过32位整数的范围。
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0, 0
            leftSum, leftTilt = dfs(root.left)
            rightSum, rightTilt = dfs(root.right)

            return leftSum + root.val + rightSum, abs(leftSum - rightSum) + leftTilt + rightTilt

        return dfs(root)[1]