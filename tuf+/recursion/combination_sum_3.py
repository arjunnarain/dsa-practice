from typing import Any


class Solution:
    """
    Find all valid combinations of k numbers that sum up to n such that:
    - Only numbers 1-9 are used
    - Each number is used at most once
    - No duplicate combinations
    """
    
    def combinationSum3(self, k, n):
        """
        Main function to find all combinations.
        
        Args:
            k: Number of elements in each combination
            n: Target sum
            
        Returns:
            List of all valid combinations
        """
        result = []
        current_combination = []
        self._backtrack(n, 1, current_combination, k, result)
        return result

    def _backtrack(self, remaining_sum, start_num, current_combination, k, result):
        """
        Backtracking helper function.
        
        Intuition:
        - We use backtracking to explore all possible combinations
        - Start from 'start_num' to avoid duplicates (only consider numbers >= start_num)
        - This ensures combinations are in ascending order, preventing duplicates like [1,2] and [2,1]
        
        Args:
            remaining_sum: The remaining sum we need to achieve
            start_num: The smallest number we can use (to avoid duplicates)
            current_combination: Current combination being built
            k: Target number of elements
            result: List to store all valid combinations
        """
        # Base case: Valid combination found
        # We've used exactly k numbers and achieved the target sum
        if remaining_sum == 0 and len(current_combination) == k:
            result.append(list[Any](current_combination))  # Append a copy
            return
        
        # Base case: Invalid path - prune early
        # If we've exceeded the sum or used too many numbers, backtrack
        if remaining_sum <= 0 or len(current_combination) > k:
            return
        
        # Try each number from start_num to 9
        # We start from start_num to ensure combinations are in ascending order
        # This prevents duplicates and ensures we only consider each number once
        for num in range(start_num, 10):
            # Pruning: If current number is greater than remaining sum,
            # all subsequent numbers will also be greater (since they're sorted)
            # So we can break early to avoid unnecessary recursive calls
            if num > remaining_sum:
                break
            
            # Choose: Add current number to combination
            current_combination.append(num)
            
            # Explore: Recurse with updated parameters
            # - Subtract num from remaining_sum
            # - Start from num + 1 to avoid using the same number twice
            self._backtrack(remaining_sum - num, num + 1, current_combination, k, result)
            
            # Unchoose: Backtrack by removing the number we just added
            # This allows us to try other combinations
            current_combination.pop()
