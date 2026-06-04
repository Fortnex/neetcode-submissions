# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root): 
            if root == None: 
                return 0,True
            lh,lb = helper(root.left)
            rh,rb = helper(root.right)
            return 1+max(lh,rh) ,abs(lh-rh)<=1 and (lb and rb) 
        s = helper(root)
        return s[1]