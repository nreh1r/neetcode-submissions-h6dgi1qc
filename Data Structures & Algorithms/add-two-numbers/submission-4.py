# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = l1
        prev_node = l1

        # Use l1 as the new list
        while curr and l2:
            # Add the 2 values
            val = curr.val + l2.val + carry
            if val > 9:
                str_val = str(val)
                val = int(str_val[1])
                carry = int(str_val[0])
            else:
                carry = 0
            curr.val = val

            if curr.next == None:
                prev_node = curr

            curr = curr.next
            l2 = l2.next

        while curr and carry:
            val = curr.val + carry
            if val > 9:
                str_val = str(val)
                val = int(str_val[1])
                carry = int(str_val[0])
            else:
                carry = 0

            curr.val = val

            if curr.next == None:
                prev_node = curr

            curr = curr.next


        if l2:
            value = l2.val + carry
            if value > 9:
                str_val = str(value)
                l2.val = int(str_val[1])
                l2.next = ListNode(int(str_val[0]))
            else:
                l2.val = value
            prev_node.next = l2
            carry = 0
        elif carry:
            prev_node.next = ListNode(carry)
        
        return l1
