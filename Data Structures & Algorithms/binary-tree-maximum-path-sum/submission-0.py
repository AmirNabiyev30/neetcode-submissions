# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')
        def dfs(node):
            if node == None:
                return 0

            #process left and right
            lsum = dfs(node.left)
            rsum = dfs(node.right)
            #if negative we dont want it
            if lsum < 0:
                lsum = 0
                #if neg we dont want it
            if rsum < 0:
                rsum = 0
            #if conditions define behavior
            
            #leaf node 
            self.best = max(self.best, node.val + lsum + rsum)
            return node.val + max(lsum, rsum)
        dfs(root)
        return self.best