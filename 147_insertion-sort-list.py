#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/19 20:35
#@Author  :ZYK
#@FileName: 147_insertion-sort-list.py

"""
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。


示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            p = dummy
            while p.next.val < val:
                p = p.next
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = p.next
            p.next = tmp
        return dummy.next
