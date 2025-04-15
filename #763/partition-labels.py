class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {c: i for i,c in enumerate(s)}
        j = start = 0
        res = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                res.append(i - start + 1)
                start = i + 1
        return res