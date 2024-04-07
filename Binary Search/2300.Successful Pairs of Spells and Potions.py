class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        #intial sorting operation is mlogm which is still better than O(n.m) time complexity
        potions.sort()
        for s in spells:
            #checking extreme bounds first
            if s*potions[0] >= success:
                res.append(len(potions))
            elif s*potions[-1] < success:
                res.append(0)  
            else:
                #Binary search algorithm
                l , r = 0 , len(potions)-1
                #initialized with len(potions) i.e starting off with assumption that no potions work for spell 
                index = len(potions) #weakest potion (i.e furthest left) that works for a spell
                while l <= r:
                    mid = l + ((r-l)//2)
                    if s*potions[mid] >= success:
                        r = mid - 1
                        index = mid
                    else:
                        l = mid + 1
                res.append(len(potions)-index)       
        return res                 