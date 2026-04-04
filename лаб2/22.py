class Solution(object):
    def generateParenthesis(self, n):
        result = []
        
        def backtrack(current, left_used, right_used):
            # Если использовали все скобки
            if left_used == n and right_used == n:
                result.append(current)
                return
            
            # Если можем добавить открывающую 
            if left_used < n:
                backtrack(current + '(', left_used + 1, right_used)
            
            # Если можем добавить закрывающую
            if right_used < left_used:
                backtrack(current + ')', left_used, right_used + 1)
        
        backtrack("", 0, 0)
        return result