class Solution:
    def aggressiveCows(self, nums, k):
        """
        Finds the largest minimum distance possible between any two of the k cows placed in the stalls.
        Approach:
        - Sort the stall positions to allow binary search on distances.
        - Use binary search to find the largest minimum distance that allows placing all cows.
        - The trick: As the minimum distance increases, it becomes harder to place all cows (monotonic property), so binary search is applicable.
        - For each candidate distance, use the helper function to check if it's possible to place all cows.
        Edge cases: Handles when k > len(nums), or when all stalls are at the same position.
        """
        nums.sort()
        def can_we_place(nums, k, distance):
            # Helper function to check if we can place k cows with at least 'distance' between them
            n = len(nums)
            current_cow_stall = nums[0]
            cows_placed = 1

            for i in range(1, n ):
                stall = nums[i]
                if stall - current_cow_stall >= distance:
                    current_cow_stall = stall
                    cows_placed += 1
            
            # If we can place at least k cows, return 1 (True), else 2 (False)
            if cows_placed >= k:
                return 1
            else:
                return 2
        
        # Binary search boundaries: minimum distance can be between 0 and the largest gap
        low, high = 0, max(nums) - min(nums)
 
        while low <= high:
            mid = (low + high) // 2
            # If we can place all cows with at least 'mid' distance, try for a larger distance
            if can_we_place(nums, k, mid) == 1:
                low = mid + 1
            else:
                # Otherwise, try a smaller distance
                high = mid - 1
        
        # The largest minimum distance possible
        return high
        