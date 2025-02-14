class Solution:
    def isUnique(self, a):
        return len(set(a)) == len(a)

    def maxLength(self, arr: List[str]) -> int:
        if not arr: return 0
        n = len(arr)
        maxlen = 0
        def backtrack(i, currStr):
            nonlocal maxlen
            maxlen = max(maxlen, len(currStr))

            for j in range(i,len(arr)):
                if self.isUnique(arr[j]) and not set(arr[j]).intersection(set(currStr)):
                    # Send to the next element with the current path string.
                    backtrack(j+1, currStr + arr[j])
       
        backtrack(0, "")

        return maxlen

# Remember
# We check one element with all elements. Be sure to check it before interview.
