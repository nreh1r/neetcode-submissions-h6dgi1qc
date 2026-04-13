# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        skip_nodes = count - n
        if skip_nodes == 0:
            return head.next
        
        curr = head
        for i in range(skip_nodes - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head