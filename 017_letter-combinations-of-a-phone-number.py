#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/1/13 20:23
#@Author  :ZYK
#@FileName: 017_letter-combinations-of-a-phone-number.py

'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        def dfs(digits, index, path, res, d):
            if index == len(digits):
                res.append("".join(path))
                return

            digit = int(digits[index])
            for c in d[digit]:
                path.append(c)
                dfs(digits, index+1, path, res, d)
                path.pop()


        res = []
        dfs(digits, 0, [], res, dic)
        return res

print(Solution().letterCombinations("23"))
