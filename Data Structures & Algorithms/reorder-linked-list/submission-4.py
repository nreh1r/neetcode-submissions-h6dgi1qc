# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def reorderList(self, head: Optional[ListNode]) -> None:
		length = 0
		count_head = head
		while count_head:
			length += 1
			count_head = count_head.next
		
		pivot_index = length // 2
		
		list1, list2 = ListNode(), ListNode()
		list1_pointer = list1
		counter = 0
		curr = head
		while curr:
			if counter <= pivot_index:
				list1_pointer.next = curr
				list1_pointer = list1_pointer.next
				curr = curr.next
				counter += 1
			else:
				list2.next = curr
				list1_pointer.next = None
				break
		
		list1 = list1.next
		list2 = list2.next
		
		tail = None
		curr = list2
		while curr:
			temp = curr.next
			curr.next = tail
			tail = curr
			curr = temp
		
		dummy = ListNode()
		curr = dummy
		counter = 0
		
		while list1 and tail:
			if counter % 2:
				curr.next = tail
				tail = tail.next
			else:
				curr.next = list1
				list1 = list1.next
			curr = curr.next
			counter += 1
		
		curr.next = list1
		
		head = dummy.next
