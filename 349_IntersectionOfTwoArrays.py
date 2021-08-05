class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        
        nums2.sort()
        
        for i in nums1:
            j =  bisect.bisect_left(nums2, i)
            if len(nums2) > 0 and len(nums2) > j and nums2[j]==i:
                res.add(i)
        return(res)
