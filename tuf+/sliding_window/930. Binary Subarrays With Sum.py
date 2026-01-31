class Solution:
    """
    Binary Subarrays With Sum (LeetCode 930).
    
    Given a binary array nums and an integer goal, return the number of non-empty
    subarrays with a sum goal.
    
    A subarray is a contiguous part of the array.
    
    Example:
        nums = [1,0,1,0,1], goal = 2
        Output: 4
        - Subarrays with sum 2: [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1]
    """
    
    def numSubarraysWithSum(self, nums, goal):
        """
        Count subarrays with exactly goal sum.
        
        Approach:
        - Use the "at most goal" technique
        - Count subarrays with sum at most goal
        - Count subarrays with sum at most (goal - 1)
        - Subtract: (at most goal) - (at most goal-1) = exactly goal
        
        Intuition:
        - Counting subarrays with exactly goal sum is tricky
        - But counting "at most goal" is easier with sliding window
        - Number of subarrays with exactly goal = Number with at most goal - Number with at most (goal-1)
        
        Key Insight:
        - This is the same pattern as problem 1248 (Count Number of Nice Subarrays)
        - Convert "exactly k" to "at most k" - "at most (k-1)"
        - Similar problems: subarrays with exactly k odd numbers, exactly k ones, etc.
        
        Args:
            nums: Binary array (contains only 0s and 1s)
            goal: Exact sum required in subarrays
            
        Returns:
            Number of subarrays with exactly goal sum
        """
        return (self._numSubarraysWithSumAtMost(nums, goal) - 
                self._numSubarraysWithSumAtMost(nums, goal - 1))
    
    def _numSubarraysWithSumAtMost(self, nums, goal):
        """
        Count subarrays with sum at most goal using sliding window.
        
        Approach:
        - Use sliding window to maintain window with sum at most goal
        - For each valid window ending at position r, count all subarrays ending at r
        - Number of such subarrays = (r - l + 1), where l is leftmost valid position
        
        Intuition:
        - We track the sum of elements in current window
        - If sum > goal, we shrink from left until sum <= goal
        - For each valid window [l, r], all subarrays ending at r with start index
          from l to r (inclusive) have sum at most goal
        - This is because: if [l, r] has sum <= goal, then [l+1, r], [l+2, r], ..., [r, r]
          all have sum <= goal (possibly smaller, but never larger)
        
        Example with nums=[1,0,1,0,1], goal=2:
        - r=0: sum=1, window=[0:0], valid, count+=1 (subarray [0:0])
        - r=1: sum=1, window=[0:1], valid, count+=2 (subarrays [0:1], [1:1])
        - r=2: sum=2, window=[0:2], valid, count+=3 (subarrays [0:2], [1:2], [2:2])
        - r=3: sum=2, window=[0:3], valid, count+=4 (subarrays [0:3], [1:3], [2:3], [3:3])
        - r=4: sum=3, invalid -> shrink to [1:4], sum=2, valid, count+=4
        - Total: 14 subarrays with sum at most 2
        
        Args:
            nums: Binary array (contains only 0s and 1s)
            goal: Maximum sum allowed in subarrays
            
        Returns:
            Number of subarrays with sum at most goal
        """
        if goal < 0:
            return 0
        
        count = 0  # Total count of valid subarrays
        current_sum = 0  # Sum of elements in current window
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        n = len(nums)
        
        # Expand window by moving right pointer
        while right < n:
            # Add current element to window
            current_sum += nums[right]
            
            # Shrink window from left if sum exceeds goal
            while current_sum > goal:
                # Remove leftmost element from window
                current_sum -= nums[left]
                left += 1
            
            # At this point, window [left:right+1] has sum at most goal
            # All subarrays ending at 'right' with start index from 'left' to 'right'
            # (inclusive) have sum at most goal
            # Number of such subarrays = right - left + 1
            count += right - left + 1
            
            # Expand window
            right += 1
        
        return count
                