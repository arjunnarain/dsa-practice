# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Remove the nth node from the end of a linked list.
    
    Example:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]  (removed node 4, which is 2nd from end)
    """
    
    def removeNthFromEnd(self, head, n):
        """
        Remove the nth node from the end of the list.
        
        Approach (Two-pass):
        1. First pass: Count total nodes to find size
        2. Calculate position from start: position = size - n
        3. Second pass: Traverse to (position - 1) and remove next node
        
        Intuition:
        - To remove nth from end, we need to find (size - n)th from start
        - Special case: If removing head (n == size), return head.next
        - We need to stop at node BEFORE the one to remove to update its next pointer
        
        Example with [1,2,3,4,5], n=2:
        - Size = 5, position from start = 5 - 2 = 3 (node with value 3)
        - We stop at node 3 (index 2), set node 3.next = node 3.next.next
        - This skips node 4 and connects node 3 to node 5
        
        Args:
            head: Head of the linked list
            n: Position from end (1-indexed, where 1 is the last node)
            
        Returns:
            Head of the modified linked list
        """
        # Edge case: Empty list
        if head is None:
            return None
        
        # First pass: Count the total number of nodes
        size = 0
        temp = head
        while temp is not None:
            size += 1
            temp = temp.next
        
        # Special case: Removing the head node (first node)
        # If n == size, we're removing the head, so return head.next
        if n == size:
            return head.next
        
        # Calculate position from start (0-indexed)
        # nth from end = (size - n)th from start
        position = size - n
        
        # Second pass: Traverse to the node BEFORE the one to remove
        # We need to stop at position - 1 to update its next pointer
        temp = head
        i = 0
        while temp.next is not None:
            # When we reach the node before the target, remove the next node
            if i == position - 1:
                temp.next = temp.next.next  # Skip the target node
                break
            i += 1
            temp = temp.next
        
        return head