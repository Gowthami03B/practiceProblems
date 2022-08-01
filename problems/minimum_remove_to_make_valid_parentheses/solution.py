class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()#indexes of invalid parenthesis to be removed
        stack = []
        for i, c in enumerate(s):
            if c not in "()":#if its a aplhabet
                continue
            if c == "(":#add open to stack
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)#if balance happens and not stack and single closing bracket, add to indexes
            else:
                stack.pop()#when closing comes, pop
        #union both set and stack
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
    
    def minRemoveToMakeValidTwoPass(self, s: str) -> str:
        def delete_invalid(string, opening, closing):
            res = []
            balance = 0
            for c in string:
                if c == opening:
                    balance += 1
                elif c == closing:
                    if balance == 0:
                        continue#ignore current character
                    balance -= 1
                res.append(c)
            return "".join(res)
        
        s = delete_invalid(s,"(",")")#start to end, balance any invalid closing brackets"("
        s = delete_invalid(s[::-1],")", "(")#end to start on the above s to remove any invalid opening"("
        return s[::-1]#reverse of s