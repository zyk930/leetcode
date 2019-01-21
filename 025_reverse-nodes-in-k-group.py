#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 17:12
# @Author  : zyk

'''
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = pre = ListNode(-1)
        dummy.next = head

        while head:
            tmp = []

            for _ in range(k):
                if head:
                    tmp.append(head)
                    head = head.next
                else:
                    return dummy.next

            for i in range(k):
                if i != k - 1:
                    tmp[k - 1 - i].next = tmp[k - 1 - i - 1]
                pre.next = tmp[-1]
                tmp[0].next = head
                pre = tmp[0]

        return dummy.next
