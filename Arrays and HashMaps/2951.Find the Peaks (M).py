class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for m in range(1,len(mountain)-1):
            if mountain[m] > mountain[m-1] and mountain[m] > mountain[m+1]:
                res.append(m)
        return res
