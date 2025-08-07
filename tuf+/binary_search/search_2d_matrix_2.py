class Solution:
    def searchMatrix(self, matrix, target):
        """
        Searches for a target value in a 2D matrix where each row is sorted from left to right,
        and each column is sorted from top to bottom.
        
        PATTERN RECOGNITION:
        - This is "Search a 2D Matrix II" (LeetCode 240) - different from the previous problem
        - Key insight: Start from top-right corner and eliminate one row or column at a time
        - The matrix has a special property: sorted both row-wise AND column-wise
        - This allows us to use a "staircase" approach instead of binary search
        
        INTUITION:
        - Starting from top-right corner gives us maximum information
        - If target < current element, it can't be in the current column (all elements below are larger)
        - If target > current element, it can't be in the current row (all elements to left are smaller)
        - This creates a "staircase" pattern where we move left or down based on comparison
        - Each comparison eliminates either an entire row or an entire column
        
        APPROACH:
        1. Start from top-right corner (row=0, col=m-1)
        2. If target == current element, return True
        3. If target < current element, move left (eliminate current column)
        4. If target > current element, move down (eliminate current row)
        5. Continue until we go out of bounds
        
        TIME COMPLEXITY: O(n + m) where n = rows, m = columns
        SPACE COMPLEXITY: O(1) - only using a few variables
        
        SIMILAR PROBLEMS:
        - LeetCode 240: Search a 2D Matrix II (this problem)
        - LeetCode 74: Search a 2D Matrix (different property - sorted as 1D array)
        - LeetCode 378: Kth Smallest Element in a Sorted Matrix
        - LeetCode 668: Kth Smallest Number in Multiplication Table
        - LeetCode 1351: Count Negative Numbers in a Sorted Matrix
        - LeetCode 1428: Leftmost Column with at Least a One
        """
        n, m = len(matrix), len(matrix[0])  # Get matrix dimensions

        # Start from top-right corner - this is the key insight!
        row, col = 0, m - 1

        # Staircase approach: move left or down based on comparison
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True  # Target found!
            elif matrix[row][col] < target:
                # Target is larger, so it must be in a row below (all elements to left are smaller)
                row += 1
            else:
                # Target is smaller, so it must be in a column to the left (all elements below are larger)
                col -= 1
        
        # Target not found in the matrix
        return False