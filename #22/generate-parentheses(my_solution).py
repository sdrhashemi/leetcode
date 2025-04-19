# https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        d = n *2
        def backTrack(currStr, baz, baste):
            if len(currStr) == d and baz ==n and baste ==n:
                res.append(currStr)
                return
            if len(currStr) == d and baz !=0:
                return
            if len(currStr) == d and baste !=0:
                return
            if baz < n:
                backTrack(currStr + "(", baz+1, baste)
            if baste < baz:
                backTrack(currStr + ")", baz, baste +1)
        backTrack("", 0, 0)
        return res
        