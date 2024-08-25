# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        oddList = head 
        evenList = head.next
        evenHead = evenList

        while evenList and evenList.next:
            # the even pointer will point to the next odd
            oddList.next = evenList.next
            oddList = oddList.next
            # the odd pointer will point to the next even
            evenList.next  = oddList.next
            evenList = evenList.next
            # then we will change the current respective list, to the next one.
        oddList.next = evenHead
        return head

# Time complexity is O(n), very good question to get some intuition about linked list
# Space complexity, O(1)
