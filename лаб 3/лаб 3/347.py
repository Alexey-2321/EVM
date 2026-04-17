class Solution(object):
    def topKFrequent(self, nums, k):

        from collections import Counter
        
        freq = Counter(nums)# частоты считаем
        
        #  Создаём ведра
        # Индекс ведра это частота, значение это список чисел с этой частотой
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)
        
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result