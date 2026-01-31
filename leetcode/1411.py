class Solution:
    """
    Number of Ways to Paint N × 3 Grid (LeetCode 1411).
    
    You have a grid of size n × 3 and want to paint each cell with one of three colors
    (Red, Yellow, or Green) such that no two adjacent cells (horizontally or vertically)
    have the same color.
    
    Return the number of ways to paint the grid. The answer must be computed modulo 10^9 + 7.
    
    Example:
        n = 1: 12 ways (3 colors for each of 3 cells, but with constraints)
        n = 2: 54 ways
    """
    
    def numOfWays(self, n):
        """
        Count number of ways to paint n×3 grid using dynamic programming.
        
        Approach:
        - Use DP to track valid patterns for each row
        - Two types of patterns: ABA (first and third same) and ABC (all different)
        - For each pattern type, count how many valid patterns of each type can follow
        
        Intuition:
        - Each row has 3 cells that need to be colored with 3 colors
        - We categorize patterns into two types based on the coloring pattern:
          * ABA pattern: First and third cells have same color (e.g., R-Y-R, G-R-G)
          * ABC pattern: All three cells have different colors (e.g., R-Y-G, G-R-Y)
        - For a 3×3 grid (first row), there are 12 total valid patterns:
          * 6 ABA patterns (2 choices for first color × 3 choices for middle color)
          * 6 ABC patterns (3! = 6 permutations of 3 colors)
        
        Recurrence Relation:
        - From an ABA pattern in row i:
          * Can create 3 new ABA patterns (middle color can be 2 new colors, but one gives ABA)
          * Can create 2 new ABC patterns
          * Total: 3 ABA + 2 ABC
        - From an ABC pattern in row i:
          * Can create 2 new ABA patterns
          * Can create 2 new ABC patterns
          * Total: 2 ABA + 2 ABC
        
        Why this works:
        - When building row i+1 based on row i, we need to ensure:
          * Row i+1 cells don't match the cell directly above
          * Row i+1 adjacent cells don't match each other
        - The pattern type determines how many valid combinations exist for the next row
        
        Example (n=2):
        - Row 1: 6 ABA + 6 ABC = 12 patterns
        - Row 2 from ABA: 6 × (3 ABA + 2 ABC) = 18 ABA + 12 ABC
        - Row 2 from ABC: 6 × (2 ABA + 2 ABC) = 12 ABA + 12 ABC
        - Total: 30 ABA + 24 ABC = 54 ways
        
        Args:
            n: Number of rows in the grid
            
        Returns:
            Number of ways to paint the grid modulo 10^9 + 7
        """
        MOD = 10**9 + 7
        
        # For the first row (3 cells), there are:
        # - 6 ABA patterns (first and third same, middle different)
        # - 6 ABC patterns (all three different)
        # Total: 12 valid patterns for first row
        aba_pattern = 6  # Count of ABA patterns for current row
        abc_pattern = 6  # Count of ABC patterns for current row
        
        # Build subsequent rows using DP
        # We already have row 0, so we need to build rows 1 to n-1
        for _ in range(n - 1):
            # Calculate new pattern counts based on recurrence relation
            # From each ABA pattern: can create 3 new ABA + 2 new ABC patterns
            # From each ABC pattern: can create 2 new ABA + 2 new ABC patterns
            new_aba_pattern = (3 * aba_pattern + 2 * abc_pattern) % MOD
            new_abc_pattern = (2 * aba_pattern + 2 * abc_pattern) % MOD
            
            # Update for next iteration
            aba_pattern, abc_pattern = new_aba_pattern, new_abc_pattern
        
        # Total ways = sum of all valid patterns in the last row
        return (aba_pattern + abc_pattern) % MOD