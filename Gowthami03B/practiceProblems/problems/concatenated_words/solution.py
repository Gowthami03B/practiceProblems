class Trie:
    def __init__(self):
        self.root = {}
        
    #worst case, if the words has no concatenated words, then O(S) - trie with all chars in all words, O(N.M) -N no of words, M length of longest string
    def insert(self, word):
        node = self.root
        for i, c in enumerate(word):
            node = node.setdefault(c,{})#create new {}
            if '$' in node:#when you reach the end, say '$':cat, then for 's'
                #say now you get dogcatsdog, after reaching '$':dog,search if catsdog exists
                if self.exists(word[i+1:]):#check if s exists #check if catsdog exists
                    return False#if so return False
                else:
                    continue#continue and insert s
        node['$'] = word
        return True
    
    def exists(self, word):
        node = self.root
        for i, c in enumerate(word):
            if c in node:#s is not in node
                node = node[c]
                if '$' in node:#reached here after $:cats
                    #if i is end of word or if dog exists, return true
                    if i == len(word)-1 or self.exists(word[i+1:]):
                        return True
                    else:
                        continue
            else:
                return False

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        res = []
        words.sort(key=len)#from small words, we make big words, hence sort by len
        for word in words:
            if not trie.insert(word):#if the word cannot be inserted into the trie, that word is the concatenated word
                res.append(word)
        print(trie.root)
        return res