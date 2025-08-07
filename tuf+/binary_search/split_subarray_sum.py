from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Finds the minimum possible value of the largest subarray sum when splitting the array into k non-empty subarrays.
        
        PATTERN RECOGNITION:
        - This is a "minimize maximum" problem - we want to minimize the largest sum
        - Key insight: If we can split into k parts with max sum <= X, we can also do it with max sum <= X+1
        - This creates a monotonic property that makes binary search applicable
        - The problem reduces to finding the minimum feasible maximum sum
        
        INTUITION:
        - We want to minimize the largest subarray sum among k subarrays
        - For any candidate max sum, we can greedily partition the array
        - If we need more than k partitions, the max sum is too low
        - If we need k or fewer partitions, the max sum might be too high (we can try lower)
        
        APPROACH:
        1. Binary search on the maximum allowed sum for each subarray
        2. For each candidate sum, greedily partition the array
        3. If we need more than k partitions, increase the sum
        4. If we need k or fewer partitions, try a lower sum
        
        SIMILAR PROBLEMS:
        - LeetCode 410: Split Array Largest Sum (this problem)
        - LeetCode 1011: Capacity To Ship Packages Within D Days
        - LeetCode 1231: Divide Chocolate
        - LeetCode 1482: Minimum Number of Days to Make m Bouquets
        - LeetCode 1552: Magnetic Force Between Two Balls
        - LeetCode 1760: Minimum Limit of Balls in a Bag
        - LeetCode 2064: Minimized Maximum of Products Distributed to Any Store
        """
        def count_partitions(nums, max_sum):
            # Helper function: count how many partitions are needed if no partition exceeds max_sum
            partition_count = 1  # Start with 1 partition
            current_partition_sum = 0

            for num in nums:
                if current_partition_sum + num <= max_sum:
                    # Can add this number to current partition
                    current_partition_sum += num
                else:
                    # Need to start a new partition here
                    partition_count += 1
                    current_partition_sum = num
            
            return partition_count
        
        # Binary search boundaries
        # Minimum possible max sum: the largest single element
        # Maximum possible max sum: sum of all elements (k=1 case)
        low, high = max(nums), sum(nums)
        
        while low <= high:
            mid = (low + high) // 2

            # If we need more than k partitions, max_sum is too low
            if count_partitions(nums, mid) > k:
                # We have more partitions than allowed, hence we will increase sum
                low = mid + 1
            else:
                # We can achieve k or fewer partitions, try a lower sum
                high = mid - 1
        
        # The minimum possible value of the largest subarray sum
        return low
            
        