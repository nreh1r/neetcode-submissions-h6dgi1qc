# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		dummy = ListNode()
		curr = dummy
		left, right = head, head
		
		while right:
			for _ in range(k - 1):
				right = right.next
				if right == None:
					break
			
			if right == None:
				break
			
			temp = right.next
			right.next = None
			right = temp
			rev_list = self.reverse_list(left)
			curr.next = rev_list
			left.next = temp
			curr = left
			left = right
		
		return dummy.next
		
	def reverse_list(self, lst):
		tail = None
		curr = lst
		
		while curr:
			temp = curr.next
			curr.next = tail
			tail = curr
			curr = temp
		
		return tail
