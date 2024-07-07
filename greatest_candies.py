class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        res = [] 
        for num in candies:
            res.append(num + extraCandies >= max_value)
        return res

# Right now runs in O(n) --> not bad, considering brute force solution 
# Space complexity also O(n) 
