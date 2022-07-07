class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        map_chars = defaultdict(int)
        for c in chars:
            map_chars[c] += 1
            
        sum_len = 0
        for word in words:
            count_chars = Counter(word)
            isValid = True
            for c in word:
                if c not in map_chars:
                    isValid = False
                if c in map_chars and map_chars[c] < count_chars[c]:
                    isValid = False
            if isValid:
                sum_len += len(word)
        return sum_len
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) if collections.Counter(word) <= collections.Counter(chars) else 0 for word in words)
        # sum_len = 0
        # for word in words:
        #     if collections.Counter(word) <= collections.Counter(chars):
        #         sum_len += len(word)
        # return sum_len
        