class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        
        # Edge case: single element array
        if n == 1:
            return nums[0]
        
        # Check if single element is at the boundaries
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        # Binary search range: exclude first and last elements (already checked)
        low, high = 1, n - 2

        while low <= high:
            mid = (low + high) // 2

            # Found the single element: different from both neighbors
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
                return nums[mid]

            # Check if we're in the "normal" pattern (before single element)
            # Normal pattern: odd indices pair with previous, even indices pair with next
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                # Pattern is normal → single element is to the RIGHT
                low = mid + 1
            else:
                # Pattern is disrupted → single element is to the LEFT (or we're past it)
                high = mid - 1
        
        return -1  # Should never reach here for valid input

    # Pattern explanation:
    # Before single element: pairs at (0,1), (2,3), (4,5)... - even indices pair forward
    # After single element:  pairs at (x,x+1), (x+2,x+3)... - pattern shifts
    # We detect which side of the disruption we're on by checking pairing rules