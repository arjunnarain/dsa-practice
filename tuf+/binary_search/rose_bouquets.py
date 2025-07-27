from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        Finds the minimum number of days needed to make 'm' bouquets, where each bouquet requires 'k' consecutive blooming roses.
        Approach:
        - Use binary search to find the minimum feasible number of days.
        - The trick: As the number of days increases, the number of possible bouquets increases (monotonic property), so binary search is applicable.
        - For each candidate day, calculate the number of possible bouquets using the helper function.
        - If we can make 'm' or more bouquets, try fewer days; otherwise, try more days.
        Edge cases: If the total number of roses is less than m*k, it's impossible to make the required bouquets.
        """
        n = len(bloomDay)
        def possible_bouquets(nums, k, days):
            # Helper function to calculate the number of bouquets possible in 'days'
            consecutive = 0
            bouquets = 0
            for bloom_day in nums:
                if bloom_day <= days:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0
            
            return bouquets
        # Edge case: If we don't have enough roses, return -1
        if n < m * k:
            return -1
        # Binary search boundaries: days can be between min and max bloom days
        low, high = min(bloomDay), max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            # If we can make 'm' or more bouquets, try fewer days
            if possible_bouquets(bloomDay, k, mid) >= m:
                high = mid - 1
            else:
                # Otherwise, try more days
                low = mid + 1

        # The minimum number of days needed to make 'm' bouquets
        return low 
        