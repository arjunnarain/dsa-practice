# Bucket Sort Solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for num in nums:
            colors[num] += 1
        
        position = 0
        for color in range(len(colors)):
            for index in range(colors[color]):
                nums[position] = color
                position += 1
        
        return nums

