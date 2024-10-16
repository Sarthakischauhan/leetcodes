class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

            n = len(nums)

            # take transpose and then reverse

            for i in range(n):
                for j in range(i + 1, n):
                    nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
                nums[i] = nums[i][::-1]

            print(nums)

# I took help for taking the transpose of the matrix 
# Time complexit O(n2) and space is constant
