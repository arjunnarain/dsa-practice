class Solution:
    """
    Count Number of Nice Subarrays (LeetCode 1248).
    
    Given an array of integers nums and an integer k. A continuous subarray is called nice
    if there are k odd numbers on it.
    
    Return the number of nice sub-arrays.
    
    Example:
        nums = [1,1,2,1,1], k = 3
        Output: 2
        - Nice subarrays: [1,1,2,1] and [1,2,1,1] (both have exactly 3 odd numbers)
    """
    
    def numberOfSubarrays(self, nums, k):
        """
        Count subarrays with exactly k odd numbers.
        
        Approach:
        - Use the "at most k" technique
        - Count subarrays with at most k odd numbers
        - Count subarrays with at most (k-1) odd numbers
        - Subtract: (at most k) - (at most k-1) = exactly k
        
        Intuition:
        - Counting subarrays with exactly k odd numbers is tricky
        - But counting "at most k" is easier with sliding window
        - Number of subarrays with exactly k = Number with at most k - Number with at most (k-1)
        
        Key Insight:
        - This is a common pattern: convert "exactly k" to "at most k" - "at most (k-1)"
        - Similar problems: subarrays with exactly k distinct elements, exactly k ones, etc.
        
        Args:
            nums: Array of integers
            k: Exact number of odd numbers required in nice subarrays
            
        Returns:
            Number of subarrays with exactly k odd numbers
        """
        return (self._numberOfOddSubarraysAtMost(nums, k) - 
                self._numberOfOddSubarraysAtMost(nums, k - 1))

    def _numberOfOddSubarraysAtMost(self, nums, k):
        """
        Count subarrays with at most k odd numbers using sliding window.
        
        Approach:
        - Use sliding window to maintain window with at most k odd numbers
        - For each valid window ending at position r, count all subarrays ending at r
        - Number of such subarrays = (r - l + 1), where l is leftmost valid position
        
        Intuition:
        - We track the count of odd numbers in current window
        - If count > k, we shrink from left until count <= k
        - For each valid window [l, r], all subarrays ending at r with start index
          from l to r (inclusive) have at most k odd numbers
        - This is because: if [l, r] has at most k odds, then [l+1, r], [l+2, r], ..., [r, r]
          all have at most k odds (possibly fewer, but never more)
        
        Example with nums=[1,1,2,1,1], k=2:
        - r=0: odd_count=1, window=[0:0], valid, count+=1 (subarray [0:0])
        - r=1: odd_count=2, window=[0:1], valid, count+=2 (subarrays [0:1], [1:1])
        - r=2: odd_count=2, window=[0:2], valid, count+=3 (subarrays [0:2], [1:2], [2:2])
        - r=3: odd_count=3, invalid -> shrink to [1:3], odd_count=2, valid, count+=3
        - r=4: odd_count=3, invalid -> shrink to [2:4], odd_count=2, valid, count+=3
        - Total: 12 subarrays with at most 2 odd numbers
        
        Args:
            nums: Array of integers
            k: Maximum number of odd numbers allowed in subarrays
            
        Returns:
            Number of subarrays with at most k odd numbers
        """
        if k < 0:
            return 0
        
        count = 0  # Total count of valid subarrays
        odd_count = 0  # Count of odd numbers in current window
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        n = len(nums)
        
        # Expand window by moving right pointer
        while right < n:
            # Add current element to window
            # nums[r] % 2 gives 1 if odd, 0 if even
            odd_count += nums[right] % 2
            
            # Shrink window from left if we have more than k odd numbers
            while odd_count > k:
                # Remove leftmost element from window
                odd_count -= nums[left] % 2
                left += 1
            
            # At this point, window [left:right+1] has at most k odd numbers
            # All subarrays ending at 'right' with start index from 'left' to 'right'
            # (inclusive) have at most k odd numbers
            # Number of such subarrays = right - left + 1
            count += right - left + 1
            
            # Expand window
            right += 1
        
        return count