class Solution(object):
    def evalRPN(self, tokens):
    
        stack = []
        
        for token in tokens:
            if token == '+':
                b = stack.pop()  
                a = stack.pop()  
                stack.append(a + b)
                
            elif token == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
                
            elif token == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
                
            elif token == '/':
                b = stack.pop()
                a = stack.pop()
                result = int(float(a) / b)
                stack.append(result)
                
            else:
                # Это число
                stack.append(int(token))
        
        # рез
        return stack[0]