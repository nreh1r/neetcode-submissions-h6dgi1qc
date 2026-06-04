# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

	def serialize(self, root: Optional[TreeNode]) -> str:
		result = []
		
		queue = deque([root])
		while queue:
			node = queue.popleft()
			
			if not node:
				result.append("N")
			else:
				result.append(str(node.val))
				queue.append(node.left)
				queue.append(node.right)
			
		return ",".join(result)
	
	def deserialize(self, data: str) -> Optional[TreeNode]:
		node_vals = data.split(",")
		
		if node_vals[0] == "N":
			return None
		
		root = TreeNode(int(node_vals[0]))
		queue = deque([root])
		
		self.idx = 1
		
		while queue:
			node = queue.popleft()
			
			if node_vals[self.idx] != "N":
				node.left = TreeNode(int(node_vals[self.idx]))
				queue.append(node.left)
			self.idx += 1
			
			if node_vals[self.idx] != "N":
				node.right = TreeNode(int(node_vals[self.idx]))
				queue.append(node.right)
			self.idx += 1
		
		return root
