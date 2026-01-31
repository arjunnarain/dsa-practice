class Solution:
    """
    Next Greater Element I (LeetCode 496).
    
    The next greater element of some element x in an array is the first greater
    element that is to the right of x in the same array.
    
    You are given two distinct 0-indexed integer arrays nums1 and nums2, where
    nums1 is a subset of nums2.
    
    For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j]
    and determine the next greater element of nums2[j] in nums2. If there is no
    next greater element, then the answer for this query is -1.
    
    Return an array ans of length nums1.length such that ans[i] is the next greater
    element as described above.
    
    Example:
        nums1 = [4,1,2], nums2 = [1,3,4,2]
        Output: [-1,3,-1]
        - For 4 in nums1: next greater in nums2 is -1 (no greater element)
        - For 1 in nums1: next greater in nums2 is 3
        - For 2 in nums1: next greater in nums2 is -1 (no greater element)
    """
    
    def nextGreaterElement(self, nums1, nums2):
        """
        Find next greater element for each element in nums1 using monotonic stack.
        
        Approach:
        - Use a monotonic decreasing stack to process nums2
        - For each number in nums2, pop all smaller numbers from stack
        - The current number is the next greater element for all popped numbers
        - Store results in hashmap for O(1) lookup for nums1
        - Elements remaining in stack have no next greater element (-1)
        
        Intuition:
        - We process nums2 from left to right
        - Maintain a stack of numbers in decreasing order (monotonic decreasing stack)
        - When we encounter a number greater than stack top, it's the next greater
          element for all smaller numbers in the stack
        - We pop these smaller numbers and record the current number as their answer
        
        Key Insight:
        - Monotonic stack helps us find the next greater element efficiently
        - Stack maintains elements that haven't found their next greater element yet
        - When we see a larger number, it resolves all smaller numbers in the stack
        
        Example with nums2=[1,3,4,2]:
        - num=1: stack=[], push 1, stack=[1]
        - num=3: 3>1, pop 1, map[1]=3, push 3, stack=[3]
        - num=4: 4>3, pop 3, map[3]=4, push 4, stack=[4]
        - num=2: 2<4, push 2, stack=[4,2]
        - Result: map={1:3, 3:4}, elements 4 and 2 have no next greater (-1)
        
        Args:
            nums1: Subset array (elements to query)
            nums2: Full array (to find next greater elements)
            
        Returns:
            Array where ans[i] is next greater element of nums1[i] in nums2, or -1
        """
        # Monotonic decreasing stack: stores elements in decreasing order
        # Elements in stack are waiting for their next greater element
        stack = []
        
        # Hashmap to store next greater element for each number in nums2
        # Key: number, Value: its next greater element
        next_greater = {}
        
        # Process nums2 from left to right
        for num in nums2:
            # While current number is greater than stack top,
            # it's the next greater element for all smaller numbers in stack
            while stack and num > stack[-1]:
                # Pop smaller number and record current number as its next greater
                smaller_num = stack.pop()
                next_greater[smaller_num] = num
            
            # Push current number to stack (it's waiting for its next greater element)
            stack.append(num)
        
        # For each element in nums1, look up its next greater element
        # If not found in hashmap, return -1 (no next greater element)
        return [next_greater.get(i, -1) for i in nums1]