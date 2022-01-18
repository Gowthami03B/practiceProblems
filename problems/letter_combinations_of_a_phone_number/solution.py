class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        lookup = {
            "2": ["a", "b","c"],
            "3": ["d", "e","f"],
            "4": ["g", "h","i"],
            "5": ["j", "k","l"],
            "6": ["m", "n","o"],
            "7": ["p", "q","r", "s"],
            "8": ["t", "u","v"],
            "9": ["w", "x","y", "z"]            
        }
        
        letters = []
        for digit in digits:
            letters.append(lookup[digit])
            
        while len(letters) > 1:
            list1 = letters.pop()
            list2 = letters.pop()
            
            combinations = []
            for i in list2:
                for j in list1:
                    combinations.append(i + j)
                    
            letters.append(combinations)
        
        return letters[0]
            
                