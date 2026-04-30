# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.is_valid = True
        self.nodes = []
        def dfs(root):
            if not root:
                return None

            dfs(root.left)

            if len(self.nodes) > 0 and root.val <= self.nodes[-1]:
                self.is_valid = False
                return
            
            self.nodes.append(root.val)

            dfs(root.right)

        
        dfs(root)

        return self.is_valid