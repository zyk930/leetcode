#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 11:12
# @Author  : zyk

'''
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def visit(v):
            if v != self.pre:
                self.pre = v
                self.cnt = 0
            self.cnt += 1
            if self.cnt > self.maxFreq:
                self.maxFreq = self.cnt
                self.modeCnt = 1
            elif self.cnt == self.maxFreq:
                if self.ans:
                    self.ans[self.modeCnt] = v
                self.modeCnt += 1

        def inorder(root):
              if root:
                inorder(root.left)
                visit(root.val)
                inorder(root.right)

        self.pre = None
        self.ans = None
        self.maxFreq = self.modeCnt = self.cnt = 0
        inorder(root)
        self.ans = [0] * self.modeCnt
        self.modeCnt = self.cnt = 0
        inorder(root)
        return self.ans