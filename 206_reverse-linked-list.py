#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 21:10
# @Author  : zyk

'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next:
        #     return head
        # ret = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return ret

        # pre = None
        # cur = head
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = tmp
        # return pre

        dummy = ListNode(-1)
        p = head
        while p:
            tmp = dummy.next
            dummy.next = p
            p = p.next
            dummy.next.next = tmp
        return dummy.next
