# https://leetcode.com/problems/generate-parentheses/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN + 1)
                stack.pop()
        backTrack(0, 0)
        return res
        