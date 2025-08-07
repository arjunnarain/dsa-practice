class Solution:
    def kthElement(self, a, b, k):
        """
        Finds the k-th element in the merged sorted array of two sorted arrays.
        
        PATTERN RECOGNITION:
        - This is a classic "Median of Two Sorted Arrays" problem variant
        - Key insight: Instead of merging arrays (O(n+m)), we can use binary search on the partition
        - The problem reduces to finding the correct partition that gives us the k-th element
        
        INTUITION:
        - If we want the k-th element, we need exactly k-1 elements before it
        - We can partition the first array to take 'mid1' elements, then take 'mid2 = k-mid1' from second array
        - The partition is valid if all elements on left <= all elements on right
        - This creates a "cut" that gives us the k-th element at the boundary
        
        APPROACH:
        1. Ensure first array is smaller (swap if needed) for efficiency
        2. Binary search on how many elements to take from first array
        3. For each partition, check if it's valid (left elements <= right elements)
        4. If valid, we found our answer; if not, adjust the partition
        
        SIMILAR PROBLEMS:
        - LeetCode 4: Median of Two Sorted Arrays (same logic, k = (n+m)/2)
        - LeetCode 23: Merge k Sorted Lists (generalization)
        - LeetCode 378: Kth Smallest Element in a Sorted Matrix
        - LeetCode 668: Kth Smallest Number in Multiplication Table
        - LeetCode 719: Find K-th Smallest Pair Distance
        """
        n1, n2 = len(a), len(b)
        # Ensure first array is smaller for efficiency
        if n1 > n2:
            return self.kthElement(b, a, k)
        
        n = n1 + n2

        # Binary search boundaries: how many elements to take from first array
        # We can take at most min(k, n1) elements from first array
        # We must take at least max(0, k-n2) elements from first array
        low, high = max(0, k - n2), min(k, n1)

        while (low <= high):
            # Try taking mid1 elements from first array
            mid1 = (low + high) // 2
            # Then take mid2 = k - mid1 elements from second array
            mid2 = k - mid1
            
            # Get the boundary elements for the partition
            # l1: last element taken from first array (or -inf if none)
            l1 = a[mid1 - 1] if mid1 > 0 else float('-inf')
            # r1: first element not taken from first array (or +inf if all taken)
            r1 = a[mid1] if mid1 < n1 else float('inf')

            # l2: last element taken from second array (or -inf if none)
            l2 = b[mid2 - 1] if mid2 > 0 else float('-inf')
            # r2: first element not taken from second array (or +inf if all taken)
            r2 = b[mid2] if mid2 < n2 else float('inf')

            # Check if this partition is valid
            # Valid partition: all elements on left <= all elements on right
            if l1 <= r2 and l2 <= r1:
                # We found the correct partition! The k-th element is max(l1, l2)
                return max(l1, l2)
            elif l1 > r2:
                # Too many elements from first array, reduce mid1
                high = mid1 - 1
            else:
                # Too few elements from first array, increase mid1
                low = mid1 + 1
        
        # Should never reach here for valid inputs
        return 0


        
