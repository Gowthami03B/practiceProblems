class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_list = sentence.split(" ")
        for idx, word in enumerate(words_list):
            if word.startswith(searchWord):
                return idx + 1
        return -1