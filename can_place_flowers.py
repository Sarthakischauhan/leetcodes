class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        l = len(flowerbed)
        for i in range(l):
            if flowerbed[i] == 0:
                left = (i==0) or (flowerbed[i-1] ==  0)
                right = (i == l-1) or (flowerbed[i+1] == 0)
                if left & right:
                    count += 1
                    # changing the current place as taken is important
                    flowerbed[i] = 1
        return count >= n
# Time Complexity O(n) 
# Space Complexity O(1)

