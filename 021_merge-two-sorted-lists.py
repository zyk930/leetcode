#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2018/12/10 19:46
#@Author  :ZYK
#@FileName: 021_merge-two-sorted-lists.py

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
  def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    l3 = ListNode(0)
    tmp = l3

    while l1 and l2:
        if l1.val < l2.val:
            tmp.next = l1
            l1 = l1.next
        else:
            tmp.next = l2
            l2 = l2.next
        tmp = tmp.next

    if l1:
        tmp.next = l1
    if l2:
        tmp.next = l2

    return l3.next

head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(4)
head1.next = n1
n1.next = n2

head2 = ListNode(1)
m1 = ListNode(3)
m2 = ListNode(4)
head2.next = m1
m1.next = m2

