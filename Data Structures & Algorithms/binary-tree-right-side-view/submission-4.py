# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
        q = [root]
        res = []
        while q:
            level = []
            temp = []
            for node in q:
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right: 
                    temp.append(node.right)
                
            res.append(level[-1])
            q = temp
        return res
