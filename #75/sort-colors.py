# https://leetcode.com/problems/sort-colors/description/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_map = [0,0,0]
        for num in nums:
            color_map[num] += 1
        nums[:] =[]
        for i, count in enumerate(color_map):
            nums.extend([i] * count)
             