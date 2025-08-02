class Solution:
    def findPages(self, nums, m):
        """
        Finds the minimum number of pages that can be allocated to the most loaded student when allocating books to m students.
        Approach:
        - Use binary search to find the minimum feasible maximum pages per student.
        - The trick: As the allowed maximum pages per student increases, fewer students are needed (monotonic property), so binary search is applicable.
        - For each candidate max, use the helper function to check how many students are needed.
        - If more than m students are needed, try a higher max; otherwise, try a lower max.
        Edge cases: If m > n (more students than books), allocation is impossible.
        How to identify binary search is applicable:
        - The problem asks for a minimum/maximum value, not a specific arrangement.
        - There is a monotonic property: as the allowed max increases, the number of students required decreases.
        - The search space can be halved based on the helper function's result.
        """
        n = len(nums)
        
        # Book allocation impossible if more students than books
        if m > n:
            return -1
        
        def allocate_pages(nums, pages):
            # Helper function to count how many students are needed if no student gets more than 'pages'
            count_students = 1
            pages_allocated = 0
            for page in nums:
                if pages_allocated + page <= pages:
                    pages_allocated += page
                else:
                    count_students += 1
                    pages_allocated = page
            return count_students
        
        # Binary search boundaries: at least max(nums) pages, at most sum(nums) pages
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) // 2

            # If more than m students are needed, try a higher max
            if allocate_pages(nums, mid) > m:
                low = mid + 1
            else:
                # Otherwise, try a lower max
                high = mid - 1
        
        # The minimum possible value for the maximum pages allocated to a student
        return low