class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, s, e):
        if (e - s) + 1 <= 1:
            return nums
        m = (s + e) / 2
        self.mergeSort(nums, s, m)
        self.mergeSort(nums, m+1, e)
        self.merge(nums, s, m, e)
        return nums
    
    def merge(self, nums, s, m, e):
        leftArray = nums[s:m+1]
        rightArray = nums[m+1:e+1]
        outputIndex = s
        leftIndex = 0
        rightIndex = 0
        while leftIndex < len(leftArray) and rightIndex < len(rightArray):
            if leftArray[leftIndex] <= rightArray[rightIndex]:
                nums[outputIndex] = leftArray[leftIndex]
                leftIndex += 1
            else:
                nums[outputIndex] = rightArray[rightIndex]
                rightIndex += 1
            outputIndex += 1

        while leftIndex < len(leftArray):
            nums[outputIndex] = leftArray[leftIndex]
            leftIndex += 1
            outputIndex += 1

        while rightIndex < len(rightArray):
            nums[outputIndex] = rightArray[rightIndex]
            rightIndex += 1
            outputIndex += 1

        return nums

                
