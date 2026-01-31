class Solution:
    """
    Minimum Window Substring (LeetCode 76).
    
    Given two strings s and t, return the minimum window substring of s such that
    every character in t (including duplicates) is included in the window.
    If there is no such substring, return an empty string "".
    
    Example:
        s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        - The minimum window substring "BANC" includes 'A', 'B', and 'C'.
    """
    
    def minWindow(self, s, t):
        """
        Find minimum window substring containing all characters of t.
        
        Approach:
        - Use sliding window technique with two pointers
        - Track character requirements using hash array
        - Expand window to include all required characters
        - Shrink window to find minimum valid window
        - Use counter to track how many characters from t are satisfied
        
        Intuition:
        - We need to find the shortest substring in s that contains all chars in t
        - Use a hash array to track how many of each character we need
        - Positive values = characters we still need
        - Zero/negative values = characters we have in excess or don't need
        - Counter tracks how many characters from t we've successfully included
        
        Key Insight:
        - When we see a character that's needed (hash[char] > 0), increment count
        - When count == len(t), we have all required characters (valid window)
        - Then we shrink from left to find minimum window
        - When shrinking, if hash[char] becomes positive, we're losing a needed char
        
        Example with s="ADOBECODEBANC", t="ABC":
        - Initial hash: A=1, B=1, C=1 (other chars = 0)
        - Expand to "ADOBEC": count=3 (all found), window len=6, min="ADOBEC"
        - Shrink to "DOBEC": count=3, window len=5, min="DOBEC"
        - Shrink to "OBEC": count=3, window len=4, min="OBEC"
        - Shrink to "BEC": count=3, window len=3, min="BEC"
        - Shrink to "EC": count=2 (lost B), expand again...
        - Continue until find "BANC" with len=4
        
        Args:
            s: Source string
            t: Target string (characters we need to find in s)
            
        Returns:
            Minimum window substring containing all characters of t, or ""
        """
        min_len = float('inf')  # Minimum window length found so far
        start_index = -1  # Starting index of minimum window
        
        # Hash array to track character requirements
        # Index represents ASCII value of character
        # Positive value = we still need this many of this character
        # Zero/negative value = we have enough (or excess) of this character
        char_need = [0] * 256
        
        # Initialize: count how many of each character we need from t
        for c in t:
            char_need[ord(c)] += 1
        
        count = 0  # Number of characters from t we've successfully included
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        
        # Expand window by moving right pointer
        while right < len(s):
            char_r = s[right]
            char_r_code = ord(char_r)
            
            # If this character is needed (char_need > 0), we've found one more required char
            if char_need[char_r_code] > 0:
                count += 1
            
            # Decrement the count for this character (even if not needed)
            # This makes non-needed characters negative
            char_need[char_r_code] -= 1
            
            # When we have all required characters (count == len(t)), try to shrink window
            while count == len(t):
                # Update minimum window if current window is smaller
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    start_index = left
                
                # Try to shrink from left
                char_l = s[left]
                char_l_code = ord(char_l)
                
                # Increment back the count for leftmost character
                char_need[char_l_code] += 1
                
                # If this character becomes positive, we're losing a needed character
                # This means we no longer have all required characters
                if char_need[char_l_code] > 0:
                    count -= 1
                
                # Move left pointer to shrink window
                left += 1
            
            # Expand window
            right += 1
        
        # Return the minimum window substring, or empty string if not found
        return s[start_index:start_index + min_len] if start_index != -1 else ""