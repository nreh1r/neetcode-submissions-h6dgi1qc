# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        processing = True

        while processing:
            smallest_index = -1
            smallest_val = 1001
            for i in range(len(lists)):
                if lists[i] and lists[i].val <= smallest_val:
                    smallest_val = lists[i].val
                    smallest_index = i

            if smallest_index == -1:
                processing = False
                continue
            
            curr.next = lists[smallest_index]
            curr = curr.next
            lists[smallest_index] = lists[smallest_index].next
        
        return dummy.next

            
