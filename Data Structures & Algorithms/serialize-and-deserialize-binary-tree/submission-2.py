# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                result.append("N")
            else:
                result.append(str(node.val))
            
            if node:
                queue.append(node.left)
                queue.append(node.right)

        return ",".join(result)

            
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        node_vals = data.split(",")

        
        if not node_vals[0]:
            return None
        
        root = self.build_node(node_vals[0])
        nodes = deque([root])

        self.idx = 1
        while self.idx < len(node_vals):
            node = nodes.popleft()

            node.left = self.build_node(node_vals[self.idx])
            if node.left:
                nodes.append(node.left)
            self.idx += 1
            node.right = self.build_node(node_vals[self.idx])
            if node.right:
                nodes.append(node.right)
            self.idx += 1


        return root
        
    
    def build_node(self, node_val):
        if node_val == "N":
            return None
        
        return TreeNode(int(node_val))
            
