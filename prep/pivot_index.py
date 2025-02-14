class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ## Find pivot index
        # pivot index -> sum(left_integers) == sum(right_integers)
        leftsum = 0 
        S = sum(nums)
        if S - nums[0] == 0:
            return 0
        for i in range(len(nums)):            
            if ( (S - leftsum - nums[i]) == leftsum ):
                return i 
            leftsum += nums[i]
        return -1
