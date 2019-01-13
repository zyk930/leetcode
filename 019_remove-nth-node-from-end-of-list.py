#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/13 21:09
#@Author  :ZYK
#@FileName: 019_remove-nth-node-from-end-of-list.py

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head

        slow = fast = dummy
        while n and fast:
            fast = fast.next
            n -= 1

        while fast.next and slow.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
        # dummy = ListNode(-1)
        # dummy.next = head
        # length = 0
        # first = head
        # while first:
        #     length += 1
        #     first = first.next
        #
        # length -= n
        # first = dummy
        # while length > 0:
        #     length -= 1
        #     first = first.next
        #
        # first.next = first.next.next
        # return dummy.next
