#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 17:23
# @Author  : zyk

'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # p = dummy = ListNode(-1)
        # carry = 0
        # while l1 and l2:
        #     p.next = ListNode(l1.val + l2.val + carry)
        #     carry = p.next.val // 10
        #     p.next.val %= 10
        #     p = p.next
        #     l1 = l1.next
        #     l2 = l2.next
        # res = l1 or l2
        # while res:
        #     p.next = ListNode(res.val + carry)
        #     carry = p.next.val // 10
        #     p.next.val %= 10
        #     p = p.next
        #     res = res.next
        # if carry:
        #     p.next = ListNode(1)
        # return dummy.next
        p = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val / 10
            p.next = ListNode(val % 10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next