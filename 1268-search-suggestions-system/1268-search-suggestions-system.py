import re
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        for i in range(len(searchWord)):
            print(searchWord[0:i+1],i)
            res.append(self.suggest(products, searchWord[0:i+1]))
        return res
        
    def suggest(self,products, searchStr):
        res = []
        for prod in products:
            if re.search(r'^'+ searchStr, prod):
                if len(res) < 3:
                    res.append(prod)
        return res