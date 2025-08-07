class Solution:
    def findPeakElement(self, arr):
        """
        Finds a peak element in the array (an element strictly greater than its neighbors).
        Approach:
        - Use binary search to efficiently find a peak element.
        - The trick: If an element is less than its left neighbor, a peak must exist to the left; if less than its right neighbor, a peak must exist to the right. This property allows binary search.
        - For each mid, check if it's a peak; otherwise, move towards the direction of a higher neighbor.
        - Edge cases: Handles single-element arrays and peaks at the boundaries.
        How to identify binary search is applicable:
        - The problem asks for an index, not a value.
        - There is a monotonic property: moving towards a higher neighbor guarantees a peak exists in that direction.
        - The search space can be halved based on comparisons, not just sorted order.
        """
        n = len(arr)
        # Binary search boundaries: avoid checking boundaries in the loop
        low, high = 1, n - 2

        # Edge case: Single-element array
        if n == 1:
            return 0

        # Edge case: Peak at the first element
        if arr[0] > arr[1]:
            return 0
        # Edge case: Peak at the last element
        if arr[-1] > arr[-2]:
            return n - 1
        
        # Binary search for a peak in the middle of the array
        while low <= high:       
            mid = (low + high) // 2

            # If mid is a peak
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            # If left neighbor is greater, move left
            elif arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                # Otherwise, move right
                low = mid + 1
        
        # Should never reach here if input is valid
        return -1