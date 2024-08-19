class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:	
		#ITERATIVE APPROACH
		def iterative(head,none):
			 curr, prev = head, None
			 while curr:
			     nxt = curr.next
			     curr.next = prev
			     prev = curr
			     curr = nxt
			 return prev

        # RECURSIVE APPROACH
        def recurse(curr,prev):
            if ( curr == None):
                return prev
            else:
                nxt = curr.next
                curr.next = prev
                prev = curr
                return recurse(nxt, curr)
      	
        return recurse(head, None)

# Time complexity is O(n) in both case
# Space complexity is better in iterative approach. O(1)--> Iterative and O(n)--> Recursive
