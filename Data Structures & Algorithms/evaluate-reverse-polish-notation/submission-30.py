class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = 0
        stack = []
        results = []
        ops = {'+', '-', '*', '/'}
        for char in tokens:
            if char not in ops:
                stack.append(int(char))
                

            elif char == '+':
                temp = stack[-2] + stack[-1]
            elif char == '-':
                temp = stack[-2] - stack[-1]
            elif char == '*':
                temp = stack[-2] * stack[-1]
            elif char == '/':
                temp = int(stack[-2] / stack[-1]) 
            if char in ops:
                print(temp)  
                stack.pop()
                stack.pop()
                stack.append(temp)
                # print(f"stack = {stack}")
        
        print(f"stack = {stack}")
        return(stack[0])


