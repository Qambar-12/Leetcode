class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        dic = {}
        List = []
        for anagram in strs:
            if tuple(sorted(anagram)) in dic:
                insertPos = dic[tuple(sorted(anagram))]
                List[insertPos].append(anagram)
            else:
                dic[tuple(sorted(anagram))] = i
                List.append([])
                List[i].append(anagram)
                i += 1
        return List
