class Solution:
def longestSubarray(self, nums: List[int]) -> int:
    cnt = 0
    left = 0
    
    maxCnt = cnt
    ks = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            ks += 1
        
        while ks > 1:
            if nums[left] == 0:
                ks -= 1
            left += 1
            
        maxCnt = max(maxCnt, right-left) 

    return maxCnt  

# Same question as last time. Just make the total number of 0's allowed to be 1
# Time complexity is O(n)
