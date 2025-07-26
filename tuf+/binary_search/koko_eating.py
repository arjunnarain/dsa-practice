import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum integer eating speed (bananas per hour) so that Koko can eat all the bananas in 'h' hours.
        Approach:
        - Use binary search to find the minimum feasible eating speed.
        - The trick: As the eating speed increases, the total hours required decreases (monotonic property), so binary search is applicable.
        - For each candidate speed, calculate the total hours needed using the helper function.
        - If Koko can finish in 'h' hours or less, try a slower speed; otherwise, try a faster speed.
        Edge cases: Handles single pile, very large piles, and when h equals the number of piles.
        """
        def calculate_total_hours(nums, hourly_eating_rate):
            # Helper function to calculate total hours needed at a given eating rate
            return sum(math.ceil(pile / hourly_eating_rate) for pile in piles)
        
        # Binary search boundaries: speed can be between 1 and max(piles)
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            # If Koko can finish eating at this speed or slower, try a slower speed
            if calculate_total_hours(piles, mid) <= h:
                high = mid - 1
            else:
                # Otherwise, try a faster speed
                low = mid + 1
        
        # The lowest speed that allows Koko to finish in h hours
        return low

        