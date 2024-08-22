# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		# find the middle node of a linked list  
        if not head.next:
            return head      
        fast = head
        slow = head
        prev = None 
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        # prev = slow.next 
        prev = prev.next
        return prev

# Just took inspo from the delete middle node question
# O(n) time complexity
# O(1) space complexity.
