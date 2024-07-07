class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = 0
        for candy in candies:
            if candy > max_value:
                max_value = candy

        res = [] 
        for num in candies:
            if ( num + extraCandies >= max_value ):
                res.append(True)
            else:
                res.append(False)
        return res

# Have to update it to optimum solution
# Right now runs in O(n) --> not bad, considering brute force solution 
# Space complexity also O(n) 
