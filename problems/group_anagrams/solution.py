from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsMap = defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            wordsMap[tuple(count)].append(s)
            # wordsMap["".join(sorted(s))].append(s)
        print(wordsMap)
        for key,val in wordsMap.items():
            res.append(val)
        return res