class Solution:
    def floorSqrt(self, n: int) -> int:
        # Initialize binary search boundaries
        # low = 1 (smallest possible square root for positive integers)
        # high = n (largest possible value - sqrt(n) is always <= n)
        low, high = 1, n
        
        # Variable to store the floor value of square root
        # This will hold the largest integer whose square is <= n
        answer = 0

        # Binary search loop continues while search space is valid
        while low <= high:
            # Calculate middle point to check
            # Using integer division to avoid floating point
            mid = (low + high) // 2
            
            # Calculate square of mid to compare with n
            mid_squared = mid * mid

            # Perfect square case: mid² = n
            if mid_squared == n:
                answer = mid
                return answer
            
            # If mid² < n, the answer could be mid or something larger
            # Store mid as potential answer and search in upper half
            if mid_squared < n:
                answer = mid  # Update answer as this could be the floor value
                low = mid + 1  # Search for larger values
            else:
                # If mid² > n, the answer must be smaller than mid
                high = mid - 1  # Search in lower half
        
        # Return the floor value found
        return answer