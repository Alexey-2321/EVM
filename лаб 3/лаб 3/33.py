class Solution(object):
    def search(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            
            # Определяем, какая половина отсортирована
            
            #  ЛЕВАЯ 
            if nums[left] <= nums[mid]:
                
                if nums[left] <= target < nums[mid]:
                    # target в левой половине
                    right = mid - 1
                else:
                    # target в правой половине
                    left = mid + 1
            
            # ПРАВАЯ 
            else:
                
                if nums[mid] < target <= nums[right]:
                    # target в правой половине
                    left = mid + 1
                else:
                    # target в левой половине
                    right = mid - 1
        
        return -1