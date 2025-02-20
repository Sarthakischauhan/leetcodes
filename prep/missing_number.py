class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = set(range(n+1))

        for num in nums:
            if num in s:
                s = s - set([num])

        if not s: return 0 
        return list(s)[0]

# Vibe coding is literally what this is called
