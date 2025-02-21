class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            # Check for the sum till now, if the current element is:
            #   greater than the current max sum
            maxSum = max(nums[i], maxSum + nums[i])
            res = max(res, maxSum)
        return res