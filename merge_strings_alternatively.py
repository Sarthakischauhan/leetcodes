class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        end = 0; 
        lowest = min(len(word1), len(word2))
        res = ""
        for start in range(lowest):
           res += word1[start] + word2[start]
           end+=1
        if len(word1) >= len(word2):
            res += word1[end:]
        else:
            res += word2[end:]
        return res

# so we are using two pointers here, start and end
# TC --> O(m+n)
# SC --> O(1)

