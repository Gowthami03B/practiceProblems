class Trie:

    def __init__(self):
        self.wordmap={}

    def insert(self, word: str) -> None:#O(M) -length of word to be inserted
        curr = self.wordmap
        for ch in word:
            curr= curr.setdefault(ch,{})
        curr['$'] = True

    def search(self, word: str) -> bool:#O(M) -length of word to be searched
        curr = self.wordmap
        for ch in word:
            if ch in curr:
                curr = curr[ch]
            else:
                return False
        return True if '$' in curr else False

    def startsWith(self, prefix: str) -> bool:#O(M) -length of prefix to be searched
        curr = self.wordmap
        for ch in prefix:
            if ch in curr:
                curr = curr[ch]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)