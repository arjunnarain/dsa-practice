#include <vector>
using namespace std;

class Solution{
    public:
        bool searchMatrix(vector<vector<int>> &mat, int target){
            /*
            Searches for a target value in a 2D matrix where each row is sorted and 
            the first element of each row is greater than the last element of the previous row.
            
            PATTERN RECOGNITION:
            - This is a "Search in 2D Sorted Matrix" problem
            - Key insight: The matrix can be treated as a 1D sorted array
            - The matrix has a special property: it's sorted both row-wise and column-wise
            - This allows us to use binary search by converting 2D indices to 1D
            
            INTUITION:
            - Since the matrix is sorted in a specific way, we can flatten it into a 1D array
            - Each element at position i in the 1D array corresponds to mat[i/m][i%m] in 2D
            - This conversion preserves the sorted order, making binary search applicable
            - The matrix property ensures that if we find the element, it's in the correct position
            
            APPROACH:
            1. Treat the 2D matrix as a 1D sorted array
            2. Use binary search on the flattened array indices
            3. Convert 1D index to 2D coordinates: row = mid / m, column = mid % m
            4. Compare the element at these coordinates with the target
            5. Adjust search boundaries based on the comparison
            
            SIMILAR PROBLEMS:
            - LeetCode 74: Search a 2D Matrix (this problem)
            - LeetCode 240: Search a 2D Matrix II (different property: sorted row-wise and column-wise)
            - LeetCode 378: Kth Smallest Element in a Sorted Matrix
            - LeetCode 668: Kth Smallest Number in Multiplication Table
            - LeetCode 1351: Count Negative Numbers in a Sorted Matrix
            - LeetCode 1428: Leftmost Column with at Least a One
            
            PYTHON vs C++ DIFFERENCES & LEARNING POINTS:
            
            1. SYNTAX DIFFERENCES:
               - Python: len(mat), len(mat[0]) vs C++: mat.size(), mat[0].size()
               - Python: // for integer division vs C++: / (automatically integer division for int types)
               - Python: % for modulo vs C++: % (same)
               - Python: True/False vs C++: true/false (lowercase)
            
            2. MEMORY MANAGEMENT:
               - Python: Automatic memory management, no need to worry about references
               - C++: Use &mat to pass by reference (avoid copying), vector manages memory automatically
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
            
            6. CONVENTIONAL DIFFERENCES:
               - Python: snake_case for variables vs C++: camelCase or snake_case
               - Python: 4-space indentation vs C++: Often 2 or 4 spaces
               - Python: No semicolons vs C++: Semicolons required
            */
            
            int n = mat.size();      // Number of rows (equivalent to len(mat) in Python)
            int m = mat[0].size();   // Number of columns (equivalent to len(mat[0]) in Python)

            // Binary search boundaries: treat matrix as 1D array with indices 0 to n*m-1
            int low = 0, high = m * n - 1;

            while (low <= high) {
                int mid = (low + high) / 2;  // Integer division (equivalent to // in Python)

                // Convert 1D index to 2D coordinates
                int row = mid / m;      // Integer division gives row number
                int col = mid % m;      // Modulo gives column number

                // Compare the element at current position with target
                if (mat[row][col] == target)
                    return true;        // C++ uses lowercase true/false
                else if (mat[row][col] < target)
                    // Target is in the right half of the 1D array
                    low = mid + 1;
                else
                    // Target is in the left half of the 1D array
                    high = mid - 1;
            }

            // Target not found in the matrix
            return false;
        }
    };