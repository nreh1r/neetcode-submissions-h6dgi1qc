# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
		if not subRoot:
			return True
		
		if not root:
			return False
		
		if self.is_subtree(root, subRoot):
			return True
		
		return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
	
	def is_subtree(self, root, sub_root):
		if not root and not sub_root:
			return True
		
		if root and sub_root and root.val == sub_root.val:
			return self.is_subtree(root.left, sub_root.left) and self.is_subtree(root.right, sub_root.right)
		
		return False
        