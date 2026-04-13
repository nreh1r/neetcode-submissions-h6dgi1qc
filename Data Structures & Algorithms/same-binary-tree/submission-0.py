# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = [True]

        def dfs(root1, root2):

            if not root1 and not root2:
                return
            elif not root1 and root2:
                res[0] = False
                return
            elif not root2 and root1:
                res[0] = False
                return
            
            if root1.val != root2.val:
                res[0] = False
                return

            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)
        
        dfs(p, q)

        return res[0]