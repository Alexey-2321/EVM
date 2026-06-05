class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        
        total_tank = 0   # Общий баланс по всем станциям
        curr_tank = 0    # Текущий баланс от стартовой станции
        start = 0        # Индекс предполагаемой стартовой станции
        
        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff
            
            # Если бак опустел, начинаем заново со следующей станции
            if curr_tank < 0:
                start = i + 1
                curr_tank = 0
        
        # Если общий баланс неотрицательный, возвращаем start
        return start if total_tank >= 0 else -1
        