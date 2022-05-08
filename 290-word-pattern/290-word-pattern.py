class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        print(words)
        if len(words) != len(pattern):
            return False
        wordMap = {}
        for i in range(len(words)):
            p = 'char_' + pattern[i]
            w = 'word_' + words[i]
            if 'char_'+ pattern[i] not in wordMap:
                wordMap['char_' +pattern[i]] = i
            if 'word_' + words[i] not in wordMap:
                wordMap['word_' +words[i]] = i
            print(wordMap)
            if wordMap[p] != wordMap[w]:
                return False
        return True
        
                