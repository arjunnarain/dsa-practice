class Solution:
    """
    Find all possible palindrome partitions of a string.
    
    A palindrome partition is a way to split the string such that
    every substring of the partition is a palindrome.
    
    Example: "aab" -> [["a","a","b"], ["aa","b"]]
    """
    
    def partition(self, s):
        """
        Main function to find all palindrome partitions.
        
        Approach:
        1. Pre-compute palindrome information using DP (optimization)
        2. Use backtracking to explore all valid partitions
        
        Args:
            s: Input string to partition
            
        Returns:
            List of all valid palindrome partitions
        """
        
        def backtrack(start_index):
            """
            Backtracking helper to find all palindrome partitions.
            
            Intuition:
            - We try to extend the current partition by considering all possible substrings starting from start_index
            - For each valid palindrome found, we add it to the partition and
              recursively process the remaining substring
            - When we reach the end of the string, we have a valid partition
            
            Example with "aab":
            - Start at index 0: try "a" (palindrome) -> recurse on "ab"
            - In "ab": try "a" -> recurse on "b" -> try "b" -> valid: ["a","a","b"]
            - Backtrack: try "aa" (palindrome) -> recurse on "b"
            - In "b": try "b" -> valid: ["aa","b"]
            
            Args:
                start_index: Current position in the string to start partitioning from
            """
            # Base case: We've processed the entire string
            # Add the current partition (a copy) to results
            if start_index == string_length:
                result.append(current_partition[:])  # Append a copy of the list
                return
          
            # Try all possible substrings starting from start_index
            # We check if s[start_index:end_index+1] is a palindrome
            for end_index in range(start_index, string_length):
                # Use pre-computed DP table for O(1) palindrome check
                if is_palindrome[start_index][end_index]:
                    # Choose: Add this palindromic substring to current partition
                    current_partition.append(s[start_index : end_index + 1])
                    
                    # Explore: Recursively partition the remaining string
                    backtrack(end_index + 1)
                    
                    # Unchoose: Backtrack by removing the last added substring
                    # IMPORTANT: We must pop() because we're using a mutable list
                    # Unlike strings (immutable), lists are shared across recursive calls
                    # So we need explicit backtracking to undo our choice
                    current_partition.pop()
      
        string_length = len(s)
      
        # Pre-compute palindrome information using Dynamic Programming
        # This optimization avoids repeated palindrome checks during backtracking
        # Instead of checking each substring repeatedly, we compute once and reuse
        #
        # is_palindrome[i][j] = True if substring s[i:j+1] is a palindrome
        # Initialize all to True (single characters are implicitly palindromes)
        is_palindrome = [[True] * string_length for _ in range(string_length)]
        
        # Fill the DP table bottom-up (process shorter substrings first)
        # We iterate from right to left for starting position
        # This ensures that when we check is_palindrome[i+1][j-1], it's already computed
        for i in range(string_length - 1, -1, -1):
            # For each starting position i, check all ending positions j > i
            for j in range(i + 1, string_length):
                # A substring s[i:j+1] is a palindrome if:
                # 1. First and last characters match: s[i] == s[j]
                # 2. Inner substring is also a palindrome: is_palindrome[i+1][j-1]
                # 
                # Note: For length 2 (j == i+1), is_palindrome[i+1][j-1] = is_palindrome[i+1][i]
                #       which is True (initialized), so we just check s[i] == s[j]
                is_palindrome[i][j] = s[i] == s[j] and is_palindrome[i + 1][j - 1]
      
        # Initialize result list and current partition tracker
        result = []
        current_partition = []  # Mutable list - requires explicit backtracking with pop()
      
        # Start backtracking from the beginning of the string
        backtrack(0)
      
        return result
