class Solution(object):
    def permute(self, nums):
        result = []
        
        def backtrack(current, used):
            # Базовый случай: перестановка полной длины готова
            if len(current) == len(nums):
                result.append(current[:])
                return
            
            # Перебираем все элементы
            for i in range(len(nums)):
                # Пропускаем уже использованные элементы
                if used[i]:
                    continue
                
                # Выбор: включаем nums[i]
                used[i] = True
                current.append(nums[i])
                
                # Исследуем дальше
                backtrack(current, used)
                
                # Отмена выбора (backtrack)
                current.pop()
                used[i] = False
        
        backtrack([], [False] * len(nums))
        return result