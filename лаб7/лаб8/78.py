class Solution(object):
    def subsets(self, nums):
        result = []
        
        def backtrack(start, current):
            # Добавляем текущее подмножество в результат
            # current[:] создаёт копию, так как current будет меняться
            result.append(current[:])
            
            # Перебираем оставшиеся элементы, начиная с индекса start
            for i in range(start, len(nums)):
                # Выбор: включаем nums[i] в текущее подмножество
                current.append(nums[i])
                
                # Исследуем дальше с этим выбором
                # i + 1 гарантирует, что каждый элемент используется не более одного раза
                backtrack(i + 1, current)
                
                # Отмена выбора (backtrack): убираем nums[i]
                # чтобы попробовать другие варианты на этом уровне
                current.pop()
        
        backtrack(0, [])
        return result