# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        dummy = ListNode(None, None)

        if list2.val < list1.val:
            dummy.next = list2
            list2 = list2.next
        else:
            dummy.next = list1
            list1 = list1.next
        
        curr = dummy.next

        while list1 and list2:
            new_node = None
            if list1.val < list2.val:
                new_node = list1
                list1 = list1.next
            else:
                new_node = list2
                list2 = list2.next

            curr.next = new_node
            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return dummy.next 


            