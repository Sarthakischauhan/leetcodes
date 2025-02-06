class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        end = len(nums) - 1
        start = 0

        while end > start:
            curr = nums[start] + nums[end]
            if curr == k:
                count += 1
                start += 1 
                end -= 1
            elif curr < k:
                start += 1
            else:
                end -= 1
        return count 

# Always remember to pair when working with pairs and using two pointers
