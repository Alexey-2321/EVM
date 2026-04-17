class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        #  считаем часы для скорости k
        def hours_needed(k):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            return total_hours
        
        
        left = 1                        # минимальная скорость
        right = max(piles)              # максимальная скорость
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Проверяем, успевает ли со скоростью mid
            if hours_needed(mid) <= h:
                
                right = mid
            else:
                
                left = mid + 1
        
        return left