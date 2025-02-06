class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, count = 0,0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
            else:
                count += 1 

        nums[start:] = [0] * count
    
