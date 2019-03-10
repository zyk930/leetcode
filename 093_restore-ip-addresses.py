#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/3/4 21:34
#@Author  :ZYK
#@FileName: 093_restore-ip-addresses.py


'''
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, start, k, result, ans):
            if k == 4:
                if start == len(s):
                    ans.append('.'.join(result))
                else:
                    return

            for i in range(1, 4):
                if start + i > len(s):
                    break

                if i > 1 and s[start] == '0':
                    continue

                if i != 3 or s[start:start+i] < '256':
                    dfs(s, start+i, k+1, result+[s[start:start+i]], ans)


        ans = []
        dfs(s, 0, 0, [], ans)
        return ans

print(Solution().restoreIpAddresses("25525511135"))
