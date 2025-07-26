import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        Finds the smallest integer divisor such that the sum of the ceiling of each number divided by the divisor
        is less than or equal to the threshold.
        Approach:
        - Use binary search to efficiently find the smallest divisor.
        - The trick: As the divisor increases, the sum decreases (monotonic property), so binary search is applicable.
        - For each candidate divisor, calculate the sum using the helper function.
        - If the sum is within the threshold, try smaller divisors; otherwise, try larger divisors.
        Edge case: If the number of elements is greater than the threshold, it's impossible to satisfy the condition.
        """
        n = len(nums)
        if n > threshold:
            return -1  # Edge case: Not possible if more elements than threshold
        # Binary search boundaries: divisor can be between 1 and max(nums)
        low, high = 1, max(nums)
        min_divisor = -1
        while low <= high:
            mid = (low + high) // 2
            # Calculate the sum for the current divisor
            current_sum = self.calculate_sum(nums, mid)
            if current_sum <= threshold:
                # If sum is within threshold, try to find a smaller divisor
                min_divisor = mid
                high = mid - 1
            else:
                # If sum exceeds threshold, need a larger divisor
                low = mid + 1 # higher the divisor lower the sum.
        return min_divisor

    def calculate_sum(self, nums, divisor):
        # Helper function to calculate the sum of ceilings for each element divided by divisor
        return sum(math.ceil(num / divisor) for num in nums)
        