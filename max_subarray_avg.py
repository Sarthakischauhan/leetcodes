class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n  = len(nums)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, n):
            curr_sum += nums[i] - nums[i-k]
            if( curr_sum > max_sum ):
                max_sum = curr_sum
        return max_sum / 

# Time complexity is O(n), my solution is using O(n*k)
# Space complexity is O(1)
