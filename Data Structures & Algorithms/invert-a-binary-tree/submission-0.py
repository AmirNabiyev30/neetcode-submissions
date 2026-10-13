# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #we can perfroma recursion on subtrees, basically an induction
        #we need a termination arguement
        #we terminate when we reach a leaf
        #we to call recursively and increase the size of the stack calls

        if root is None:
            return None
        root.left,root.right = root.right,root.left
        
        #recusrively switch

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        



        