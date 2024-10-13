class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        cnt = 0
        left = 0 
        ## Cnt stands for Count and not anything else
        maxCnt = cnt
        ks = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                ks += 1

            while ks > k:
                if nums[left] == 0:
                    ks -= 1
                left += 1
            maxCnt = max(maxCnt, right - left + 1)

        return maxCnt

# Learned a new concept where I don't have a fixed size window
# So in this case we are using two pointers
