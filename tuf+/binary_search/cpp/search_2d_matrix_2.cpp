#include <vector>
using namespace std;

class Solution{
    public:
        bool searchMatrix(vector<vector<int>> &matrix, int target){
            /*
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
            
            APPROACH:
            1. Start from top-right corner (row=0, col=m-1)
            2. If target == current element, return true
            3. If target < current element, move left (eliminate current column)
            4. If target > current element, move down (eliminate current row)
            5. Continue until we go out of bounds
            
            SIMILAR PROBLEMS:
            - LeetCode 240: Search a 2D Matrix II (this problem)
            - LeetCode 74: Search a 2D Matrix (different property - sorted as 1D array)
            - LeetCode 378: Kth Smallest Element in a Sorted Matrix
            - LeetCode 668: Kth Smallest Number in Multiplication Table
            - LeetCode 1351: Count Negative Numbers in a Sorted Matrix
            - LeetCode 1428: Leftmost Column with at Least a One
            
            PYTHON vs C++ DIFFERENCES & LEARNING POINTS:
            
            1. SYNTAX DIFFERENCES:
               - Python: len(matrix), len(matrix[0]) vs C++: matrix.size(), matrix[0].size()
               - Python: True/False vs C++: true/false (lowercase)
               - Python: No semicolons vs C++: Semicolons required
               - Python: and/or vs C++: &&/|| (logical operators)
            
            2. MEMORY MANAGEMENT:
               - Python: Automatic memory management, no need to worry about references
               - C++: Use &matrix to pass by reference (avoid copying), vector manages memory automatically
               - Python: Lists are dynamic, C++: vectors are dynamic but need explicit includes
            
            3. TYPE SYSTEM:
               - Python: Dynamic typing, no need to declare types
               - C++: Static typing, must declare vector<vector<int>> for 2D array
               - Python: len() works on any sequence vs C++: .size() is a member function
            
            4. PERFORMANCE CONSIDERATIONS:
               - C++: Generally faster due to compiled nature and direct memory access
               - Python: Slower but more readable, automatic bounds checking
               - C++: More control over memory layout and cache efficiency
            
            5. ERROR HANDLING:
               - Python: IndexError for out-of-bounds access
               - C++: Undefined behavior for out-of-bounds access (more dangerous)
            
            6. ALGORITHM DIFFERENCES:
               - This problem uses "staircase" approach vs previous problem's binary search
               - Time complexity: O(n+m) vs O(log(n*m)) for binary search approach
               - Space complexity: O(1) for both approaches
            */
            
            int n = matrix.size(), m = matrix[0].size();  // Get matrix dimensions
            int row = 0, col = m - 1;  // Start from top-right corner

            // Staircase approach: move left or down based on comparison
            while (row < n && col >= 0) {
                if (matrix[row][col] == target)
                    return true;        // Target found
                else if (matrix[row][col] < target)
                    row++;              // Move down (eliminate current row)
                else
                    col--;              // Move left (eliminate current column)
            }
            
            // Target not found in the matrix
            return false;
        }
    };