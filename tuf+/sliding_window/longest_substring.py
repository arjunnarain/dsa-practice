class Solution:
    """
    Find the length of the longest substring with at most k distinct characters.
    
    Given a string s and an integer k, return the length of the longest substring
    that contains at most k distinct characters.
    
    Example:
        s = "eceba", k = 2
        Output: 3 (substring "ece" has 2 distinct characters: 'e' and 'c')
        
        s = "aa", k = 1
        Output: 2 (substring "aa" has 1 distinct character: 'a')
    """
    
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Find longest substring with at most k distinct characters using sliding window.
        
        Approach:
        - Use sliding window technique with two pointers
        - Track count of each character using hash map
        - Expand window by moving right pointer
        - If we have more than k distinct characters, shrink from left until valid
        - Track maximum valid window size
        
        Intuition:
        - We want the longest subarray with at most k distinct characters
        - As we expand the window, we add characters to our collection
        - If we encounter more than k distinct characters, we need to remove
          characters from the left until we have at most k distinct characters
        - We use a hash map to track how many of each character we have
        - When count of a character reaches 0, we remove it from the map
        
        Key Insight:
        - We don't need to track which specific characters, just the count of distinct ones
        - When shrinking, we decrement count of leftmost character
        - If count becomes 0, we remove it from map (now we have <= k distinct chars)
        - The maximum window size we achieve = answer
        
        Example with s="eceba", k=2:
        - Window [0:1]: chars={'e':1}, distinct=1, valid, len=1, max=1
        - Window [0:2]: chars={'e':1,'c':1}, distinct=2, valid, len=2, max=2
        - Window [0:3]: chars={'e':2,'c':1}, distinct=2, valid, len=3, max=3
        - Window [0:4]: chars={'e':2,'c':1,'b':1}, distinct=3, invalid -> shrink left
        - Window [1:4]: chars={'e':1,'c':1,'b':1}, distinct=3, invalid -> shrink left
        - Window [2:4]: chars={'c':1,'b':1}, distinct=2, valid, len=2, max=3
        - Window [2:5]: chars={'c':1,'b':1,'a':1}, distinct=3, invalid -> shrink left
        - Window [3:5]: chars={'b':1,'a':1}, distinct=2, valid, len=2, max=3
        
        Args:
            s: Input string
            k: Maximum number of distinct characters allowed in substring
            
        Returns:
            Length of longest substring with at most k distinct characters
        """
        n = len(s)
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        max_len = 0  # Maximum valid window size found so far
        
        # Hash map to track count of each character in current window
        # Key: character, Value: count of that character in window
        char_count = {}
        
        # Expand window by moving right pointer
        while right < n:
            # Add current character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            
            # If we have more than k distinct characters, shrink window from left
            # Keep shrinking until we have at most k distinct characters
            if len(char_count) > k:
                # Remove leftmost character from window
                char_count[s[left]] -= 1
                
                # If count becomes 0, remove from map (no longer in window)
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                
                # Move left pointer to shrink window
                left += 1
            
            # At this point, window [left:right+1] is valid (has <= k distinct chars)
            # Calculate current window size and update maximum
            if len(char_count) <= k:
                max_len = max(max_len, right - left + 1)
            
            # Expand window
            right += 1
        
        return max_len