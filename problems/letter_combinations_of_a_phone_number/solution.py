from itertools import combinations
class Solution:
    #O(4^N).N,O(N)
    # That is, lock the first letter in, and solve all the possible combinations that start with that letter.
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index,path):
             # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            possible_letters = mapping[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index+1,path)
                 # Backtrack by removing the letter before moving onto the next
                path.pop() #say 23, after generating, ad, we pop d to generate ae,af and then pop a to get bd,be,bd, and so on
            
        combinations =[]
        backtrack(0,[])
        return combinations

    def letterCombinations1(self, digits: str) -> List[str]:
        lookup = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        letter_lists = []
        for ch in digits:
            letter_lists.append(lookup[ch])
            
        while len(letter_lists) > 1:
            l2 = letter_lists.pop()
            l1 = letter_lists.pop()
            combos = []
            for i in l1:
                for j in l2:
                    combos.append(i+j)
            letter_lists.append(combos)
            
        return [] if not letter_lists else letter_lists[0]