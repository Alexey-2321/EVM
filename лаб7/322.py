class Solution(object):
    def coinChange(self, coins, amount):
        # Инициализируем массив значением amount + 1 (недостижимо большое)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Для суммы 0 нужно 0 монет
        
        # Заполняем dp для всех сумм от 1 до amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Если значение не изменилось, сумму составить невозможно
        return dp[amount] if dp[amount] != amount + 1 else -1