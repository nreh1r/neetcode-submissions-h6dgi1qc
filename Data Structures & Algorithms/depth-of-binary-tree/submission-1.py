# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS

        stack = [[root, 1]]
        res = 0

        while stack:
            node, height = stack.pop()

            if node:
                stack.append([node.left, height + 1])
                stack.append([node.right, height + 1])
                res = max(res, height)
        
        return res

