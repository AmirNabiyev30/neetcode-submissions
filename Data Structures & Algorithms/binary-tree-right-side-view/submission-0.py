# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we can just add nodes to queue
        #perform a level search but only pull 1 node from the list
        #perform left to right adding children until we reach the last
        #node in the sLen which is guranteed to be the most right
        q = [root]
        res = []
        while q:
            qLen = len(q)
            latest_val = None
            for i in range(qLen):
                curr = q[0]
                q = q[1:]
                if curr:
                    latest_val = curr.val
                    q.append(curr.left)
                    q.append(curr.right)
            if latest_val:
                res.append(latest_val)
        return res
