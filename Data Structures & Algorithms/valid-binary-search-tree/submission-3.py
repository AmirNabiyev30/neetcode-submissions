# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we need to be able to pass values down and perform comparsions
        #but we need to dictate if we went left or right down the subtree
        #0 for left and 1 for right, 2 for root
        def dfs(root,minny,maxxy):
            if not root:
                return True
            if root.val <= minny or root.val >= maxxy:
                return False
            valid_left = dfs(root.left,minny,root.val)
            valid_right  = dfs(root.right,root.val,maxxy)

            return valid_left and valid_right
        return dfs(root,-1001,1001)

            


            
            
    
            
        