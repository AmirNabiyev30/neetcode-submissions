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
        
        def dfs(root):
            if not root:
                return [True,0]

            #we need to compute left and right subtree
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <=1
            if not balanced:
                return [False,0]
            return [balanced, 1 + max(left[1],right[1])]

        return dfs(root)[0]
        