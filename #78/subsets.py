# https://leetcode.com/problems/subsets/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backTrack(i=0, stack=[]):
            if i == len(nums):
                res.append(stack[:])
                
                return
            stack.append(nums[i])
            backTrack(i+1,stack)
            stack.pop()
            backTrack(i+1, stack)
        backTrack()
        return res