class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        #there is no factor of a number greater than half of it except the number itself
        #1 and n will always be in the sorted list
        list_ = [1]
        for i in range(2,(n//2)+1):
            if not (n % i):
                list_.append(i)
        list_.append(n)
        print(list_)
        return list_[k-1] if len(list_) >= k else -1  
     
