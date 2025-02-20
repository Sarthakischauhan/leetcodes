class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0,0
        maxSub = 0
        sub = ""
        i = 0
        while right < len(s):
            if s[right] not in sub:
                sub += s[right]
                maxSub = max(maxSub, len(sub))
                right += 1
            else:
                left += 1
                sub = s[left:right]
        return maxSub
