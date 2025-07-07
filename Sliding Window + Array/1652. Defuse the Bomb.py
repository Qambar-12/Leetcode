class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = [0]*len(code)
        if k == 0:
            return res
        #sliding window of fixed size
        #indices of circular array can possibly go from: 0-k  to n-1+k
        #if these go out of bounds can be handled by mod function
        #if k > 0:
            #sum of fixed window is for element just before window starts
        #else:
            #sum of fixed window is for element just after window ends
        N = len(code)
        l = 0
        curr_sum = 0
        for r in range(N+abs(k)):
            curr_sum += code[r%N]
            if r-l+1 > abs(k):
                curr_sum -= code[l%N]
                l = (l+1) % N
            if r-l+1 == abs(k):
                if k > 0:
                    res[(l-1)%N] = curr_sum
                else:
                    res[(r+1)%N] = curr_sum
        return res            