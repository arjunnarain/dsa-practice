# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        main_result = []
        if root:
            queue.append(root)
        while len(queue) > 0:
            temp_result = [] 
            for i in range(len(queue)):   
                cur = queue.popleft()
                temp_result.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            main_result.append(temp_result)
        return main_result
            
            
