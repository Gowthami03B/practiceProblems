class Trie:

    def __init__(self):
        self.wordmap={}

    def insert(self, word: str) -> None:
        curr = self.wordmap
        for ch in word:
            curr= curr.setdefault(ch,{})
        curr['$'] = True

    def search(self, word: str) -> bool:
        curr = self.wordmap
        for ch in word:
            if ch in curr:
                curr = curr[ch]
            else:
                return False
        return '$' in curr

    def startsWith(self, prefix: str) -> bool:
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