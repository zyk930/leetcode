#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 15:51
# @Author  : zyk

'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def reverse(root):
            pre = None
            cur = root
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        end = reverse(slow)
        while head and end:
            if head.val != end.val:
                return False
            head = head.next
            end = end.next
        return True