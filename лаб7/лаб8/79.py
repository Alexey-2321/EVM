class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        def backtrack(row, col, index):
            # Базовый случай: все буквы слова найдены
            if index == len(word):
                return True
            
            # Проверка выхода за границы
            if row < 0 or row >= m or col < 0 or col >= n:
                return False
            
            # Проверка совпадения буквы
            if board[row][col] != word[index]:
                return False
            
            # Выбор: временно отмечаем ячейку как использованную
            temp = board[row][col]
            board[row][col] = '#'  # Маркер посещённой ячейки
            
            # Исследуем все 4 направления
            # Если любое вернёт True — слово найдено
            found = (backtrack(row + 1, col, index + 1) or  # вниз
                     backtrack(row - 1, col, index + 1) or  # вверх
                     backtrack(row, col + 1, index + 1) or  # вправо
                     backtrack(row, col - 1, index + 1))    # влево
            
            # Отмена выбора: восстанавливаем ячейку
            board[row][col] = temp
            
            return found
        
        # Запускаем поиск из каждой ячейки
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(i, j, 0):
                        return True
        
        return False
        