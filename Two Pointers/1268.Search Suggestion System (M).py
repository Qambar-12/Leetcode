class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #lexographically ---> Alphabetical order
        #words having common prefixes or matching characters would be adjacent to eachother after sorting O(nlogn)
        products.sort()
        res = []   #List of lists of len(res) == len(SearchWord)
        #now we can use our standard two-pointer algorithm to implement the solution
        l , r = 0 , len(products)-1
        for i in range(len(searchWord)):
            c = searchWord[i]
            #to eliminate invalid products so there are only valid products in b/w our pointers
            while l <= r and (len(products[l]) < i+1 or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) < i+1 or products[r][i] != c):
                r -= 1
            #after the while loops all words in our window are valid however we need to check for size of window i.e <= 3 
            res.append([])
            windowSize = r - l + 1
            for j in range(min(3,windowSize)):
                res[-1].append(products[l+j])
        return res            




