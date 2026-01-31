class Solution:
    """
    Number of Substrings Containing All Three Characters (LeetCode 1358).
    
    Given a string s consisting only of characters a, b, and c.
    Return the number of substrings containing at least one occurrence of all three characters a, b, and c.
    
    Example:
        s = "abcabc"
        Output: 10
        - Valid substrings: "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc",
          "cab", "cabc", "abc" (second occurrence)
    """
    
    def numberOfSubstrings(self, s):
        """
        Count number of substrings containing all three characters (a, b, c).
        
        Approach:
        - Track the last seen index of each character (a, b, c)
        - For each position i, check if all three have been seen
        - If yes, all substrings starting from 0 to min(last_seen) and ending at i are valid
        
        Intuition:
        - For a substring ending at position i to contain all three characters,
          all three must have appeared at or before position i
        - The minimum of the three last_seen indices (min_idx) tells us the leftmost
          position where all three characters have been seen
        - All substrings starting from index 0 to min_idx (inclusive) and ending at i
          will contain all three characters
        - Number of such substrings = min_idx + 1 (indices 0, 1, 2, ..., min_idx)
        
        Key Insight:
        - We don't need to check every substring explicitly
        - Once we know all three have been seen, we can calculate how many valid
          substrings end at current position using the minimum last_seen index
        - This is O(n) time instead of O(n²) brute force
        
        Example with s="abcabc":
        - i=0 ('a'): last_seen=[0,-1,-1], not all seen, count=0
        - i=1 ('b'): last_seen=[0,1,-1], not all seen, count=0
        - i=2 ('c'): last_seen=[0,1,2], all seen! min=0, count+=1+0=1
          (substring "abc" starting at 0)
        - i=3 ('a'): last_seen=[3,1,2], all seen! min=1, count+=1+1=3
          (substrings "abca", "bca" starting at 0,1)
        - i=4 ('b'): last_seen=[3,4,2], all seen! min=2, count+=1+2=6
          (substrings "abcab", "bcab", "cab" starting at 0,1,2)
        - i=5 ('c'): last_seen=[3,4,5], all seen! min=3, count+=1+3=10
          (substrings "abcabc", "bcabc", "cabc", "abc" starting at 0,1,2,3)
        
        Args:
            s: String consisting only of characters 'a', 'b', and 'c'
            
        Returns:
            Number of substrings containing at least one occurrence of all three characters
        """
        # Track last seen index of each character: [a, b, c]
        # Initialize to -1 (not seen yet)
        last_seen = [-1, -1, -1]
        
        count = 0  # Total count of valid substrings
        
        # Process each character in the string
        for i in range(len(s)):
            # Update last seen index for current character
            # Map 'a'->0, 'b'->1, 'c'->2
            char_index = ord(s[i]) - ord('a')
            last_seen[char_index] = i
            
            # Check if all three characters have been seen at least once
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                # All three characters have been seen
                # Find the minimum last_seen index (leftmost position where all three exist)
                min_last_seen = min(last_seen[0], last_seen[1], last_seen[2])
                
                # All substrings starting from index 0 to min_last_seen (inclusive)
                # and ending at i contain all three characters
                # Number of such substrings = min_last_seen + 1
                count += 1 + min_last_seen
        
        return count
        