class Solution(object):
    def isValid(self, s):
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            # Если закрывающая 
            if char in brackets:
                if not stack:
                    return False
                
                if stack[-1] != brackets[char]:
                    return False
                stack.pop()
            # Если открывающая 
            else:
                stack.append(char)
        
       
        return not stack