class Solution:
    def searchInARotatedSortedArrayII(self, nums, k):
        # Get the length of the array
        n = len(nums)
        # Initialize pointers for binary search
        low, high = 0, n - 1

        # Standard binary search loop
        while low <= high:
            # Find the middle index
            mid = (low + high) // 2

            # If the middle element is the target, return True
            if nums[mid] == k:
                return True
            
            # If we can't determine which side is sorted due to duplicates
            if nums[low] == nums[mid] == nums[high]:
                # Move both pointers inward to skip duplicates
                low += 1
                high -= 1
                continue
            
            # If the left half is sorted
            if nums[low] <= nums[mid]:
                # Check if the target is in the left half
                if nums[low] <= k <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Otherwise, the right half must be sorted
                # Check if the target is in the right half
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        # If we exit the loop, the target is not present
        return False

        # Approach:
        # - This is a modified binary search to handle rotated sorted arrays with duplicates.
        # - If nums[low] == nums[mid] == nums[high], we can't determine the sorted half, so we shrink the search space.
        # - Otherwise, we check which half is sorted and adjust the search range accordingly.
        # - The presence of duplicates can degrade the time complexity to O(n) in the worst case.

        
        

