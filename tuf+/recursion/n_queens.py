class Solution:
    """
    Solve the N-Queens problem: Place n queens on an n×n chessboard
    such that no two queens attack each other.
    
    Queens can attack horizontally, vertically, and diagonally.
    We need to find all distinct solutions.
    
    Example for n=4:
        [".Q..",
         "...Q",
         "Q...",
         "..Q."]
    """
    
    def solveNQueens(self, n):
        """
        Find all distinct solutions to the n-queens puzzle.
        
        Approach:
        - Place queens row by row (one queen per row)
        - For each row, try placing queen in each column
        - Use tracking arrays to quickly check if a position is safe
        - Backtrack when no valid position found
        
        Args:
            n: Size of the board (n×n) and number of queens
            
        Returns:
            List of all valid solutions, where each solution is a list of strings
            representing the board configuration
        """
        
        def backtrack(row):
            """
            Backtracking helper to place queens row by row.
            
            Intuition:
            - We place queens one row at a time (ensures no horizontal conflicts)
            - For each row, try each column position
            - Check if position is safe using pre-computed tracking arrays
            - If safe, place queen and recurse to next row
            - If we place all n queens, we have a valid solution
            - Backtrack by removing queen and restoring tracking arrays
            
            Args:
                row: Current row we're trying to place a queen in
            """
            # Base case: Successfully placed queens in all n rows
            # Convert board to solution format (list of strings)
            if row == n:
                solution = ["".join(row_chars) for row_chars in board]
                results.append(solution)
                return
            
            # Try placing queen in each column of current row
            for col in range(n):
                # Check if position (row, col) is safe
                # A position is safe if:
                # 1. Column is not used by another queen
                # 2. Main diagonal (top-left to bottom-right) is not used
                # 3. Anti-diagonal (top-right to bottom-left) is not used
                if (columns_used[col] == 0 and 
                    diagonals_used[row + col] == 0 and 
                    anti_diagonals_used[n - row + col] == 0):
                    
                    # Choose: Place queen at (row, col)
                    board[row][col] = 'Q'
                    
                    # Mark column, diagonal, and anti-diagonal as used
                    # This prevents other queens from attacking this position
                    columns_used[col] = 1
                    diagonals_used[row + col] = 1
                    anti_diagonals_used[n - row + col] = 1
                    
                    # Explore: Recurse to place queen in next row
                    backtrack(row + 1)
                    
                    # Unchoose: Backtrack by removing queen and restoring state
                    # IMPORTANT: We must restore all tracking arrays because:
                    # 1. They are mutable and shared across recursive calls
                    # 2. Other paths might need to use these positions
                    # 3. This is explicit backtracking (like pop() for lists)
                    columns_used[col] = 0
                    diagonals_used[row + col] = 0
                    anti_diagonals_used[n - row + col] = 0
                    board[row][col] = "."
        
        # Initialize tracking data structures
        results = []  # Store all valid solutions
        board = [["."] * n for _ in range(n)]  # Chessboard representation
        
        # Tracking arrays for O(1) conflict checking:
        # Instead of checking all previous queens, we use arrays to track:
        # - columns_used: which columns have queens
        # - diagonals_used: which diagonals have queens
        # - anti_diagonals_used: which anti-diagonals have queens
        
        columns_used = [0] * n  # Track columns: index = column number
        
        # Track diagonals: index = row + col
        # All cells on the same diagonal have the same (row + col) value
        # Range: 0 to 2*n-2 (for n×n board)
        diagonals_used = [0] * (2 * n)
        
        # Track anti-diagonals: index = n - row + col
        # All cells on the same anti-diagonal have the same (n - row + col) value
        # Range: 1 to 2*n-1 (for n×n board)
        # Note: We use (n - row + col) instead of (row - col) to avoid negative indices
        anti_diagonals_used = [0] * (2 * n)
        
        # Start backtracking from the first row
        backtrack(0)
        
        return results
