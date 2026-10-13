# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        #we want to perform dfs until we reach the same node as the subRoot
        #and then we reach same node we perform equality dfs from last problem
        def equal_trees(p ,q):
            if p is None and q is None:
                return True

            if p is None or q is None or p.val != q.val:
                return False
            return equal_trees(p.left,q.left) and equal_trees(p.right,q.right)
        #modified dfs

        def dfs(root,subroot):
            
            if not subroot:
                return True
            
            if not root:
                return False

            if equal_trees(root,subroot):
                return True
    
            return dfs(root.left,subroot) or dfs(root.right,subroot)
        
        return dfs(root,subRoot)

