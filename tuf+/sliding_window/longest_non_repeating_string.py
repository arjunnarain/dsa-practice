class Solution:
    """
    Find the length of the longest substring without repeating characters.
    
    Example:
        Input: "abcabcbb"
        Output: 3 (substring "abc" or "bca" or "cab")
    """
    
    def lengthOfLongestSubstring(self, s):
        """
        Find longest substring without repeating characters using sliding window.
        
        Approach:
        - Use sliding window technique with two pointers (left, right)
        - Track last seen position of each character using array (hash map)
        - Expand window by moving right pointer
        - Shrink window by moving left pointer when duplicate found
        - Track maximum window size
        
        Intuition:
        - As we expand the window (move right pointer), we check for duplicates
        - If we've seen the current character before, we move left pointer
          to the position AFTER the last occurrence of that character
        - This ensures our window always contains unique characters
        - We use max() to ensure left pointer only moves forward (never backward)
        
        Key Insight:
        - When we find a duplicate at position r, we don't necessarily move
          left to hash[s[r]] + 1 immediately
        - We use max() because left might already be ahead if we encountered
          another duplicate earlier
        - Example: "abba" - when r=3 (second 'a'), hash['a']=0, but left=2
          (from handling 'b' at r=2), so we don't move left backward
        
        Example with "abcabcbb":
        - r=0 ('a'): last_seen['a']=-1, window=[0:1], len=1, max=1
        - r=1 ('b'): last_seen['b']=-1, window=[0:2], len=2, max=2
        - r=2 ('c'): last_seen['c']=-1, window=[0:3], len=3, max=3
        - r=3 ('a'): last_seen['a']=0, left=max(1,0)=1, window=[1:4], len=3, max=3
        - r=4 ('b'): last_seen['b']=1, left=max(2,1)=2, window=[2:5], len=3, max=3
        - r=5 ('c'): last_seen['c']=2, left=max(3,2)=3, window=[3:6], len=3, max=3
        - r=6 ('b'): last_seen['b']=4, left=max(5,3)=5, window=[5:7], len=2, max=3
        - r=7 ('b'): last_seen['b']=6, left=max(7,5)=7, window=[7:8], len=1, max=3
        
        Args:
            s: Input string
            
        Returns:
            Length of longest substring without repeating characters
        """
        n = len(s)
        HASH_SIZE = 256  # ASCII character set size
        
        # Track last seen index of each character
        # last_seen[char_code] = last index where this character appeared
        # Initialize to -1 (not seen yet)
        last_seen = [-1] * HASH_SIZE
        
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        max_len = 0  # Maximum length of valid substring found so far
        
        # Expand window by moving right pointer
        while right < n:
            char_code = ord(s[right])
            
            # If we've seen this character before within current window
            # Move left pointer to skip the previous occurrence
            if last_seen[char_code] != -1:
                # Use max() to ensure left only moves forward, never backward
                # This handles cases where left is already ahead due to
                # a previous duplicate we handled
                left = max(last_seen[char_code] + 1, left)
            
            # Calculate current window size and update maximum
            current_len = right - left + 1
            max_len = max(max_len, current_len)
            
            # Update last seen position of current character
            last_seen[char_code] = right
            
            # Expand window
            right += 1
        
        return max_len