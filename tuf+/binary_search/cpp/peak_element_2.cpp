#include <vector>
#include <climits>
using namespace std;

class Solution {
    public:
        int maxElement(vector<vector<int>>& arr, int col) {
            /*
            Helper function to find the row index of the maximum element in a given column.
            This is crucial for the binary search approach on columns.
            */
            int n = arr.size();
            int max_val = INT_MIN;  // C++ equivalent of Python's float('-inf')
            int index = -1;

            for(int i = 0; i < n; i++) {
                if(arr[i][col] > max_val) {
                    max_val = arr[i][col];
                    index = i;
                }
            }

            return index;
        }
        
        vector<int> findPeakGrid(vector<vector<int>>& mat) {
            /*
            Finds a 2D peak element in a matrix where a peak is greater than all its adjacent elements.
            
            PATTERN RECOGNITION:
            - This is a "Find Peak Element II" problem (LeetCode 1901)
            - Key insight: We can use binary search on columns, not rows
            - For each column, we find the maximum element in that column
            - A peak exists if the max element is greater than its left and right neighbors
            - This reduces a 2D problem to 1D binary search on columns
            
            INTUITION:
            - In a 2D matrix, a peak must be the maximum in its column
            - We can't use binary search on rows because peaks can be anywhere
            - But we can use binary search on columns by finding the max in each column
            - If the max in column mid is a peak, we're done
            - If not, we can eliminate half the columns based on comparison
            
            APPROACH:
            1. Binary search on columns (0 to m-1)
            2. For each column mid, find the row with maximum element using maxElement()
            3. Check if this element is a peak by comparing with left and right neighbors
            4. If it's a peak, return {row, col}
            5. If left neighbor is larger, search in left half; else search in right half
            
            TIME COMPLEXITY: O(n * log m) where n = rows, m = columns
            SPACE COMPLEXITY: O(1) - only using a few variables
            
            SIMILAR PROBLEMS:
            - LeetCode 1901: Find a Peak Element II (this problem)
            - LeetCode 162: Find Peak Element (1D version)
            - LeetCode 852: Peak Index in a Mountain Array
            - LeetCode 1095: Find in Mountain Array
            - LeetCode 1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number
            
            PYTHON vs C++ DIFFERENCES & LEARNING POINTS:
            
            1. SYNTAX DIFFERENCES:
               - Python: len(mat), len(mat[0]) vs C++: mat.size(), mat[0].size()
               - Python: float('-inf') vs C++: INT_MIN (from <climits>)
               - Python: [row, mid] vs C++: {row, mid} (initializer list)
               - Python: No semicolons vs C++: Semicolons required
            
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
               - C++: Need to manually check bounds before accessing elements
            
            6. ALGORITHM INSIGHTS:
               - This problem demonstrates how to reduce 2D problems to 1D binary search
               - The key is finding the right dimension to apply binary search
               - Helper functions (like maxElement) are crucial for complex binary search problems
            */
            
            int n = mat.size();      // Number of rows
            int m = mat[0].size();   // Number of columns

            // Binary search boundaries: search through columns
            int low = 0;
            int high = m - 1;

            while(low <= high) {
                int mid = (low + high) / 2;  // Integer division

                // Find the row with maximum element in column mid
                int row = maxElement(mat, mid);

                // Get left and right neighbors, handle boundary cases
                int left = mid - 1 >= 0 ? mat[row][mid - 1] : INT_MIN;
                int right = mid + 1 < m ? mat[row][mid + 1] : INT_MIN;

                // Check if current element is a peak
                if(mat[row][mid] > left && mat[row][mid] > right)
                    return {row, mid};  // C++ initializer list syntax
                else if (left > mat[row][mid])
                    // Peak is in left half
                    high = mid - 1;
                else
                    // Peak is in right half
                    low = mid + 1;
            }

            // No peak found (should not happen for valid inputs)
            return {-1, -1};  // C++ initializer list syntax
        }
    };