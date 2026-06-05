class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        # dp[i] - длина LIS, заканчивающейся на nums[i]
        dp = [1] * n  # Каждый элемент сам по себе - подпоследовательность длины 1
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)