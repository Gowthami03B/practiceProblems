"""
Part 2: Coding
Find the first word in an array of words that matches a string pattern.

Example:
String[] words = {"cat", dada", breath" , "taking", "doll"}
String pattern = "drctkla"
String pattern = "rdatlbohe"

Answer - cat
Answer - breath

return "-" if can't be found
"""
def find_word_in_pattern_dict(words, pattern):
    pattern_map = defaultdict(int)
    for s in pattern:
        pattern_map[s] += 1
    print(pattern_map)
    for word in words:
        word_map = defaultdict(int)
        for c in word:
            word_map[c] += 1
        for char, count in word_map.items():
            if char in pattern_map:
                if pattern_map[char] > 0:
                    word_map[char] -= 1
        if sum(word_map.values()) == 0:
            return word

def find_word_in_pattern_counter(words, pattern):
    pattern_count = Counter(pattern)
    for word in words:
        word_count = Counter(word)
        isValid = True
        for c in word:
            if c not in pattern_count:
                isValid = False
            elif pattern_count[c] < word_count[c]:
                isValid = False
        if isValid:
            return word
                
def find_word_in_pattern(words, pattern):
    pattern_count = [0]*26
    for c in pattern:
        pattern_count[ord(c)-ord('a')] +=1
    for word in words:
        word_count = [0]*26
        for i in range(len(word_count)):
            word_count[i] = pattern_count[i]
        for i in range(len(word)):
            c = word[i]
            if word_count[ord(c)-ord('a')] > 0:
                word_count[ord(c)-ord('a')] -=1
            else:
                break
        if i == len(word)-1:
            return word

words = ["cat", "dada", "breath" , "taking", "doll"]
pattern = "rdatlbohe"
print(find_word_in_pattern(words, pattern))
