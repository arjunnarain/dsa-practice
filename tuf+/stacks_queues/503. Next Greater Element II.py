class Solution:
    def nextGreaterElements(self, arr):
        """
        PATTERN:
        - Monotonic Stack (Decreasing Stack)
        - Used when we need "next greater / smaller element" efficiently

        INTUITION:
        - For each element, we want the first greater element to its right.
        - Since the array is circular, elements at the end can look ahead to the start.
        - Brute force would be O(n^2), but a stack helps us solve it in O(n).

        KEY IDEA:
        - Traverse the array twice (2 * n) to simulate circular behavior.
        - Maintain a stack that keeps elements in strictly decreasing order.
        - The top of the stack always represents the next greater candidate.

        APPROACH:
        1. Initialize result array with -1 (default if no greater element exists).
        2. Traverse from right to left to ensure future elements are processed first.
        3. Use modulo (%) to map indices back to the original array.
        4. Pop all elements from stack that are <= current element
           (they can never be the "next greater").
        5. The remaining stack top (if any) is the next greater element.
        6. Push current element onto stack for future comparisons.
        """

        n = len(arr)
        ans = [-1] * n   # Default answer is -1

        st = []          # Monotonic decreasing stack (stores values, not indices)

        # Traverse twice from right to left to handle circular array
        for i in range(2 * n - 1, -1, -1):
            ind = i % n  # Map index back into original array range

            # Maintain decreasing stack:
            # Remove all elements smaller than or equal to current element
            while st and st[-1] <= arr[ind]:
                st.pop()

            # If stack is not empty, top is the next greater element
            if st:
                ans[ind] = st[-1]

            # Push current element for elements to its left
            st.append(arr[ind])

        return ans
