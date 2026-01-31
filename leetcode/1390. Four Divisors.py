class Solution:
    """
    Four Divisors (LeetCode 1390).
    
    Given an integer array nums, return the sum of divisors of the integers in that array
    that have exactly four divisors. If there is no such integer in the array, return 0.
    
    Example:
        nums = [21, 4, 7]
        - 21 has divisors: 1, 3, 7, 21 (4 divisors) -> sum = 32
        - 4 has divisors: 1, 2, 4 (3 divisors) -> skip
        - 7 has divisors: 1, 7 (2 divisors) -> skip
        Output: 32
    """
    
    def sumFourDivisors(self, nums):
        """
        Sum divisors of numbers that have exactly 4 divisors.
        
        Args:
            nums: List of integers
            
        Returns:
            Sum of divisors for numbers with exactly 4 divisors
        """
        result = 0
        for num in nums:
            result += self._findSumOfDivisors(num)
        return result
    
    def _findSumOfDivisors(self, num):
        """
        Find sum of divisors if number has exactly 4 divisors, else return 0.
        
        Approach:
        - Use divisor pair property: if d divides num, then num/d also divides num
        - Only iterate up to sqrt(num) to find all divisors efficiently
        - Count divisors and sum them as we go
        - Early termination: if count > 4, return 0 immediately
        
        Intuition:
        - Divisors come in pairs: if d is a divisor, then num/d is also a divisor
        - Example: For 21, divisors are (1,21), (3,7) -> 4 divisors total
        - We only need to check d from 1 to sqrt(num) because:
          * For each divisor d <= sqrt(num), we get its pair num/d >= sqrt(num)
          * This finds all divisors without checking every number
        
        Numbers with exactly 4 divisors:
        - p^3 (cube of prime): divisors are 1, p, p^2, p^3
        - p*q (product of two distinct primes): divisors are 1, p, q, p*q
        
        Example with num=21:
        - d=1: 21%1==0, d2=21, count=2, sum=1+21=22
        - d=2: 21%2!=0, skip
        - d=3: 21%3==0, d2=7, count=4, sum=22+3+7=32
        - d=4: 21%4!=0, skip
        - d=5: 21%5!=0, skip
        - d=sqrt(21)≈4.58, stop
        - count==4, return 32
        
        Args:
            num: Integer to check
            
        Returns:
            Sum of divisors if num has exactly 4 divisors, 0 otherwise
        """
        div_sum = 0  # Sum of divisors
        count = 0  # Count of divisors found so far
        
        # Iterate only up to sqrt(num) because divisors come in pairs
        # For each divisor d <= sqrt(num), we get its pair num/d >= sqrt(num)
        d = 1
        while d * d <= num:
            if num % d == 0:
                # d is a divisor, so num/d is also a divisor (its pair)
                d2 = num // d
                
                if d == d2:
                    # Perfect square: d*d == num (same divisor counted once)
                    # Example: For 4, divisors are 1, 2, 4 (not 1,2,2,4)
                    count += 1
                    div_sum += d
                else:
                    # Two distinct divisors: d and d2 (its pair)
                    count += 2
                    div_sum += d + d2
                
                # Early termination: if we already have more than 4 divisors, stop
                # No need to continue checking
                if count > 4:
                    return 0
            d += 1
        
        # Return sum only if exactly 4 divisors were found
        return div_sum if count == 4 else 0