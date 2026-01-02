class Solution:
    """
    Find the minimum number of meeting rooms required.
    
    Given an array of meeting time intervals, find the minimum number of
    conference rooms required so that all meetings can be scheduled.
    
    Example:
        intervals = [[0,30], [5,10], [15,20]]
        Output: 2
        - Meeting [0,30] needs room 1
        - Meeting [5,10] overlaps with [0,30], needs room 2
        - Meeting [15,20] can use room 1 (since [0,30] is still ongoing)
    """
    
    def minMeetingRooms(self, intervals):
        """
        Find minimum meeting rooms needed using greedy two-pointer approach.
        
        Approach:
        - Separate start and end times into two sorted arrays
        - Use two pointers to simulate timeline of events
        - Track count of simultaneous meetings (rooms needed)
        - Maximum count during simulation = minimum rooms needed
        
        Intuition:
        - We don't care which specific meetings overlap
        - We only care about the MAXIMUM number of simultaneous meetings
        - By sorting start and end times separately, we can process events chronologically
        - When a meeting starts: increment count (need another room)
        - When a meeting ends: decrement count (free up a room)
        
        Key Insight:
        - If start[i] < end[j], a new meeting starts before an old one ends
        - This means we need an additional room
        - Otherwise, a meeting ends, freeing up a room
        
        Example with [[0,30], [5,10], [15,20]]:
        - start = [0, 5, 15], end = [10, 20, 30]
        - Timeline: 0(start, count=1), 5(start, count=2), 10(end, count=1),
                    15(start, count=2), 20(end, count=1), 30(end, count=0)
        - Maximum count = 2, so we need 2 rooms
        
        Args:
            intervals: List of [start, end] pairs representing meeting times
            
        Returns:
            Minimum number of meeting rooms required
        """
        n = len(intervals)
        
        # Separate start and end times into two arrays
        # This allows us to process events chronologically
        start = []
        end = []
        
        for i in range(n):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        
        # Sort both arrays to process events in chronological order
        start.sort()
        end.sort()
        
        # Two-pointer technique to simulate timeline
        # i: pointer for start times (next meeting to start)
        # j: pointer for end times (next meeting to end)
        # count: current number of simultaneous meetings (rooms in use)
        # ans: maximum count seen (minimum rooms needed)
        
        i, j = 1, 0  # Start with i=1 because first meeting already started
        ans = count = 1  # First meeting is already in progress
        
        # Process all events (both starts and ends)
        while i < n and j < n:
            # If next start time is before next end time:
            # A new meeting starts before an old one ends -> need another room
            if start[i] < end[j]:
                count += 1
                i += 1
            # Otherwise: A meeting ends -> free up a room
            else:
                count -= 1
                j += 1
            
            # Track the maximum number of simultaneous meetings
            # This equals the minimum number of rooms needed
            ans = max(ans, count)
        
        return ans

