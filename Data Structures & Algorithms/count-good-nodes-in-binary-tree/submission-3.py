# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0
        queue = deque([(root, root.val)])

        while queue:
            node, path_val = queue.popleft()

            if node.val >= path_val:
                good_nodes += 1
            
            new_val = max(path_val, node.val)

            if node.left:
                queue.append((node.left, new_val))
            
            if node.right:
                queue.append((node.right, new_val))
        
        return good_nodes