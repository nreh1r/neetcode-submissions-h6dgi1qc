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
				return 0
			
			left_path = dfs(root.left)
			right_path = dfs(root.right)
			left_max = max(0, left_path)
			right_max = max(0, right_path)
			self.path_sum = max(self.path_sum, root.val + left_max + right_max)
			
			return root.val + max(left_max, right_max)
		
		dfs(root)
		return self.path_sum
        