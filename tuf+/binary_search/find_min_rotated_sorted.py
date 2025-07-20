class Solution(object):
    def findMin(self, nums):
        """
        Finds the minimum element in a rotated sorted array with no duplicates.
        Uses a modified binary search approach.
        Edge cases: Handles arrays that are not rotated (already sorted), and single-element arrays.
        """
        n = len(nums)

        # Initialize pointers for binary search
        low, high = 0, n -1 
        # Initialize min_element to positive infinity
        min_element = float('inf')

        # Binary search loop
        while low <= high:
            mid = (low + high) // 2

            # If the left half is sorted
            if nums[low] <= nums[mid]:
                # The minimum could be at low, so update min_element
                min_element = min(min_element, nums[low])
                # Move to the right half
                low = mid + 1
            else:
                # The right half is sorted, so the minimum could be at mid
                min_element = min(min_element, nums[mid])
                # Move to the left half
                high = mid - 1
        
        # Edge case: If the array is not rotated, the first element is the minimum
        # This is handled by the logic above, as min_element will be updated with nums[low]
        # Edge case: Single-element array, min_element will be updated with that element
        return min_element