# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        global ele
        global el
        ele = []
        el=[]
        
        def parser(root): 
            if root==None: 
                ele.append(None)
            else:
                ele.append(root.val)
                parser(root.left)
                parser(root.right)
            return ele
            
        def parser2(root): 
            if root==None: 
                el.append(None)
            else:
                el.append(root.val)
                parser2(root.left)
                parser2(root.right)
            return el

        a = parser(p)
        b = parser2(q)
        print(a,b)
        return a==b