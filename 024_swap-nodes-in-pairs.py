#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:44
# @Author  : zyk


'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = pre = ListNode(-1)
        dummy.next = head

        while head and head.next:
            pre.next, head.next.next, head.next = head.next, head, head.next.next,

            pre = head
            head = head.next

        return dummy.next