class Solution:
    """
    Find the maximum number of fruits you can collect (Fruit Into Baskets).
    
    You have two baskets, and you want to collect fruits such that:
    - Each basket can only hold one type of fruit
    - You can start from any tree, but once you start, you must pick
      exactly one fruit from every tree you encounter
    - You must stop if you encounter a third type of fruit
    
    This is equivalent to: Find the longest subarray with at most 2 distinct elements.
    
    Example:
        fruits = [1,2,1]
        Output: 3 (collect all fruits: [1,2,1])
        
        fruits = [0,1,2,2]
        Output: 3 (collect [1,2,2] - skip 0 or stop after 0,1,2)
    """
    
    def totalFruit(self, fruits):
        """
        Find maximum fruits collectible using sliding window.
        
        Approach:
        - Use sliding window technique with two pointers
        - Track count of each fruit type using hash map
        - Expand window by moving right pointer
        - If we have more than 2 types, shrink from left until valid
        - Track maximum valid window size
        
        Intuition:
        - We want the longest subarray with at most 2 distinct fruit types
        - As we expand the window, we add fruits to our collection
        - If we encounter a third type, we need to remove fruits from the left
          until we have at most 2 types again
        - We use a hash map to track how many of each type we have
        - When count of a type reaches 0, we remove it from the map
        
        Key Insight:
        - We don't need to track which specific types, just the count of distinct types
        - When shrinking, we decrement count of leftmost fruit
        - If count becomes 0, we remove it from map (now we have <= 2 types)
        - The maximum window size we achieve = answer
        
        Example with fruits=[1,2,1,2,3]:
        - Window [0:1]: types={1:1}, valid, len=1, max=1
        - Window [0:2]: types={1:1,2:1}, valid, len=2, max=2
        - Window [0:3]: types={1:2,2:1}, valid, len=3, max=3
        - Window [0:4]: types={1:2,2:1,3:1}, invalid -> shrink left
        - Window [1:4]: types={1:1,2:1,3:1}, invalid -> shrink left
        - Window [2:4]: types={1:1,2:2,3:1}, invalid -> shrink left
        - Window [3:4]: types={2:1,3:1}, valid, len=2, max=3
        
        Args:
            fruits: Array where fruits[i] is the type of fruit at tree i
            
        Returns:
            Maximum number of fruits you can collect
        """
        n = len(fruits)
        left = 0  # Left pointer of sliding window
        right = 0  # Right pointer of sliding window
        max_len = 0  # Maximum valid window size found so far
        
        # Hash map to track count of each fruit type in current window
        # Key: fruit type, Value: count of that type in window
        fruit_count = {}
        
        # Expand window by moving right pointer
        while right < n:
            # Add current fruit to window
            fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
            
            # If we have more than 2 distinct types, shrink window from left
            # Keep shrinking until we have at most 2 types
            if len(fruit_count) > 2:
                # Remove leftmost fruit from window
                fruit_count[fruits[left]] -= 1
                
                # If count becomes 0, remove from map (no longer in window)
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                
                # Move left pointer to shrink window
                left += 1
            
            # At this point, window [left:right+1] is valid (has <= 2 types)
            # Calculate current window size and update maximum
            if len(fruit_count) <= 2:
                max_len = max(max_len, right - left + 1)
            
            # Expand window
            right += 1
        
        return max_len
        