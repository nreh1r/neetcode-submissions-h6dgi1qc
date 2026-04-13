"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = dummy
        random_cache = {}

        while head:
            copy = Node(head.val, head.next, head.random)
            random_cache[hash(head)] = copy
            curr.next = copy
            curr = curr.next
            head = head.next
        
        curr = dummy.next
        while curr:
            if curr.random:
                curr.random = random_cache[hash(curr.random)]
            curr = curr.next
        
        return dummy.next
