class Solution:
    """
    Find the longest subarray of 1s with at most k zeros that can be flipped.
    
    Given a binary array and an integer k, return the maximum number of
    consecutive 1s in the array if you can flip at most k 0s to 1s.
    
    Example:
        nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
        Output: 6
        - Flip two 0s in the middle: [1,1,1,1,1,1,1,1,1,1,0]
        - Longest subarray of 1s has length 6 (or more)
    """
    
    def longestOnes(self, nums, k):
        """
        Find longest subarray with at most k zeros using sliding window.
        
        Approach:
        - Use sliding window technique with two pointers
        - Expand window by moving right pointer
        - Count zeros in current window
        - If zeros exceed k, shrink window from left until valid
        - Track maximum valid window size
        
        Intuition:
        - We want the longest subarray with at most k zeros
        - This is equivalent to: longest subarray where we can flip at most k 0s
        - As we expand the window, if we have more than k zeros, we need to
          shrink from the left until we have at most k zeros again
        - The maximum window size we achieve = answer
        
        Key Insight:
        - We don't actually flip the zeros, we just count them
        - If a window has <= k zeros, we can flip them all to get all 1s
        - We want the maximum such window
        
        Example with nums=[1,1,1,0,0,0,1,1,1,1,0], k=2:
        - Window [0:3]: zeros=0, valid, len=3, max=3
        - Window [0:4]: zeros=1, valid, len=4, max=4
        - Window [0:5]: zeros=2, valid, len=5, max=5
        - Window [0:6]: zeros=3, invalid -> shrink left
        - Window [1:6]: zeros=2, valid, len=5, max=5
        - Window [1:7]: zeros=2, valid, len=6, max=6
        - ... continue expanding
        
        Args:
            nums: Binary array (contains only 0s and 1s)
            k: Maximum number of zeros allowed in the subarray
            
        Returns:
            Length of longest subarray with at most k zeros
        """
        n = len(nums)
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        zeros = 0  # Count of zeros in current window
        max_len = 0  # Maximum valid window size found so far
        
        # Expand window by moving right pointer
        while right < n:
            # Count zeros as we expand
            if nums[right] == 0:
                zeros += 1
            
            # Shrink window from left if we have too many zeros
            # Keep shrinking until window is valid (zeros <= k)
            while zeros > k:
                # If leftmost element is a zero, decrement zero count
                if nums[left] == 0:
                    zeros -= 1
                # Move left pointer to shrink window
                left += 1
            
            # At this point, window [left:right+1] is valid (has <= k zeros)
            # Calculate current window size and update maximum
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)
            
            # Expand window
            right += 1
        
        return max_len



