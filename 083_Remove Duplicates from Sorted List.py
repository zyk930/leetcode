#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 21:08
# @Author  : zyk

# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        p = dummy.next

        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next



head1 = ListNode(1)
n1 = ListNode(1)
n2 = ListNode(2)
head1.next = n1
n1.next = n2
