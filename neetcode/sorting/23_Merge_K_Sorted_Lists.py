# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                leftList = lists[i]
                rightList = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(leftList, rightList))
            lists = mergedLists
        return lists[0]


    def mergeList(self,leftList, rightList):
        dummy = ListNode()
        tail = dummy
        while leftList and rightList:
            if leftList.val < rightList.val:
                tail.next = leftList
                leftList = leftList.next
            else:
                tail.next = rightList
                rightList = rightList.next
            tail = tail.next 

        if leftList:
            tail.next = leftList
        if rightList:
            tail.next = rightList
        return dummy.next

        