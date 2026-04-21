# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()
        curr = root
        p_list = self.fill_node_list(curr, p)
        curr = root
        q_list = self.fill_node_list(curr, q)

        smallest_list = q_list if len(q_list) < len(p_list) else p_list

        for node in smallest_list[::-1]:
            if node in q_list and node in p_list:
                return node


    def fill_node_list(self, root, target):
        node_list = []

        while root.val != target.val:
            node_list.append(root)
            if root.val < target.val:
                root = root.right
            else:
                root = root.left
            
        node_list.append(root)

        return node_list