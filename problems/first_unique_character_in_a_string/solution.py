from collections import OrderedDict
from collections import Counter
class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     charCount = OrderedDict()
    #     for c in s:
    #         if c in charCount:
    #             charCount[c] += 1
    #         else:
    #             charCount[c] = 1
    #     for k,v in charCount.items():
    #         if v == 1:
    #             return s.find(k)
    #     return -1
    
    def firstUniqChar(self, s: str) -> int:
        charCount = Counter(s) #Can use OrderedDict if you don't remember this
        #Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})
# Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})
# Counter({'a': 2, 'b': 2}) - first counts by highest frequency, then original order in string
        print(charCount)
        for idx,ch in enumerate(s):#we also get a need to keep a count of iterations.
            if charCount[ch] == 1:
                return idx
        return -1
    