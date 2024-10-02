class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        n, m = len(nums1), len(nums2)
        occ1 = {}
        occ2 = {}
        for i in range(n):
                occ1[nums1[i]] = occ1.get(nums1[i], 0) +  1
        for i in range(m):
            occ2[nums2[i]] = occ2.get(nums2[i], 0) + 1
        
        res = [[], []]
       
        for j in range(n):
            if not occ2.get(nums1[j], 0) and nums1[j] not in res[0]:
                res[0].append(nums1[j])
        
        for j in range(m):
            if not occ1.get(nums2[j],0) and nums2[j] not in res[1]:
                        res[1].append(nums2[j])
        

        return res


# Hey it works ok, time complexity is O(Max(m,n)) so essentially a linear time complexity. 
# Space complexity is linear as well

