class Solution:
    def findRotation(self, nums: List[List[int]], target: List[List[int]]) -> bool:
        n = len(nums)
        for t in range(4):
            for i in range(n):
                for j in range(i + 1, n):
                    nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
                nums[i] = nums[i][::-1]
            if nums == target:
                return True

        return False

# Leetcode easy, just needs to call rotating matrix 4 times (90*4 = 360)
