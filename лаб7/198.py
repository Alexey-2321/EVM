class Solution(object):
    def rob(self, nums):
        # Обработка частных случаев
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 - максимальная сумма до дома i-2
        # prev1 - максимальная сумма до дома i-1
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            # Для текущего дома выбираем максимум:
            # либо не грабим его (prev1), либо грабим + сумма до i-2 (prev2 + nums[i])
            current = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = current
            
        return prev1