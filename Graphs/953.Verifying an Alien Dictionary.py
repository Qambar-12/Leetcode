class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
       #the order of letters in Alien Dictionary is not same as our regular English a-z sequence
       #instead its some permutation of those 26 lower case english letters

       #we need to start comparing by first differing char 
       #if word A is prefix of word B then it must precede B
        hashmap = {ch:index for index , ch in enumerate(order)}
        #comparing each of the adjacent pairs i.e indirectly compare each of word with its following words due to transitive property
        for i in range(len(words)-1):
            #indexing i+1 never flags index out of bound b/c our loop runs one less time
            w1 , w2 = words[i] , words[i+1]
            for j in range(len(w1)):
                #i.e our word 2 finishes but loop still running on word 1
                if j == len(w2):
                    return False
                #compare when differing character
                if w1[j] != w2[j]:
                    if hashmap[w1[j]] > hashmap[w2[j]]:
                        return False
                    #we found our differing character where the condition is satisfied
                    else:
                        break    
        #finally after all comparasion we can return True
        return True
