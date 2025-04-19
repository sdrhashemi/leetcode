# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letterDict = {"2":"abc", "3":"def", "4":"ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8": "tuv",
             "9":"wxyz"}
        res = []
        if not digits:
            return []
        def backTrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in letterDict[digits[i]]:
                backTrack(i +1, currStr +c)
        backTrack(0, "")
        return res