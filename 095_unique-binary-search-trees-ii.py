#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/5 22:01
#@Author  :ZYK
#@FileName: 095_unique-binary-search-trees-ii.py

'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def reset(root, offset):
            if root:
                newroot = TreeNode(root.val + offset)
                newroot.left = reset(root.left, offset)
                newroot.right = reset(root.right, offset)
                return newroot

        if n == 0:
            return []
        dp = [[]] * (n + 1)
        dp[0] = [None]
        for i in range(1, n + 1):
            dp[i] = []
            for j in range(1, i + 1):
                for left in dp[j - 1]:
                    for right in dp[i - j]:
                        root = TreeNode(j)
                        root.left = left
                        root.right = reset(right, j)
                        dp[i].append(root)
        return dp[-1]

