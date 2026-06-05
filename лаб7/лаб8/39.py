class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtrack(start, current, remaining):
            # Базовый случай: сумма достигнута
            if remaining == 0:
                result.append(current[:])
                return
            
            # Базовый случай: сумма превышена — обрезаем ветку
            if remaining < 0:
                return
            
            # Перебираем кандидатов, начиная с индекса start
            # start гарантирует, что мы не будем генерировать дубликаты
            # типа [2,3] и [3,2] — только неубывающие комбинации
            for i in range(start, len(candidates)):
                # Выбор: включаем candidates[i]
                current.append(candidates[i])
                
                # Исследуем дальше
                # i (не i+1) позволяет использовать тот же элемент снова
                backtrack(i, current, remaining - candidates[i])
                
                # Отмена выбора (backtrack)
                current.pop()
        
        backtrack(0, [], target)
        return result