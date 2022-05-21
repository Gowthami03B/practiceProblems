class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "*+/-":
                stack.append(int(token)) #bcs token is string
                continue
            num2 = stack.pop()
            num1 = stack.pop() #first number is second popped one on stack
            res = 0
            if token == "+":
                res = num1+num2
            elif token == "-":
                res = num1 - num2
            elif token == "*":
                res = num1 * num2
            else:
                res = int(num1 / num2)
            stack.append(res)
        return stack.pop() #last element is final result
    
    def evalRPNWithLambda(self, tokens: List[str]) -> int:
        #lambda returns a function that takes 2 params
        #create a dict with key-value pairs between operator and operations
        operations = {
            "+" : lambda a,b : a+b,
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a *b,
            "/" : lambda a,b : int(a/b)
        }
        stack = []
        for token in tokens:
            if token not in "*+/-":
                stack.append(int(token)) #bcs token is string
                continue
            num2 = stack.pop()
            num1 = stack.pop() #first number is second popped one on stack
            operation = operations[token] #access the operations dict
            stack.append(operation(num1,num2))
        return stack.pop() #last element is final result
    