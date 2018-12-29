#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/29 10:03
# @Author  : zyk

'''
1. 你设计的矩形页面必须等于给定的目标面积。

2. 宽度 W 不应大于长度 L，换言之，要求 L >= W 。

3. 长度 L 和宽度 W 之间的差距应当尽可能小。
你需要按顺序输出你设计的页面的长度 L 和宽度 W。

示例：

输入: 4
输出: [2, 2]
解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
说明:

给定的面积不大于 10,000,000 且为正整数。
你设计的页面的长度和宽度必须都是正整数。
'''


class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # res = [area, 1]
        # for w in range(1, int(area ** .5)+1):
        #     if area % w == 0:
        #         l = area // w
        #         if res[0] - res[1] > l - w:
        #             res = [l, w]
        # return res
        root = int(area ** 0.5)
        while root > 0:
            if area % root == 0:
                return int(area / root), root
            root -= 1

print(Solution().constructRectangle(4))