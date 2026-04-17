class Solution(object):
    def groupAnagrams(self, strs):
        from collections import defaultdict
        
        anagrams = defaultdict(list)
        
        for word in strs:
            # Сортируем буквы в слове и используем как ключ
            key = ''.join(sorted(word))
            anagrams[key].append(word)
        
        # значения словаря 
        return list(anagrams.values())