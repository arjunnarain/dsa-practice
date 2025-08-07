class Solution:
    def searchMatrix(self, mat, target):
        """
        Searches for a target value in a 2D matrix where each row is sorted and the first element of each row is greater than the last element of the previous row.
        
        PATTERN RECOGNITION:
        - This is a "Search in 2D Sorted Matrix" problem
        - Key insight: The matrix can be treated as a 1D sorted array
        - The matrix has a special property: it's sorted both row-wise and column-wise
        - This allows us to use binary search by converting 2D indices to 1D
        
        INTUITION:
        - Since the matrix is sorted in a specific way, we can flatten it into a 1D array
        - Each element at position i in the 1D array corresponds to mat[i//m][i%m] in 2D
        - This conversion preserves the sorted order, making binary search applicable
        - The matrix property ensures that if we find the element, it's in the correct position
        
        APPROACH:
        1. Treat the 2D matrix as a 1D sorted array
        2. Use binary search on the flattened array indices
        3. Convert 1D index to 2D coordinates: row = mid // m, column = mid % m
        4. Compare the element at these coordinates with the target
        5. Adjust search boundaries based on the comparison
        
        SIMILAR PROBLEMS:
        - LeetCode 74: Search a 2D Matrix (this problem)
        - LeetCode 240: Search a 2D Matrix II (different property: sorted row-wise and column-wise)
        - LeetCode 378: Kth Smallest Element in a Sorted Matrix
        - LeetCode 668: Kth Smallest Number in Multiplication Table
        - LeetCode 1351: Count Negative Numbers in a Sorted Matrix
        - LeetCode 1428: Leftmost Column with at Least a One
        """
        n = len(mat)  # Number of rows
        m = len(mat[0])  # Number of columns

        # Binary search boundaries: treat matrix as 1D array with indices 0 to n*m-1
        low, high = 0, n * m - 1

        while low <= high:
            mid = (low + high) // 2

            # Convert 1D index to 2D coordinates
            row = mid // m      # Integer division gives row number
            column = mid % m    # Modulo gives column number

            # Compare the element at current position with target
            if mat[row][column] == target:
                return True
            elif mat[row][column] < target:
                # Target is in the right half of the 1D array
                low = mid + 1
            else:
                # Target is in the left half of the 1D array
                high = mid - 1
        
        # Target not found in the matrix
        return False
     