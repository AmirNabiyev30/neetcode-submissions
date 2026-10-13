# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0
        def dfs(root,val): #instead of an array, we pass the max value we see as we go down
            if not root:
                return None

            if root.val >= val:
                self.goodNodes +=1
            
            root.left
            left = dfs(root.left,max(root.left.val if root.left else 0,val))
            right = dfs(root.right,max(root.right.val if root.right else 0,val))

            return root
        dfs(root,root.val)
        return self.goodNodes
        