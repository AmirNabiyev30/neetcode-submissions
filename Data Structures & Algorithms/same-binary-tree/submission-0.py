# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we basically want to traverse a tree 
        #we can create a mapping and then do another pass to check that mapping on a second pass
        #we can traverse the second tree and then traverse the right tree and check equivalence
        #we can build a array of the copy 

        def dfs(p,q)->bool:

            if p is None and q is None:
                return True
            
            #first check null,
            if p is None or q is None:
                return False
            #now we check values
            if p.val != q.val:
                return False
            
            #so now we need to traverse the tree
            return dfs(p.left,q.left) and dfs(p.right,q.right)
        
        return dfs(p,q)
        
        