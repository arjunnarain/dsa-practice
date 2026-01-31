class Solution:
    """
    Find the length of the longest substring with same character after at most k replacements.
    
    You can choose any character of the string and change it to any other uppercase
    English character. You can perform this operation at most k times.
    
    Return the length of the longest substring containing the same letter you can get
    after performing the above operations.
    
    Example:
        s = "ABAB", k = 2
        Output: 4
        - Replace the two 'A's with two 'B's or vice versa: "BBBB" or "AAAA"
        
        s = "AABABBA", k = 1
        Output: 4
        - Replace the one 'A' in the middle with 'B': "AABBBBA"
        - Longest substring "BBBB" has length 4
    """
    
    def characterReplacement(self, s, k):
        """
        Find longest substring with same character after at most k replacements.
        
        Approach:
        - Use sliding window technique with two pointers
        - Track frequency of each character in current window
        - Track maximum frequency of any character in current window
        - If (window_size - max_freq) > k, we need more than k replacements -> shrink
        - Track maximum valid window size
        
        Intuition:
        - In a valid window, we want to make all characters the same
        - The minimum replacements needed = window_size - frequency_of_most_common_char
        - If this is <= k, the window is valid
        - We expand the window and shrink when it becomes invalid
        
        Key Insight (Optimization):
        - We don't need to recalculate maxFreq when shrinking!
        - maxFreq only increases or stays the same when we expand
        - When we shrink, the current window might have lower maxFreq, but that's okay
        - We're tracking maximum window size, and we've already considered windows
          with higher maxFreq
        - This works because: if a smaller window with lower maxFreq is valid,
          a larger window with higher maxFreq would also be valid (and we've seen it)
        
        Example with s="AABABBA", k=1:
        - Window [0:1]: freq={'A':1}, maxFreq=1, replacements=0, valid, len=1, max=1
        - Window [0:2]: freq={'A':2}, maxFreq=2, replacements=0, valid, len=2, max=2
        - Window [0:3]: freq={'A':2,'B':1}, maxFreq=2, replacements=1, valid, len=3, max=3
        - Window [0:4]: freq={'A':2,'B':2}, maxFreq=2, replacements=2, invalid -> shrink
        - Window [1:4]: freq={'A':1,'B':2}, maxFreq=2 (not recalculated!), replacements=1, valid, len=3, max=3
        - Window [1:5]: freq={'A':1,'B':3}, maxFreq=3, replacements=1, valid, len=4, max=4
        - Window [1:6]: freq={'A':2,'B':3}, maxFreq=3, replacements=1, valid, len=5, max=5
        - Window [1:7]: freq={'A':3,'B':3}, maxFreq=3, replacements=1, valid, len=6, max=6
        
        Args:
            s: String containing only uppercase English letters
            k: Maximum number of character replacements allowed
            
        Returns:
            Length of longest substring with same character after at most k replacements
        """
        max_len = 0  # Maximum valid window size found so far
        max_freq = 0  # Maximum frequency of any character in current window
        
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        
        # Array to track frequency of each character (A-Z)
        # Index 0-25 represents characters 'A' to 'Z'
        char_freq = [0] * 26
        
        # Expand window by moving right pointer
        while right < len(s):
            # Add current character to window and update its frequency
            char_index = ord(s[right]) - ord('A')
            char_freq[char_index] += 1
            
            # Update maximum frequency seen so far
            # This only increases or stays the same (never decreases)
            max_freq = max(max_freq, char_freq[char_index])
            
            # Check if current window is valid
            # Window is valid if: (window_size - max_freq) <= k
            # This means we need at most k replacements to make all chars same
            window_size = right - left + 1
            if window_size - max_freq > k:
                # Window is invalid (needs more than k replacements)
                # Shrink from left
                char_freq[ord(s[left]) - ord('A')] -= 1
                left += 1
                # Note: We don't recalculate max_freq here (optimization)
                # The current window might have lower max_freq, but that's okay
                # We've already considered windows with higher max_freq
            
            # At this point, window [left:right+1] is valid
            # Calculate current window size and update maximum
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            
            # Expand window
            right += 1
        
        return max_len