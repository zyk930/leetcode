#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/27 20:37
# @Author  : zyk

'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            if p.next.next and p.next.val == p.next.next.val:
                z = p.next
                while z.next and z.val == z.next.val:
                    z = z.next
                p.next = z.next
            else:
                p = p.next
        return dummy.next
