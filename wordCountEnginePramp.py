"""
Word Count Engine
Implement a document scanning function wordCountEngine, which receives a string document and returns a list of all unique words in it and their number of occurrences, sorted by the number of occurrences in a descending order. If two or more words have the same count, they should be sorted according to their order in the original sentence. Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time while keeping a polynomial space complexity.

Examples:

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"]

#strip the whole sentence with punctuation - convert to smallcase
#split words by space - array/list
#go over the list and then add values to a hashmap by counting#
#returning based on higest occurrences 
#when count matches, recheck original split array and compare indices
#insertion order, return highest occurrences

[ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
"""
#O(N LOG N), O(N)
import re
from collections import OrderedDict
def word_count_engine(document):
    finalDict = OrderedDict()
    document = re.sub(r'[^\w\s]', '', document.lower()) #involves creation of new string, hence space complexity
    words = document.split() #splits a string with whitespace as delimiter
    res = []
    #print(document)
    print(words)
    for w in words:
        if w in finalDict:
            finalDict[w] += 1
        else:
            finalDict[w] = 1
    print(finalDict) #construct map in order of words
    test = sorted( finalDict.items(),
                                key=lambda kv:(kv[1],kv[0]),
                                reverse=True) 
    print(test)
    finalDict = sorted( finalDict.items(),
                                key=lambda kv:kv[1],
                                reverse=True)                     
    for k,v in finalDict:
        res.append([k,str(v)])
    return res
  #print(sorted_dict)
document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
print(word_count_engine(document))
