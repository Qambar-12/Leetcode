class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charDic = Counter(chars)
        res = 0
        for w in words:
            wordDic = defaultdict(int)
            #Boolean Flag
            good = True
            for c in w:
                wordDic[c] += 1
                if c not in charDic.keys() or wordDic[c] > charDic[c]:
                    good = False
                    break
            if good:
                res += len(w)       
        return res
