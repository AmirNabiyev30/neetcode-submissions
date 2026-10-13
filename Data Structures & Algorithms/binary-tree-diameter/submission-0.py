# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            #get height of left tree
            left = dfs(curr.left)
            right = dfs(curr.right)

            #compute new max diameter

            self.res = max(self.res,left+right)

            #return new height + 1

            return 1 + max(left,right)
        dfs(root)
        return self.res


        
        