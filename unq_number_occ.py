class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for num in arr:
           d[num] = d.get(num,0) + 1

        s = set(d.values())

        if( len(s) == len(d.values())):
            return True

        return False 

# Bruh I should not even be posting this. 
