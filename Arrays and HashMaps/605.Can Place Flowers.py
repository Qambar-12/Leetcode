class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n :
            return True
        else:
            f = 0
            while f < len(flowerbed):
                if not flowerbed[f]:
                    count = 0
                    if f-1 >= 0:
                        start = 1
                    else:
                        start = 0    
                    while f < len(flowerbed) and not flowerbed[f] :
                        count += 1
                        f += 1      
                    #if the loop breaks when the length of flowerbed exceeds i.e ending value is 0
                    if f >= len(flowerbed):
                        end = 0
                    #if the loop breaks due to encountering 1 so ending value is 1
                    else:
                        end = 1    
                    if (start and end):
                        if count%2:
                            n -= count//2
                            if n <= 0:
                                return True
                        else:
                            n -= (count//2) -1 
                            if n <= 0 :
                                return True
                    elif (not start and end) or (start and not end):
                        n -= count//2
                        if n <=0 :
                            return True                 
                    else:
                        if count%2:
                            n -= (count//2)+1
                            if n <= 0:
                                return True
                        else:
                            n -= (count//2) 
                            if n <= 0:
                                return True              
                f += 1                    
            return not bool(n)
                
