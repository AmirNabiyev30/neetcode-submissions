# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we need an o(n) algorithm, we want to append to a non local variable result
        res = []
        #this is basiaclly a bfs
        queue = [root]
        
        while queue:
            level = []
            qLen = len(queue)
            for _ in range(qLen):
                curr = queue[0]
                queue = queue[1:]
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:
                res.append(level)  
        return res
        