class Solution:
    """
    Find the maximum amount of gold you can collect in a grid.
    
    Rules:
    - You can start from any cell with gold (non-zero value)
    - You can move up, down, left, right
    - You cannot visit the same cell twice
    - You cannot visit cells with 0 gold (obstacles)
    - You can stop at any time
    
    Example:
        grid = [[0,6,0],
                [5,8,7],
                [0,9,0]]
        Maximum gold path: 9 -> 8 -> 7 = 24
    """
    
    def getMaximumGold(self, grid):
        """
        Find maximum gold collectible from any starting position.
        
        Approach:
        - Try starting from every cell with gold
        - Use DFS to explore all paths from each starting position
        - Track maximum gold collected along any path
        - Mark visited cells to avoid cycles, restore when backtracking
        
        Args:
            grid: 2D list where grid[i][j] represents gold amount (0 = obstacle)
            
        Returns:
            Maximum gold that can be collected
        """
        
        def dfs(row, col):
            """
            DFS helper to collect maximum gold from current position.
            
            Intuition:
            - We use DFS to explore all possible paths from (row, col)
            - At each cell, we collect the gold and try all 4 directions
            - We take the MAXIMUM path (not sum) - this is key!
            - We mark cells as visited (set to 0) to avoid cycles
            - We restore the cell value when backtracking
            
            Why MAX not SUM?
            - We can only take ONE path from each cell
            - We want the best path, not all paths combined
            
            Example:
                Current cell has 5 gold, can go:
                - Left: collect 10 more
                - Right: collect 8 more
                - Up: collect 12 more
                - Down: collect 7 more
                We take max(10, 8, 12, 7) = 12, so total = 5 + 12 = 17
            
            Args:
                row: Current row index
                col: Current column index
                
            Returns:
                Maximum gold collectible from this position
            """
            # Base cases: Out of bounds or obstacle
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                grid[row][col] == 0):
                return 0
            
            # Choose: Collect gold and mark cell as visited
            gold = grid[row][col]
            grid[row][col] = 0  # Mark as visited to prevent cycles
            
            # Explore: Try all 4 directions and take the maximum path
            # We use a directions array to avoid redundant code
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
            max_path = max(dfs(row + dr, col + dc) for dr, dc in directions)
            
            # Unchoose: Restore cell value when backtracking
            # IMPORTANT: We must restore because grid is mutable and shared
            grid[row][col] = gold
            
            # Return current gold + best path from neighbors
            return gold + max_path
        
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0
        
        # Try starting from every cell with gold
        # Different starting positions can lead to different maximum paths
        for start_row in range(rows):
            for start_col in range(cols):
                if grid[start_row][start_col] != 0:
                    max_gold = max(max_gold, dfs(start_row, start_col))
        
        return max_gold