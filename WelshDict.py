class Solution(object):
    def __init__(self):
        # None for index 0 we want from index 1
        self.alphabets = ['None','a','b','c','ch','dd','d','e', 'f', 'ff', 'g', 'ng', 'h', 'i', 'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
            
    def alphabetIndex(self, word):
        print("word",word)
        # convert each alphabet into it's index value in decimal point
        indexValue = ''
        i = 0
        while i < len(word):
            if (i+1 < len(word) and word[i]+word[i+1] in self.alphabets):
                indexNumber = self.alphabets.index(word[i]+word[i+1])
                # calculate index value
                if (i == 0):
                    indexValue = str(indexNumber) + '.'
                else:
                    indexValue += str(indexNumber)
                # increment i value
                i = i+2
            else:
                indexNumber = self.alphabets.index(word[i])
                # calculate index value
                if (i == 0):
                    indexValue = str(indexNumber) + '.'
                else:
                    indexValue += str(indexNumber)
                # increment i value
                i = i+1
        print(word, indexValue)
        # convert string index value to a number.
        return float(indexValue)
            
        
    def logic(self, words):
        words.sort(key=self.alphabetIndex)
        print(words)
# Main
obj = Solution()
obj.logic(["ddr","nah","dea","dd","ngah"])
