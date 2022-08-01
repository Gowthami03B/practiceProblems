from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsMap = defaultdict(list)
        res = []
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1#create a 26 char array and store values
            wordsMap[tuple(count)].append(s)
            # wordsMap["".join(sorted(s))].append(s)
        # print(wordsMap)
        return [value for value in wordsMap.values()]
    
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for s in strs:
            temp = s
            sorted_s = "".join(sorted(s))#sorting, making a string - extra space
            group_anagrams[sorted_s].append(s)
        print(group_anagrams)
        return [value for value in group_anagrams.values()]