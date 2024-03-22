class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        res = [0,0]
        d1,d2 = Counter(nums1),Counter(nums2)
        if len(d1.keys()) >= len(d2.keys()):
            for val in d1.keys():
                if val in d2.keys():
                    res[0] += d1[val]
                    res[1] += d2[val]
        else:
            for val in d2.keys():
                if val in d1.keys():
                    res[0] += d1[val]
                    res[1] += d2[val] 
        return res                     
