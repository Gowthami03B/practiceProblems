class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(path, count_open, count_close):
            
            if count_open == 0 and count_close == 0:
                combinations.append(''.join(path))
                return
            
            if count_open > 0:
                path.append('(')
                generate(path, count_open - 1, count_close)
                path.pop()
            
            if count_close > 0:
                if count_open < count_close:
                    path.append(')')
                    generate(path, count_open, count_close - 1)
                    path.pop()  
        
        combinations = []
        generate([], n, n)
        return combinations
        
        