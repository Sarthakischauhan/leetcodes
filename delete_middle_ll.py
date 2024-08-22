# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force approach.
        ## count the length of the linked list 
        if not head.next:
            return None
        count,curr = 0, head  
        while curr:
            count += 1
            curr = curr.next
        middle = count//2 - 1
        current = head
        for i in range(middle):
            # we want to run it one less than the middle node
            current = current.next
            print(current==head)
        current.next = current.next.next
        return head

# A poorly written code but has the same time complexity as other solns O(n) 
# You can argue that I am not a big fan of clean code
# LC says that the space complexity is O(1), hell even I don't know
