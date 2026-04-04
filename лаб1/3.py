class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Словарь для хранения последнего индекса каждого символа
        char_index = {}
        left = 0
        max_length = 0
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left: 
                left = char_index[char] + 1 # Сдвигаем левую границу
        
            char_index[char] = right
            
            # текущая длина и обновление максимума
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        
        return max_length