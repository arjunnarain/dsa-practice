class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles)
        result = high
        while low <= high:
            mid = (low + high) // 2
            time_taken_status = self.totalTimeTaken(piles, mid, h)
            if time_taken_status <= 0:  # We managed to finish within h or exactly at h.
                high = mid - 1
                result = mid  # Since we could finish it within h hours, update the result
            else:  # We couldn't finish in time, need to increase eating speed
                low = mid + 1
        return result

    def totalTimeTaken(self, piles, rate, allowedHours):
        total = 0
        for pile in piles:
            total += -(-pile // rate)  # equivalent to math.ceil(pile / rate)
        
        if total < allowedHours:
            return -1
        elif total > allowedHours:
            return 1
        else:
            return 0
