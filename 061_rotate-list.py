#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 20:38
# @Author  : zyk

'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        l = 1
        p = head
        while p.next:
            l += 1
            p = p.next
        k %= l
        if k == 0:
            return head
        k = l - k - 1
        print(k)
        pp = head
        while k > 0:
            pp = pp.next
            k -= 1
        newhead, pp.next, p.next = pp.next, None, head
        return newhead