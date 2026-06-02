# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path_sum = root.val

        def dfs(root):
            if not root:
                return
            
            left = self.get_max(root.left)
            right = self.get_max(root.right)
            self.path_sum = max(self.path_sum, root.val + left + right)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return self.path_sum
        
    def get_max(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        left = self.get_max(root.left)
        right = self.get_max(root.right)
        val = root.val + max(left, right)

        return max(0, val)