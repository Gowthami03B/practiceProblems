class TrieNode:
    def __init__(self):
        self.children = {} #trie data structure is nothing but a dict
        self.word = False #to mark if a word is complete
        
class WordDictionary:

    def __init__(self):
        # self.wordmap = TrieNode()
        self.wordmap = {}

    def addWord(self, word: str) -> None:
        #if we want to use TrieNode class and take advantage of self.word to mark end of a word
        # curr = self.wordmap
        # for ch in word:
        #     if ch not in curr.children:
        #         curr.children[ch] = TrieNode()
        #     curr = curr.children[ch]
        # curr.word = True
        curr = self.wordmap
        for ch in word:
            curr = curr.setdefault(ch,{})
            # if ch not in curr:#if ch is not in map
            #     curr[ch] = {}#create new
            # curr = curr[ch]#else get the map and assign to curr
        curr['$'] = True#marks end of word
        # print(self.wordmap)
        """
        'd': {'a': {'d': {'$': True} : {'d' : {'y' : {'$' : True}}}
        {'b': {'a': {'d': {'$': True}}}}
{'b': {'a': {'d': {'$': True}}}, 'd': {'a': {'d': {'$': True}}}}
{'b': {'a': {'d': {'$': True}}}, 'd': {'a': {'d': {'$': True}}}, 'm': {'a': {'d': {'$': True}}}}
        """

    def search(self, word: str) -> bool:
        #recursive dfs
        #when we encounter a ".", we need to check in every child for the next subsequent characters through the length of the word
        def search_in_child(word, curr):
            for i, ch in enumerate(word):
                if ch not in curr:
                    if ch == ".":#if it's a dot
                        for child in curr:#for every child in curr
                            if child != '$' and search_in_child(word[i+1:], curr[child]):#we search for the next part word[i+1:] and curr[child]
                                return True
                    return False
                else:
                    curr = curr[ch]#get curr if it exists
            return '$' in curr#if a word is found, to check if it's the end of word
                    
        return search_in_child(word, self.wordmap)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)