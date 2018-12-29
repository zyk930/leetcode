#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 10:57
# @Author  : zyk

'''
给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:

输入:
[[0,0],[1,0],[2,0]]

输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
'''


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in points:
            dic = {}
            for j in points:
                if j != i:
                    dist = (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2
                    dic[dist] = dic.get(dist, 0) + 1
            for k in dic:
                ans += dic[k] * (dic[k] - 1)
        return ans

print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))