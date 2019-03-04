#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/2 10:49
#@Author  :ZYK
#@FileName: 086_partition-list.py


'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = sp = ListNode(-1)
        ldummy = ListNode(-1)
        ldummy.next = head
        p = ldummy
        while p and p.next:
            if p.next.val < x:
                sp.next = p.next
                p.next = p.next.next
                sp = sp.next
            else:
                p = p.next
        sp.next = ldummy.next
        return dummy.next