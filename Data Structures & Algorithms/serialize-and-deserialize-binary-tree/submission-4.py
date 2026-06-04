# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
	
	def serialize(self, root: Optional[TreeNode]) -> str:
		result = []
		
		def dfs(root):
			if not root:
				result.append("N")
				return
			
			result.append(str(root.val))
			dfs(root.left)
			dfs(root.right)
		
		dfs(root)
		
		return ",".join(result)
	
	def deserialize(self, data: str) -> Optional[TreeNode]:
		node_vals = data.split(",")
		self.idx = 0
		
		def dfs():
			if node_vals[self.idx] == "N":
				self.idx += 1
				return None
			
			node = TreeNode(node_vals[self.idx])
			self.idx += 1
			node.left = dfs()
			node.right = dfs()
			
			return node
		
		return dfs()
