class TrieNode:
    def __init__(self):
        self.children = {} #trie data structure is nothing but a dict
        self.word = False #to mark if a word is complete
        
class WordDictionary:

    def __init__(self):
        # self.wordmap = TrieNode()
        self.wordmap = {}

    def addWord(self, word: str) -> None:
        # curr = self.wordmap
        # for ch in word:
        #     if ch not in curr.children:
        #         curr.children[ch] = TrieNode()
        #     curr = curr.children[ch]
        # curr.word = True
        curr = self.wordmap
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['$'] = True

    def search(self, word: str) -> bool:
        
        def search_in_child(word, curr):
            for i, ch in enumerate(word):
                if ch not in curr:
                    if ch == ".":
                        for child in curr:
                            if child != '$' and search_in_child(word[i+1:], curr[child]):
                                return True
                    return False
                else:
                    curr = curr[ch]
            return '$' in curr
                    
        return search_in_child(word, self.wordmap)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)