# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0

        def dfs(node, path_val):
            if not node:
                return None
            
            if node.val >= path_val:
                self.good_nodes += 1
            
            new_val = max(path_val, node.val)

            dfs(node.left, new_val)
            dfs(node.right, new_val)

        dfs(root, root.val)

        return self.good_nodes