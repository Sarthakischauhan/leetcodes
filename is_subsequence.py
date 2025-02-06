class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        
        start_s = 0
        start_t = 0
        while start_s < len(s) and start_t < len(t):
            if t[start_t] == s[start_s]:
                start_s += 1

            # Keep updating the pointer for traversing t string
            start_t += 1

        if start_s == len(s):
            return True
        return False
