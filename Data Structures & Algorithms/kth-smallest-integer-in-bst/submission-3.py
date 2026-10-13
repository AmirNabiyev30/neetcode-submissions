# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        I think a brute force solution would be pass lists of sorted values up the tree and
        when computation comes back to the root we would have a list of values and then just select the kth element
        the nice thing is that binary search trees are always already sorted

        For example we can append elementts of left child to end of array and put elements on the left
        in begining of the array

        we need to properly define how we give lists 
        """
        def dfs(root,val):
            if not root:
                return None
            
            #we want to pull from the left
            left_vals  = dfs(root.left,[root.val])
            right_vals = dfs(root.right, [root.val])
            # we want to pull values from the left
            if left_vals == None and right_vals == None:
                return [root.val]
            elif left_vals == None:
                return [root.val] + right_vals
            elif right_vals == None:
                return left_vals + [root.val]

            vals = left_vals + [root.val] + right_vals
            return vals
        val = dfs(root,root.val)
        print(val)
        return val[k-1]


        