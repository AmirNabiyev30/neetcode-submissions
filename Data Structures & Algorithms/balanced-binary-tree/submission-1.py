# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #this shouldn't be that bad we just compute a dfs
        #and if at any point the height difference is greater than 1 then we 
        #we should have an external variable
        self.diff = 0
        def dfs(root):
            if not root:
                return 0

            #we need to compute left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            self.diff = max(self.diff,abs(left - right))

            return 1 + max(left, right)
        dfs(root)
        print(self.diff)
        return self.diff <= 1
        