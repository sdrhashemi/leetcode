class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        subStringSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in subStringSet:
                subStringSet.remove(s[l])
                l += 1
            subStringSet.add(s[r])
            res = max(res, len(subStringSet))
        return res
        