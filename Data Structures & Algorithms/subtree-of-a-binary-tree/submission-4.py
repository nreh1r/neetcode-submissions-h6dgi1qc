# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.result = False

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if self.is_subtree(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False
    
    def is_subtree(self, root, sub_root):
        if not root and not sub_root:
            return True
        if root and sub_root and root.val == sub_root.val:
            return self.is_subtree(root.left, sub_root.left) and self.is_subtree(root.right, sub_root.right)
        else:
            return False