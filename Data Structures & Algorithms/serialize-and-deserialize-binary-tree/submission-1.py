# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serialized = ""
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                serialized += f"{node.val}#"
            else:
                serialized += "null#"
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
        
        return serialized


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        root = None
        node_queue = deque([])

        l, r = 0, 0
        while r < len(data):
            while r < len(data) and data[r] != "#":
                r += 1
            
            # print(f"initial node_val: {node_val}")
            if len(node_queue) == 0:
                node_val = data[l:r]
                print("calling root build")
                root = self.build_node(node_val)
                node_queue.append(root)
                r += 1
                l = r
            else:
                child_nodes = []
                while len(node_queue):
                    node_val = data[l:r]
                    print(f"starting child build. l: {l}; r: {r}")
                    parent_node = node_queue.popleft()
                    if not parent_node:
                        continue
                    print(f"calling first build. Parent is {parent_node.val}")
                    parent_node.left = self.build_node(node_val)
                    child_nodes.append(parent_node.left)

                    r += 1
                    l = r

                    while r < len(data) and data[r] != "#":
                        r += 1
                    
                    node_val = data[l:r]
                    print(f"inner node_val: {node_val}")
                    print("calling inner build")
                    parent_node.right = self.build_node(node_val)
                    child_nodes.append(parent_node.right)
                    r += 1
                    l = r

                    while r < len(data) and data[r] != "#":
                        r += 1
                if len(child_nodes) == 0:
                    break
                node_queue = deque(child_nodes)
            
        print(root)
        return root

    def build_node(self, val):
        print(f"buildilng node with value: #{val}")
        if val == "null":
            return None
        
        return TreeNode(int(val))