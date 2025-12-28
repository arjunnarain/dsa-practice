class Solution:
    """
    Determine if a word exists in a 2D board.
    
    The word can be constructed from letters of sequentially adjacent cells,
    where "adjacent" cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    
    Example:
        board = [["A","B","C","E"],
                 ["S","F","C","S"],
                 ["A","D","E","E"]]
        word = "ABCCED" -> True
    """
    
    def exist(self, board, word):
        """
        Main function to check if word exists in board.
        
        Approach:
        - Try starting from each cell in the board
        - Use backtracking/DFS to explore all paths
        - Mark visited cells to avoid cycles
        - Restore cells when backtracking
        
        Args:
            board: 2D list of characters
            word: String to search for
            
        Returns:
            True if word exists, False otherwise
        """
        
        def backtrack(row, col, word_index):
            """
            Backtracking helper to search for word starting from (row, col).
            
            Intuition:
            - We use DFS to explore all possible paths from current cell
            - Mark current cell as visited (with "#") to prevent revisiting
            - Try all 4 directions (up, right, down, left)
            - If we find the word, return True immediately
            - Restore cell when backtracking (undo our choice)
            
            Example with word "AB":
            - Start at cell with 'A': mark as "#", try neighbors
            - Find neighbor with 'B': mark as "#", check if it's last char -> True
            - Backtrack: restore 'B', restore 'A'
            
            Args:
                row: Current row index
                col: Current column index
                word_index: Current position in the word we're matching
                
            Returns:
                True if word can be found from this path, False otherwise
            """
            # Base case: We're at the last character of the word
            # Check if current cell matches the last character
            if word_index == len(word) - 1:
                return board[row][col] == word[word_index]
            
            # Early termination: Current cell doesn't match expected character
            if board[row][col] != word[word_index]:
                return False
            
            # Choose: Mark current cell as visited to prevent cycles
            # We temporarily modify the board to track visited cells
            # This is more memory-efficient than maintaining a separate visited set
            original_char = board[row][col]
            board[row][col] = "#"  # Mark as visited
            
            # Define 4 possible directions: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            
            # Explore: Try all adjacent cells
            for dr, dc in directions:
                next_row = row + dr
                next_col = col + dc
                
                # Check if next cell is valid:
                # 1. Within board boundaries
                # 2. Not already visited (not marked as "#")
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    board[next_row][next_col] != "#"):
                    
                    # Recursively search from next cell
                    if backtrack(next_row, next_col, word_index + 1):
                        # Found the word! Restore cell before returning
                        board[row][col] = original_char
                        return True
            
            # Unchoose: Restore cell when backtracking
            # IMPORTANT: We must restore the original character because:
            # 1. The board is mutable and shared across recursive calls
            # 2. Other paths might need to use this cell
            # 3. This is explicit backtracking (like pop() for lists)
            board[row][col] = original_char
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        # Try starting the search from every cell in the board
        # The word might start from any position
        for start_row in range(rows):
            for start_col in range(cols):
                if backtrack(start_row, start_col, 0):
                    return True
        
        return False
